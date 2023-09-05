regex_integer_in_range = r"\b\d{6}\b"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(.)\1"	# Do not delete 'r'.


import re
P = input()
print('++++++++++')
print(re.findall(regex_integer_in_range, P))

