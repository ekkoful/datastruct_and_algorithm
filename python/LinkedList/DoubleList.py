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
            while current:
                current = current.next
            current.next = node
            node.prev = current
            node.next = None
        
    def insert(self, index, value):
        if index < 0 or index > self.get_len():
            return False
        else:
            node = ListNode(value)
            count = 1
            current = self.__head
            while count < index:
                current = current.next

            node.next = current.next
            current.next.prev = node
            node.prev = current
            current.next = node

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
            return self.__head
        else:
            count = 1
            current = self.__head
            while count < index:
                current = current.next
                count += 1
            return current.next.data

    def delete_by_index(self, index):
        pass

    def delete_by_value(self, value):
        pass


            


