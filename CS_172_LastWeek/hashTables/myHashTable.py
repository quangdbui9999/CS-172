
from myObject import MyObject

# Create an empty list for our hash table
hashTable = []

# Each element of hashTable is another list
for count in range(0, 95):
    hashTable.append([])


# Add items to the hash table. Each item is a tuple of the form: (MyObject, integer)
# This hash table uses MyObject as the key and an integer to state
# what place in the input sequence a character was entered
for count in range(0, 10):
    char = input('Enter a single character: ')
    key = MyObject(char)
    index = hash(key)
    hashTable[index].append((key, str(count + 1)))

# iterate the hashtable, find the locations used and print their values
# remember that an element in the table is a tuple
for item in hashTable:
    if len(item) != 0:
        key = item[0][0].getValue()
        when = item[0][1]
        print(key, 'was entered', when)

# the following line is just so we can visualize the hash table
print()
for item in hashTable:
    print(item)