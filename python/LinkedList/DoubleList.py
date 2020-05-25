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

    
            


