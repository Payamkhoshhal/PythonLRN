def swap_case(s):
    result = ''
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            result = result + s[i].lower()
        elif 97 <= ord(s[i]) <= 122:
            result= result + s[i].upper()
        else:
            result = result + s[i]
            
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)