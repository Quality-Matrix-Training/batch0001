# importing the csv files and reading the data
import csv

with open('asnmt.csv', newline='\n') as csvfile:
    datareader = csv.reader(csvfile, delimiter='\t')
    l_stu = []
    
    for row in datareader:
        l_stu.append(row)
    
# print(l_stu)

# importing the faculty csv file and reading it
import csv
with open('faculty.csv', mode='r', newline="\n") as csvfile1:
    datareader1 = csv.reader(csvfile1, delimiter='\t')
    fac = []
    for row in datareader1:
        fac.append(row)
        
# print(fac)

# creating a dictionary for faculty
fac_dict = {}

for i in range(0, len(fac)):
    fac_dict[fac[i][0]] = fac[i][1]
    
# print(fac_dict)

# arranging the student and their marks into a dictionary
stu_marks = {}
for i in range(0, len(l_stu)):
    x = l_stu[i][0]
    
    if x not in stu_marks:
        stu_marks[x] = [l_stu[i][1], int(l_stu[i][2])]
    
    else:
        stu_marks[x].append(l_stu[i][1])
        stu_marks[x].append(int(l_stu[i][2]))

# print(stu_marks)

# calculating the total marks of different students and arranging in a dictionary
tot_marks = {}

for i in stu_marks:
    e = stu_marks[i]
    s = 0
    
    for j in range(1, len(e), 2):
        s += e[j]
        
    tot_marks[i] = s
    
    
# print(tot_marks)

# creating dictionary for different subjects marks ignoring failures
sub_marks = {}

for i in stu_marks:
    g = stu_marks[i]
    
    for j in range(0, len(g), 2):
        
        if g[j+1] >= 40: # ignoring failures
            
            if g[j] not in sub_marks:
                sub_marks[g[j]] = [g[j+1]]
            
            else:
                sub_marks[g[j]].append(g[j+1])
    
# print(sub_marks)

# creating dictionary based on the marks greater than 90
marks_90 = {}

for i in stu_marks:
    h = stu_marks[i]
    
    for j in range(0, len(h), 2):
        if h[j+1] > 90: # checking greater than 90

            if h[j] not in marks_90:
                marks_90[h[j]] = [h[j+1]]
            
            else:
                marks_90[h[j]].append(h[j+1])
                
# print(marks_90)

# finding the pass percentage of each subject
per_pass = {}

for i in stu_marks:
    l = stu_marks[i]
    
    for j in range(0, len(l), 2):
        if l[j+1] > 40:
            
            if l[j] not in per_pass:
                per_pass[l[j]] = [l[j+1]]
            
            else:
                per_pass[l[j]].append(l[j+1])
                
# print(per_pass)

# finding the failures of each subject
fail_per = {}

for i in stu_marks:
    m = stu_marks[i]
    
    for j in range(0, len(m), 2):
        if m[j+1] <= 40:
            
            if m[j] not in fail_per:
                fail_per[m[j]] = [m[j+1]]
            
            else:
                fail_per[m[j]].append(m[j+1])
                
# print(fail_per)

# 1.faculty with highest student count who got more than 90% marks
def fac_with_high_per_student():
    
    sub_90 = max(marks_90.items(), key=lambda x:len(x[1]))
    print("Faculty with highest student count who got more than 90% is:")
    print(fac_dict[sub_90[0]],",", sub_90[0])


# 2.highest pass percentage of subject and printing the faculty name
def faculty_with_high_pass_percentage():
    
    high_pp = max(per_pass.items(), key=lambda x:len(x[1]))
    print("The faculty with highest pass percentage is:")
    print(fac_dict[high_pp[0]],",", high_pp[0])
    
    
# 3.finding the faculty with least pass percentage
def faculty_with_less_pass_percentage():
    
    least_pass = max(fail_per.items(), key=lambda x:len(x[1]))
    print("The faculty with least pass percentage is:")
    print(fac_dict[least_pass[0]],",", least_pass[0])
    
    
# 4.student with highest marks total
def student_with_highest_total():
    
    max_marks = max(tot_marks.items(), key=lambda x:x[1])
    print(f"Student with maximum total marks is {max_marks}")
    
    
# 5.student with best marks in mathematics
def student_best_in_math():
    
    math_marks = {}

    for i in stu_marks:
        math_marks[i] = stu_marks[i][1]

    max_math = max(math_marks.items(), key=lambda x:x[1])
    print(f"Student with best marks in mathematics is {max_math}")
    
    
# 6.finding the average of each subject
def avg_marks_of_each_subject():
    
    avg_marks = {}

    for i in sub_marks:
        avg_marks[i] = round((sum(sub_marks[i])/len(sub_marks[i])), 2)

    print("The Average marks of each subjects is:")
    print(avg_marks)
    
    
# 7.student with lowest marks total
def student_with_lowest_total():
    
    min_marks = min(tot_marks.items(), key=lambda x:x[1])
    print(f"Student with minimum total marks is {min_marks}")
    
    
    
# 1.faculty with highest student count who got more than 90% marks
fac_with_high_per_student()

# 2.highest pass percentage of subject and printing the faculty name
faculty_with_high_pass_percentage()

# 3.finding the faculty with least pass percentage
faculty_with_less_pass_percentage()

# 4.student with highest marks total
student_with_highest_total()

# 5.student with best marks in mathematics
student_best_in_math()

# 6.finding the average of each subject
avg_marks_of_each_subject()

# 7.student with lowest marks total
student_with_lowest_total()