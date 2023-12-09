class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, data):
        new_node = Node(name, data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

rune_keystones = LinkedList()

Lethal_Tempo = {'Name': 'Lethal Tempo','current_damage_number': 25}

rune_keystones.append('Lethal Tempo', Lethal_Tempo)



    
