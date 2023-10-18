class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
        self.temp = None
    def create_list(self):
        for i in range(10):
            new_node = Node(i)
            if self.start is None:
                self.start = new_node
                self.temp = self.start
            else:
                self.temp.next = new_node
                self.temp = self.temp.next
        return self.start
    def print_list(self):
        self.temp = start
        while self.temp:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print()
    '''def find_median(self):
        self.temp = self.start'''
    def reverse_list(self):
        self.temp = self.start
        arr = []
        while self.temp is not None:
            arr.append(self.temp.data)
            self.temp = self.temp.next
        arr = arr[::-1]
        self.temp = self.start
        while self.temp is not None:
            self.temp.data = arr[i]
            i+=1
            self.temp = self.temp.next
object_ = LinkedList()
start = object_.create_list()
object_.print_list()
object_.reverse_list()
object_.print_list()

