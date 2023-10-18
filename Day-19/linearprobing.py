'''Collision:
1) Separate Chaining (Open Hashing)
2) Open Address Chaining'''
'''def hash_function(key, size):
  return key % size

def linear_probing(table, key, size):
  index = hash_function(key, size)
  i = 0
  while table[index] is not None:
    index = (index + 1) % size
    i += 1
  if i == size:
    return None
  table[index] = key
  return index

def main():
  table = [None] * 10
  keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for key in keys:
    linear_probing(table, key, 10)
  for i in range(10):
    print(table[i])

if __name__ == "__main__":
  main()'''
def hash_function(value):
    return value % 10
def get_next_available_index(hash_table, current_index):
        for i in range(current_index, len(hash_table)):
            if hash_table[i] == 0:
                return i
            elif i == len(hash_table) - 1:
                i = 0
def main():
    searchkeys = [12,32,45,34,42,65,78,90,112]
    n = 10
    hash_table = [0 for i in range(n)]        
    for value in searchkeys:
        hash_value = hash_function(value)
        if hash_table[hash_value] == 0:
            hash_table[hash_value] = value
        else:
            next_index = get_next_available_index(hash_table, hash_value)
            hash_table[next_index] = value      
    print(hash_table)
main()
