#There is a horizontal row of N cubes. The length of each cube is given. 
#You need to create a new vertical pile of cubes. The new pile should follow these directions: if  cubes[i] is on top of cubes[j] then 
# sideLength[i] >= sideLength[j].
#When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
#Print Yes if it is possible to stack the cubes. Otherwise, print No.
#Input Format

#The first line contains a single integer T, the number of test cases.
#For each test case, there are 2 lines.
#The first line of each test case contains n , the number of cubes.
#The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

def check(blocks):
    if blocks[0] >= blocks[-1]:
        check_output = blocks.pop(0)
    else:
        check_output = blocks.pop(-1)

    return check_output , blocks    

if __name__ == '__main__':
    result = 'Yes'
    T = int(input('Enter the number of testcase: '))
    for i in range(T):
        n = int(input('Enter the number of cubes: '))
        blocks = list(input('Enter the numbers with space in between: '))
        blocks = [ i for i in blocks if i != ' ']
        print(blocks)
        if blocks[0] >= blocks[-1]:
            flag = blocks.pop(0)            
        else:
            flag = blocks.pop(-1)
        for k in range(len(blocks)-1):
            check_output , blocks = check(blocks)
            if check_output > flag:
                result = 'No'
                break
            elif check_output <= flag:
                flag = check_output
        print(result)

            
