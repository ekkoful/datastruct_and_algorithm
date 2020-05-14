package main

import (
	"fmt"
)

//set node struct
type Node struct {
	data int
	next *Node
}

//set list struct
type LinkedList struct {
	head *Node
}

//一般的list.head 就是整个LinkedList
//Head Insert

//        -----------
//|head|->|data|next| ->
//		  -----------
//如果链表为空，则直接把data变量赋值给list.head
//如果链表非空，则把list.head的值，赋值给data.next，因为在头部插入，插入的数据就变为头部数据了
func (list *LinkedList) InsertFirst(i int) {
	data := &Node{data: i}
	if list.head != nil {
		data.next = list.head
	}
	list.head = data
	return
}

//如果链表为空，则直接把data变量赋值给list.head
//如果链表非空，则for循环找到最后一个节点，最后一个节点的next指向data
func (list *LinkedList) InsertLast(i int) {
	data := &Node{data: i}
	if list.head == nil {
		list.head = data
		return
	}
	current := list.head
	for current.next != nil {
		current = current.next
	}
	current.next = data
}

//在指定节点index前插入
//如果链表插入的节点小于等于1，使用InsertFirst
//如果链表插入的节点大于链表的长度，使用InsertLast
//golang 中的for 和 while
func (list *LinkedList) Insert(index int, i int) {
	if index <= 0 {
		list.InsertFirst(i)
	} else if index > list.GetSize() {
		list.InsertLast(i)
	} else {
		pre := list.head
		//链表下标从0开始
		//这样可以从1开始
		//count := 1
		//for count < (index - 1) {
		//	pre = pre.next
		//	count++
		//}
		count := 1
		for count < index {
			pre = pre.next
			count++
		}
		node := &Node{data: i}
		node.next = pre.next
		pre.next = node

	}
}

func (list *LinkedList) RemoveByIndex(index int) bool {
	if list.head == nil {
		return false
	}
	if index < 0 {
		return false
	} else if index == 0 {
		list.head = list.head.next
		return true
	}
	current := list.head
	count := 1
	for count < index && current.next != nil {
		current = current.next
		count++
	}
	current.next = current.next.next
	return true
}

func (list *LinkedList) RemoveByValue(data int) bool {
	if list.head == nil {
		return false
	}
	if list.head.data == data {
		list.head = list.head.next
		return true
	}
	current := list.head
	for current.next != nil {
		if current.next.data == data {
			current.next = current.next.next
			return true
		}
		current = current.next
	}
	return true
}

func (list *LinkedList) GetSize() int {
	count := 0
	current := list.head
	for current != nil {
		count += 1
		current = current.next
	}
	return count
}

func (list *LinkedList) GetItems() []int {
	var items []int
	current := list.head
	for current != nil {
		items = append(items, current.data)
		current = current.next
	}
	return items
}

func (list *LinkedList) SearchValue(i int) bool {
	if list.head == nil {
		return false
	}
	current := list.head
	for current.next != nil {
		if current.next.data == i {
			return true
		}
		current = current.next
	}
	return false
}

func (list *LinkedList) GetFirst() (int, bool) {
	if list.head == nil {
		return 0, false
	}
	return list.head.data, true
}

func (list *LinkedList) GetLast() (int, bool) {
	if list.head == nil {
		return 0, false
	}
	current := list.head
	for current.next != nil {
		current = current.next
	}
	return current.data, true
}

func main() {
	list := &LinkedList{}
	list.InsertFirst(1)
	list.InsertFirst(3)
	list.InsertFirst(5)
	list.InsertFirst(7)
	list.InsertFirst(9)
	list.InsertLast(2)
	fmt.Println(list.GetSize())
	fmt.Println(list.GetItems())
	list.Insert(1, 10)
	//list.Insert(0, 11)
	list.RemoveByIndex(4)
	fmt.Println(list.GetSize())
	fmt.Println(list.GetItems())
	list.RemoveByValue(1)
	list.RemoveByValue(2)
	fmt.Println(list.GetSize())
	fmt.Println(list.GetItems())
	fmt.Println(list.SearchValue(5))
	fmt.Println(list.GetFirst())
	fmt.Println(list.GetLast())
}
