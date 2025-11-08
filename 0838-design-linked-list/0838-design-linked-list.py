class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.val
            temp = temp.next
            count += 1
        return -1   # index out of bounds


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if not temp:
            return  # index out of bounds
        new_node = Node(val)
        new_node.next = temp.next
        temp.next = new_node



    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if not curr or not curr.next:
            return  # index out of bounds
        temp = curr.next
        curr.next = temp.next
        del temp

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)