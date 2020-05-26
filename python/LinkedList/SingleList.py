#!/user/bin/python3

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SingleList(object):
    
    def __init__(self, node=None):
        self.__head = node
    
    def is_empty(self):
        return self.__head == None
    
    def insert_first(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node
    
    def insert_last(self, value):
        node = Node(value)
        current = self.__head
        if self.__head == None:
            self.__head = node
        else:
            while current.next:
                current = current.next
            current.next = node
    
    def insert(self, index, value):
        if index < 0:
            self.add(value)
        elif index > self.get_len():
            self.append(value)
        else:
            current = self.__head
            count = 1
            while count < index:
                current = current.next
                count += 1

            node = Node(value)
            node.next = current.next
            current.next = node

    def get_len(self):
        if self.is_empty():
            return False
        else:
            count = 0
            current = self.__head
            while current != None:
                current = current.next
                count += 1
            return count

    def delete_byvalue(self, value):
        if self.is_empty():
            return False
        else:
            current = self.__head
            while current.next != None:
                if current.next.data == value:
                    current.next = current.next.next
                    return True
                else:
                    current = current.next
            return True
    
    def delete_byindex(self, index):
        if self.is_empty():
            return False
        elif index < 0 or index > self.get_len():
            return False
        elif index == 0:
            current = self.__head
            self.__head = current.next
        else:
            current = self.__head
            count = 1
            while count < index:
                current = current.next
                count += 1
            current.next = current.next.next
            return True
    
    def search_by_value(self, value):
        if self.is_empty():
            return False
        current = self.__head
        while current.next != None:
            if current.next.data == value:
                return value
            current = current.next
        return False

    def search_by_index(self, index):
        if self.is_empty():
            return False
        if index < 0 or index > self.get_len():
            return False
        elif index == 0:
            return self.__head.data
        else:
            count = 1
            current = self.__head
            while count < index:
                current = current.next
                count += 1
            return current.next.data

    def get_items(self):
        if self.is_empty():
            return False
        new_list = []
        current = self.__head
        while current != None:
            new_list.append(current.data)
            current = current.next
        return new_list

if __name__ == '__main__':
    singlelist = SingleList()
    print(singlelist.is_empty())
    print(singlelist.get_len())
    singlelist.insert_first(1)
    print(singlelist.is_empty())
    print(singlelist.get_len())
    singlelist.insert_last(2)
    singlelist.insert_last(3)
    singlelist.insert_last(5)
    singlelist.insert(2, 10)
    print(singlelist.get_len())
    print(singlelist.get_items())
    print(singlelist.search_by_value(2))
    print(singlelist.search_by_index(2))
    singlelist.delete_byindex(0)
    print(singlelist.get_len())
    print(singlelist.get_items())


        

