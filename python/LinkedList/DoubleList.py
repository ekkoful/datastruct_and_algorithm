#! /usr/bin/python3
# coding:utf-8

class ListNode():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleList():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def get_len(self):
        count = 0
        current = self.__head
        while current != None:
            count += 1
            current = current.next
        return count

    def get_items(self):
        current = self.__head
        list_item = []
        while current != None:
            list_item.append(current.data)
            current = current.next
        return list_item

    def insert_first(self, value):
        node = ListNode(value)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def insert_last(self, value):
        node = ListNode(value)
        if self.is_empty():
            self.__head = node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            node.next = None
        
    def insert(self, index, value):
        if index < 0 or index > self.get_len():
            return False
        elif index == 0:
            self.insert_first(value)
        else:
            node = ListNode(value)
            count = 1
            current = self.__head
            while count < index:
                current = current.next
                count += 1
            node.next = current.next
            current.next.prev = node
            node.prev = current
            current.next = node
            return True

    def search_by_value(self, value):
        if self.is_empty():
            return False
        else:
            current = self.__head
            while current.next:
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

    def delete_by_index(self, index):
        if self.is_empty():
            return False
        if index < 0 or index > self.get_len():
            return False
        elif index == 0:
            current = self.__head
            current.next.prev = None
            self.__head = current.next
        else:
            count = 1
            current = self.__head
            while count < index:
                current = current.next
                count += 1
            current.next = current.next.next
            current.next.prev = current
            return True 

    def delete_by_value(self, value):
        if self.is_empty():
            return False
        current = self.__head
        if current.data == value:
            current.next.prev = None
            self.__head = current.next
        while current.next:
            if current.next.data == value:
                if current.next.next:
                    current.next = current.next.next
                    current.next.prev = current
                else:
                    current.next = None
            else:
                current = current.next
        return True

if __name__ == '__main__':
    doublelist = DoubleList()
    print(doublelist.is_empty())
    print(doublelist.get_len())
    print(doublelist.get_items())
    print(doublelist.insert_first(1))
    print(doublelist.get_items())
    print(doublelist.insert_last(2))
    print(doublelist.get_items())
    print(doublelist.insert(1,2))
    print(doublelist.get_items())
    print(doublelist.search_by_index(0))
    print(doublelist.search_by_value(2))
    print(doublelist.insert(2, 5))
    print(doublelist.get_items())
    print(doublelist.delete_by_index(1))
    print(doublelist.get_items())
    print(doublelist.delete_by_value(5))
    print(doublelist.get_items())
            


