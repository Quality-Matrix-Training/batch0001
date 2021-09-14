def faculty_with_morethan_ninety_percent():
    import csv

    l = []
    l1 = []
    d = {}

    l2 = []
    l3 = []
    d1 = {}

    f = open("faculty.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')

    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        d[l1[i][0]] = l1[i][1]

    # print("\n",d)

    f1 = open("asnmt.csv", mode="r", newline='\n')

    datareader1 = csv.reader(f1, delimiter=',')

    for row in datareader1:
        l2.append(row)

    # print(l2)

    for i in range(0, len(l2)):
        l3.append(l2[i][0].split('\t'))

    # print(l3)

    for i in range(0, len(l3)):
        t1 = l3[i]
        if int(l3[i][2]) > 90:
            if l3[i][1] not in d1:
                d1[l3[i][1]] = [int(l3[i][2])]
            else:
                d1[l3[i][1]].append(int(l3[i][2]))

    # print(d1)

    w1 = d1.items()
    w2 = max(w1, key=lambda x: len(x[1]))

    # print(w2[0])
    print("The faculty with highest student count who got more than 90% is: ", d[w2[0]])

    f.close()
    f1.close()


def faculty_with_high_pass_percentage():
    import csv

    l = []
    l1 = []
    d = {}

    l2 = []
    l3 = []
    d1 = {}

    f = open("faculty.csv", mode="r", newline='\n')
    f1 = open("asnmt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')
    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        d[l1[i][0]] = l1[i][1]

    # print(d)

    datareader1 = csv.reader(f1, delimiter='\n')
    for row in datareader1:
        l2.append(row)

    # print(l2)

    for i in range(0, len(l2)):
        l3.append(l2[i][0].split('\t'))
    # print(l3)

    for i in range(0, len(l3)):
        m1 = l3[i]
        if int(l3[i][2]) > 40:
            if l3[i][1] not in d1:
                d1[l3[i][1]] = [int(l3[i][2])]
            else:
                d1[l3[i][1]].append(int(l3[i][2]))

    # print(d1)

    m2 = d1.items()
    m3 = max(m2, key=lambda x: len(x[1]))

    print("The faculty with highest pass percentage is:", end=' ')
    print(d[m3[0]])

    f.close()
    f1.close()


def facuilty_with_least_pass_percentage():
    import csv

    l = []
    l1 = []
    d = {}

    l2 = []
    l3 = []
    d1 = {}

    f = open("faculty.csv", mode="r", newline='\n')
    f1 = open("asnmt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')
    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        d[l1[i][0]] = l1[i][1]

    # print(d)

    datareader1 = csv.reader(f1, delimiter='\n')
    for row in datareader1:
        l2.append(row)

    # print(l2)

    for i in range(0, len(l2)):
        l3.append(l2[i][0].split('\t'))
    # print(l3)

    for i in range(0, len(l3)):
        m1 = l3[i]
        if int(l3[i][2]) <= 40:
            if l3[i][1] not in d1:
                d1[l3[i][1]] = [int(l3[i][2])]
            else:
                d1[l3[i][1]].append(int(l3[i][2]))

    # print(d1)
    m2 = d1.items()
    m3 = max(m2, key=lambda x: len(x[1]))

    print("The faculty with least pass percentage is:", end=' ')
    print(d[m3[0]])

    f.close()
    f1.close()


def top_and_least_totaled_student():
    import csv

    l = []
    l1 = []
    d = {}
    d1 = {}

    f = open("asnmt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')

    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        s = l1[i][0]
        if s not in d:
            d[s] = [l1[i][1], int(l1[i][2])]
        else:
            d[s].append(l1[i][1])
            d[s].append(int(l1[i][2]))

    # print(d)
    sum1 = 0

    for i in d:
        e = d[i]
        for j in range(1, len(e), 2):
            sum1 = sum1 + int(e[j])
        d1[i] = sum1
        sum1 = 0

    # print(d1)

    n = d1.items()
    n1 = sorted(n, key=lambda x: x[1], reverse=True)

    print("The top student with max total is: ")
    print(n1[0][0])

    print("\nThe student with least total is: ")
    print(n1[len(n1) - 1][0])

    f.close()


def best_student_in_mathematics():
    import csv

    l = []
    l1 = []

    d = {}

    f = open("asnmt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')

    # column = next(datareader)
    # l.append(column)

    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        if l1[i][0] not in d:
            d[l1[i][0]] = [l1[i][1], int(l1[i][2])]
        else:
            d[l1[i][0]].append(l1[i][1])
            d[l1[i][0]].append(int(l1[i][2]))

    # print(d)

    q = list(d.items())
    # print(q)

    print("The best student(s) in Mathematics is:")
    q1 = sorted(q, key=lambda x: x[1][1], reverse=True)
    # print(q1)

    maxi = q1[0][1][1]
    for i in range(1, len(q1)):
        if maxi == q1[i][1][1]:
            print(q1[i][0])

    print(q1[0][0])

    f.close()


def average_mark_for_each_subject():
    import csv

    l = []
    l1 = []
    d = {}
    d1 = {}

    f = open("asnmt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter=',')

    # column = next(datareader)
    # l.append(column)

    for row in datareader:
        l.append(row)

    # print(l)

    for i in range(0, len(l)):
        l1.append(l[i][0].split('\t'))

    # print(l1)

    for i in range(0, len(l1)):
        g = l1[i]

        if int(g[2]) >= 40:
            if g[1] not in d:
                d[g[1]] = [int(g[2])]
            else:
                d[g[1]].append(int(g[2]))

    # print(d)
    x1 = list(d.items())

    # print(x1)
    print("The average mark for each subject after ignoring the failures is: ")

    for i in range(0, len(x1)):
        if x1[i][0] not in d1:
            d1[x1[i][0]] = round((sum(x1[i][1]) / len(x1[i][1])), 3)

    print(d1)

    f.close()

# uncomment each one of function calls to invoke their definitions.

# faculty_with_morethan_ninety_percent()

# faculty_with_high_pass_percentage()

# facuilty_with_least_pass_percentage()

# top_and_least_totaled_student()

# best_student_in_mathematics()

# average_mark_for_each_subject()
