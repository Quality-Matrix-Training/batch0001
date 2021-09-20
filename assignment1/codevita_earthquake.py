list1 = []  # actual
list2 = []  # zeroes

N = int(input("Enter the grid size:"))

for i in range(0, N):
    t = []
    for j in range(0, N):
        t.append(int(input()))

    list1.append(t)

a, b = map(int, input("Enter the epicenter co-ordinates:").split())
M = float(input("Enter the magnitude:"))

for i in range(0, N):
    t1 = []
    for j in range(0, N):
        t1.append(0)

    list2.append(t1)


def ways(row, col, Mag):
    if Mag <= 3.00:

        if row < 0 or row > (N - 1) or col < 0 or col > (N - 1):
            return

        elif list1[row][col] == 0:
            return

        elif list1[row][col] == 1:
            list2[row][col] = 2

        ways(row + 1, col + 1, Mag)
        ways(row - 1, col - 1, Mag)
        ways(row + 1, col - 1, Mag)
        ways(row - 1, col + 1, Mag)
        ways(row, col + 1, Mag)
        ways(row, col - 1, Mag)
        ways(row + 1, col, Mag)
        ways(row - 1, col, Mag)


ways(a - 1, b - 1, M)

print(list2)