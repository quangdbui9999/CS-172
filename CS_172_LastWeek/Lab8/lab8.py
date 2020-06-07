
from birthday import Birthday

if __name__ == "__main__":

    fileName = "xid-85887447_1.txt"
    lines = []
    newList = []
    with open(fileName) as f:
        lines = f.readlines()

    for i in lines:
        i = i.strip("\n")
        newList.append(i)
    print(newList)

    day, month, year = 0, 0, 0
    dayList = []
    monthList = []
    yearList = []
    for i in newList:
        i1, i2, i3 = i.split("/")
        dayList.append(i2)
        monthList.append(i1)
        yearList.append(i3)

    hashtable = []
    for i in range(12):
        hashtable.append([])

    dem = 0
    for count in range(0, 100):
        key = Birthday(int(dayList[count]), int(monthList[count]), int(yearList[count]))
        index = hash(key)
        hashtable[index].append((key, str(count + 1)))

    for item in hashtable:
        if len(item) != 0:
            key = item[0][0].getValue()
            when = item[0][1]
            #print(key, 'was entered', when)
print()
for item in hashtable:
    key = item[0][0].getValue()
    print(f"Hash location {key} has {len(item)} elements in it")
