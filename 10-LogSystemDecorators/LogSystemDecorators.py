import sqlite3
import json
import datetime
import logging
from functools import wraps

# Constants
DATABASE_PATH = 'logs.db'
LOG_FILENAME = 'logs.txt'

# Setup logging configuration
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s - %(message)s')

def setup_database(database_path=DATABASE_PATH):
    """Setup the SQLite database for logging."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS function_logs (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                function_name TEXT,
                args TEXT,
                kwargs TEXT,
                result TEXT          
            )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")

def log_func(func):
    """Decorator to log function calls to a file."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function: {func.__name__} - Args: {args} Kwargs: {kwargs} Result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error executing {func.__name__}: {e}")
            return None
    return wrapper

def db_log_func(func):
    """Decorator to log function calls to the database."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            with sqlite3.connect(DATABASE_PATH) as conn:
                cursor = conn.cursor()
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                args_str = json.dumps(args)
                kwargs_str = json.dumps(kwargs)
                cursor.execute("INSERT INTO function_logs (timestamp, function_name, args, kwargs, result) VALUES (?, ?, ?, ?, ?)", 
                               (timestamp, func.__name__, args_str, kwargs_str, result))
                conn.commit()
            return result
        except Exception as e:
            logging.error(f"Error executing {func.__name__} and logging to database: {e}")
            return None
    return wrapper

def fetch_logs_from_db(database_path=DATABASE_PATH):
    """Fetch and print the logs from SQLite database."""
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM function_logs")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

@db_log_func
@log_func
def hello_func(name):
    """Return Hello with the given name."""
    return "Hello " + name

@db_log_func
@log_func
def sum_three_numbers(a, b, c):
    """Return the sum of three numbers."""
    return a + b + c

@db_log_func
@log_func
def csv_file_generator(csv_file_name, data, *, column_separator, row_separator):
    """Prepare an iterable for a CSV file with custom separators and save it."""
    rows = [column_separator.join(map(str, row)) for row in data]
    csv_data = row_separator.join(rows)
    with open(csv_file_name , mode='w') as file:
        file.write(csv_data)
    return csv_file_name 

def main():
    # Setup Database 
    setup_database()

    # Test the functions
    name = 'Your name'
    hello_func(name)
    sum_three_numbers(10, 6, 56.56)
    csv_file_generator('data.csv', [['c1','c2','c3'], [1,2,3]], column_separator=";", row_separator="\n")
    
    # Checking the data in database
    fetch_logs_from_db()

if __name__ == "__main__":
    main()
