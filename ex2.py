#Linked Structures
class Node(object):
      """Sebuah simpul di linked list"""
      def __init__(self, data, next = None):
            self.data = data
            self.next = next
#mengunjungi setiap simpul dari depan
def kunjungi(head):
      curNode = head
      while curNode is not None :
            print(curNode.data)
            curNode = curNode.next
#menambah sebuah simpul awal
def insertAtStart (self, data):
      newNode = Node(data)
      self.size += 1

      if self.head is None :
            self.head = newNode
      else:
            newNode.nestNode = self.head
            self.head = newNode


#menghapus data
def removeData(self,data):
      currentNode = self.head

      while currentNode is not data:
            prevNode = currentNode is not data:
                  prevNode = currentNode
                  currentNode = current.nextNode

      prevNode.nextNode = currentNode.nextNode
      self.size -= 1
