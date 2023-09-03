if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    arr_list = list(filter(lambda a: a != max(arr_list) , arr_list)) #find the first max in list and remove all the occurance
    print(max(arr_list)) # second max is our result