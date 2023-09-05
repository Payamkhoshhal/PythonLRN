def count_substring(string, sub_string):
    substring_len = len(sub_string)
    posibilities = []
    for i in range(len(string) - substring_len + 1):
        posibilities.append( string[i:i+substring_len])
    return posibilities.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)