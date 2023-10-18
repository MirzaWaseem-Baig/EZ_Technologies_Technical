n = int(input())
HashTable = [[] for _ in range(n)]
def insert(Hash, keyvalue, value):
    Hashnew = keyvalue % len(Hash)
    Hash[Hashnew].append(value)
for i in range(n):
    insert(HashTable, int(input()), input())
for i in range(len(HashTable)): 
        print(i, end = " ") 
          
        for j in HashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
              
        print() 
  
