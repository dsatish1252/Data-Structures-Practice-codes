class Node:

    def __init__(self):
        self.__data = 0
        self.__next = None

    def set_data(self, d):
        self.__data = d

    def set_next(self, n):
        self.__next = n

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next


class SingleLinkedList:

    def __init__(self):
        self.__head = None

    def add_at_head(self, ele):
        p = Node()
        p.set_data(ele)
        if self.__head is None:
            self.__head = p
        else:
            p.set_next(self.__head)
            self.__head = p
        print("Node added @ Head")

    def list_nodes(self):
        if self.__head is None:
            print("Empty List")
        else:
            q = self.__head
            while q is not None:
                print(q.get_data(), end="-->")
                q = q.get_next()

    def add_at_tail(self, ele):
        if self.__head is None:
            self.add_at_head(ele)
        else:
            p = Node()
            p.set_data(x)
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p)

    def count_nodes(self):
        c = 0
        q = self.__head
        while q is not None:
            c += 1
            q = q.get_next()
        return c

    def search_node(self, d):
        q = self.__head
        while q is not None:
            if q.get_data() == d:
                print("element found")
                return
        print("element not found")

    def add_after_position(self, ele, pos):
        p = Node()
        p.set_data(ele)
        i = 1
        q = self.__head
        if self.count_nodes() >= pos:
            while i < pos:
                q = q.get_next()
                i += 1
            p.set_next(q.get_next())
            q.set_next(p)
            print("node added after position")

    def add_at_position(self, val, pos):
        p = Node()
        p.set_data(val)
        q = self.__head
        if self.count_nodes() >= pos:
            i = 1
            while i < pos - 1:
                q = q.get_next()
                i += 1
            p.set_next((q.get_next()))
            q.set_next(p)
            print("node added at position")




sll = SingleLinkedList()
while True:
    print("\nMenu")
    print("1. Add @ Head")
    print("2. add after position")
    print("3. Add @ tail")
    print("4. Count Nodes")
    print("5. search element")
    print("6. list nodes")
    print("7. add @ position")
    print("8. Exit")
    print("Enter your option :")
    option = int(input())
    if option == 1:
        print("Enter data")
        data = int(input())
        sll.add_at_head(data)
    elif option == 2:
        print("enter data")
        x = int(input())
        print("enter position")
        po = int(input())
        sll.add_after_position(x, po)
    elif option == 3:
        print("Enter data")
        data = int(input())
        sll.add_at_tail(data)
    elif option == 4:
        print("count = ", sll.count_nodes())
    elif option == 5:
        print("enter element to search")
        x = int(input())
        sll.search_node(x)
    elif option == 6:
        sll.list_nodes()
    elif option == 7:
        print("enter element")
        data = int(input())
        print("enter position")
        p = int(input())
        sll.add_at_position(data, p)
    else:
        break
