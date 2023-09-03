if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    lowest_grade = min([ i[:][1] for i in records]) #find the lowest grade
    new_records = filter(lambda a :  a[:][1] != lowest_grade , records) #remove the lowest grade from list
    second_lowest_grade = min([ i[:][1] for i in new_records]) #find the second lowest frade from the new list
    s = sorted([i[:][0] for i in records if i[:][1] == second_lowest_grade]) #find the name correspond to the grade and sort the names
    for i in range(len(s)):
        print(s[i])