class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_every_second_with_lowercase(self):
        count = 0
        current = self.head
        prev = None
        index = 0
        while current:
            if index % 2 == 1 and current.data[0].islower():
                prev.next = current.next
                count += 1
            else:
                prev = current
            current = current.next
            index += 1
        return count

    def move_element(self):
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return
        first = self.head
        second = self.head.next
        current = self.head.next.next
        prev = self.head.next

        while current:
            if len(current.data) > len(first.data) + len(second.data):
                move_node = current
                if prev.next:
                    prev.next = current.next
                move_node.next = self.head
                self.head = move_node
                return
            prev = current
            current = current.next

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


def main():
    n = int(input("Podaj liczbę elementów listy: "))
    linked_list = LinkedList()
    for _ in range(n):
        element = input("Podaj napis: ")
        linked_list.append(element)

    print("Lista przed usunięciem elementów:", linked_list.to_list())
    removed_count = linked_list.delete_every_second_with_lowercase()
    print("Liczba usuniętych elementów:", removed_count)
    print("Lista po usunięciu elementów:", linked_list.to_list())

    linked_list.move_element()
    print("Lista po przeniesieniu elementu:", linked_list.to_list())


if __name__ == "__main__":
    main()
