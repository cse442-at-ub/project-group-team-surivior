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
ITEMS = LinkedList()

###############################################################shoes###################################################################################################
Plated_Steelcaps = {'current_armor': 20,'current_moving_speed': 45}
Mercurys_Treads = {'current_magic_resistance': 25, 'current_moving_speed': 45}

ITEMS.append('Plated_Steelcaps', Plated_Steelcaps)
ITEMS.append('Mercurys_Treads', Mercurys_Treads)

###########################################################Legendary items#############################################################################################
B_F_Sword = {'current_damage_number': 55}
Hearthbound_Axe = {'current_damage_number': 30, 'current_moving_speed': 0.07}
Aegis_of_the_Legion = {'current_magic_resistance': 60, 'current_armor': 60}
Randuin_Omen = {'max_health': 300, 'current_armor': 60}
Abyssal_Mask = {'max_health': 300, 'current_magic_resistance': 60}
Winter_Approach = {'current_armor': 40, 'max_health': 350, 'current_moving_speed': 0.05}
Force_of_Nature = {'current_magic_resistance': 40, 'max_health': 350, 'current_moving_speed': 0.05}
Warmog_Armor = {'max_health': 1000}

ITEMS.append('Runaans_Hurricane', B_F_Sword)
ITEMS.append('Runaans_Hurricane', Hearthbound_Axe)
ITEMS.append('Runaans_Hurricane', Aegis_of_the_Legion)
ITEMS.append('Force_of_Nature', Randuin_Omen)
ITEMS.append('Force_of_Nature', Abyssal_Mask)
ITEMS.append('Force_of_Nature', Winter_Approach)
ITEMS.append('Force_of_Nature', Force_of_Nature)
ITEMS.append('Steraks_Gage', Warmog_Armor)
