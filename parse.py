import csv
import os
with open('live.csv', 'r') as f:
    reader = csv.reader(f)
    amr_csv = list(reader)

    if os.path.exists("myfile.txt"):
        os.remove("myfile.txt")
    else:
        print("Cnothing to remove")

    f1 = open("myfile.txt", "w")
    x=1
    temp_list = []
    for line in amr_csv:
        if line[1] not in temp_list:
            if (line[1]) != 'buyer':
                temp_list.append(line[1])
                print(line[1])
        # if (line[1]) != 'buyer':
        #     print(line[1])

    temp_list.sort()
    for i in temp_list:
        if x < 10:
            f1.write(str(x) + '.    ' + i + '\n')
        if x >= 10:
            f1.write(str(x) + '.   ' + i + '\n')

        x = x+1

