rows = int(input("Give number of rows:   "))

row_list = [0, 1, 0]

print(row_list)

for n in range(1, rows+1):
    row1_list = []
    for r in range(1, len(row_list)):
        row1_list.insert(r, row_list[r-1]+row_list[r])

    row1_list.insert(0,0)
    row1_list.append(0)

    row_list = row1_list
    print(row1_list)
