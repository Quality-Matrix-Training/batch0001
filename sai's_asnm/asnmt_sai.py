# max and min marks of students

def min_and_max_totalled_students():
    import csv

    d = {}

    d1 = {}

    l = []

    f = open("assnmentt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter='\t')

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    # print(d)

    sum1 = 0

    for i in d:
        e = d[i]
        for j in range(1, len(e), 2):
            sum1 += e[j]
        d1[i] = sum1
        sum1 = 0

    # print(d1)

    e = d1.items()

    max_marks = max(e, key=lambda x: x[1])

    a = (max_marks)

    print(f"maximum marks{a}")

    min_marks = min(e, key=lambda x: x[1])

    b = min_marks

    print(f"minimum marks{b}")

    f.close()


# max marks in math

def highest_maths_marks():
    import csv

    l = []

    d = {}

    d1 = {}

    f = open("assnmentt.csv", mode="r", newline="\n")

    datareader = csv.reader(f, delimiter="\t")

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    e = list(d.items())

    for i in range(0, len(e)):
        if e[i][0] not in d1:
            d1[e[i][0]] = e[i][1][1]

    s = d1.items()

    max_math = max(s, key=lambda x: x[1])

    print(max_math)

    f.close()


# avg marks of each subject

def avg_total_in_each_sub():

    import csv

    d = {}

    l = []

    f = open("assnmentt.csv", mode="r", newline="\n")

    datareader = csv.reader(f, delimiter="\t")

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    d1 = {}
    d2 = {}

    for i in d:
        e = d[i]
        for j in range(0, len(e), 2):
            if e[j + 1] >= 40:
                if e[j] not in d1:
                    d1[e[j]] = [e[j + 1]]

                else:
                    d1[e[j]].append(e[j + 1])

    # print(d1)

    for k in d1:
        q = round((sum(d1[k]) / len(d1[k])), 2)
        d2[k] = q

    print(d2)

    f.close()


# highest student count who got more than 90

def faculty_with_morethan_90percent():
    l = []
    import csv

    f = open("fcuiltyy.csv", mode='r', newline="\n")

    datareader = csv.reader(f, delimiter="\t")

    for row in datareader:
        l.append(row)

    #print(l)

    d5 = {}

    for i in range(0, len(l)):
        if l[i][0] not in d5:
            d5[l[i][0]] = l[i][1]

    #print(d5)

    f.close()

    import csv

    d = {}

    d2 = {}

    l = []

    f = open("assnmentt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter='\t')

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    for i in d:
        e = d[i]
        for j in range(0, len(e), 2):
            if e[j + 1] >= 90:

                if e[j] not in d2:
                    d2[e[j]] = [e[j + 1]]

                else:
                    d2[e[j]].append(e[j + 1])

    q = d2.items()

    q1 = max(q, key=lambda x: len(x[1]))

    print(q1)
    print(d5[q1[0]])

    f.close()


# highest pass percentage of faculty >40

def faculty_with_more_pass_percent():
    import csv

    d = {}

    d2 = {}

    l = []

    f = open("assnmentt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter='\t')

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    l = []
    import csv

    f = open("fcuiltyy.csv", mode='r', newline="\n")

    datareader = csv.reader(f, delimiter="\t")

    for row in datareader:
        l.append(row)

    # print(l)

    d5 = {}

    for i in range(0, len(l)):
        if l[i][0] not in d5:
            d5[l[i][0]] = l[i][1]

    # print(d5)

    f.close()

    d7 = {}


    for i in d:
        e = d[i]

        for j in range(0, len(e) - 1, 2):

            if e[j + 1] > 40:

                if e[j] not in d7:
                    d7[e[j]] = [e[j + 1]]

                else:
                    d7[e[j]].append(e[j + 1])

    #print(d7)

    e1 = d7.items()

    highest_pass = max(e1, key=lambda x: len(x[1]))

    print(highest_pass)

    print(d5[highest_pass[0]])


# less pass percentage of faculty <= 40

def faculty_with_more_failures():
    l = []

    import csv

    f = open("fcuiltyy.csv", mode='r', newline="\n")

    datareader = csv.reader(f, delimiter="\t")

    for row in datareader:
        l.append(row)

    # print(l)

    d5 = {}

    for i in range(0, len(l)):
        if l[i][0] not in d5:
            d5[l[i][0]] = l[i][1]

    # print(d5)

    f.close()

    import csv

    d = {}

    d2 = {}

    l = []

    f = open("assnmentt.csv", mode="r", newline='\n')

    datareader = csv.reader(f, delimiter='\t')

    for row in datareader:
        l.append(row)

    for i in range(0, len(l)):
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1], int(l[i][2])]

        else:
            d[l[i][0]].append(l[i][1])
            d[l[i][0]].append(int(l[i][2]))

    d8 = {}

    for i in d:
        e = d[i]

        for j in range(0, len(e) - 1, 2):
            if e[j + 1] <= 40:

                if e[j] not in d8:
                    d8[e[j]] = [e[j + 1]]

                else:
                    d8[e[j]].append(e[j + 1])

    f = d8.items()

    min_pass_per = max(f, key=lambda x: len(x[1]))

    print(min_pass_per)

    a = d5[min_pass_per[0]]

    print(a)


# min_and_max_totalled_students()

# highest_maths_marks()

# avg_total_in_each_sub()

# faculty_with_morethan_90percent()

# faculty_with_more_pass_percent()

# faculty_with_more_failures()
