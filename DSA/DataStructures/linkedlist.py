class Node:
    def __init__(self,val,next= None):
        self.val = val
        self.next=next
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.cur = head

    def addItem(self, val, next = None):
        node = Node(val,next)
        if(self.head == None):
            self.head = node
            self.cur = node
        else:
            self.cur.next = node
            self.cur = node

    def display(self):
        if(self.head == None):
            return
        itr = self.head
        while(True):
            print(itr.val, end=" ")
            if(itr.next == None):
                return
            itr = itr.next


l1 = Node(10)
l1.next = Node(11)
l1.next = Node(17)

l2 = Node(13)
l2.next = Node(14)
l2.next = Node(15)

class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
    
        i1 = list1
        i2 = list2
        i3 = i1
        while(True):
            if(i1.next.next == None and  i2.next.next == None):
                break
            else:
                if(i1.val<=i2.val):
                    if(i1.next!=None):
                        if(i1.next.val>=i2.val):
                            y = i2
                            while(True):
                                if(y.val<=i1.next.val):
                                    y = y.next
                                else:
                                    break
                            x = i1.next
                            i1.next = i2
                            i1.next.next = y
                        else:
                            i1 = i1.next
                            i2 = i2.next
                    else:
                        i1.next = i2                    
        return i3



sol = Solution().mergeTwoLists(l1, l2)




while(True):
    print(sol.val, end=" ")
    if(sol.next == None):
        break
    sol = sol.next







                


            
        






                









