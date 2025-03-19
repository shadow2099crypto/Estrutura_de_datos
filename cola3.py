class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     nombre: {self.get_customer()}")
        print(f"     edad: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer

class Node:
    def __init__(self, order):
        self.order = order
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, order):
        new_node = Node(order)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            current_node.order.print()
            current_node = current_node.next

order1 = Order(20, "Carlos")
order2 = Order(10, "Ana")
order3 = Order(15, "Fax")
order4 = Order(19, "Alexis")

lista_pedidos = LinkedList()
lista_pedidos.append(order1)
lista_pedidos.append(order2)
lista_pedidos.append(order3)
lista_pedidos.append(order4)

lista_pedidos.print_list()
