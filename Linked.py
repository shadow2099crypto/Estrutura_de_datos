class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Elemento no encontrado.")
            return

        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    lista = MyLinkedList()

    lista.insert(10)
    lista.insert(20)
    lista.insert(30)
    lista.display()  

    print("¿Existe 20?:", lista.search(20))  
    print("¿Existe 40?:", lista.search(40))  

    lista.delete(20)
    lista.display()  
