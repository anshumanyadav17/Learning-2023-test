class Node:
    def __init__(self,data=None,next=None):

        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print1(self):

        if self.head is None:
            print('linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'->'
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self,data):
        if(self.head is None):
            node = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)
        

    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(4)
    ll.insert_at_begining(10)
    ll.insert_at_begining('a')
    ll.insert_at_end(42)
    ll.print1()