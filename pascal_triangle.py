row = [1]
rowmax = int(input('rowmax = '))
while (len(row) - 1) < rowmax:
    print(str(len(row) - 1), ': ', str(row))
    rowcp = row[:]
    rowcp.append(1)
    for i in range(1,len(row)):
        rowcp[i] = row[i - 1] + row[i]
    row = rowcp[:]
print(str(len(row) - 1), ': ', str(row))
input('press Enter to exit')
