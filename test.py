from role import character1, Enemy
from rune_keystone import rune_keystones

test_item_list2 = []

# test items
print("character's attributes affect by items test:")

test_item_list1 = ['Plated_Steelcaps','Mercurys_Treads','B_F_Sword',
            'Hearthbound_Axe','Aegis_of_the_Legion',
            'Randuin_Omen','Abyssal_Mask',
            'Winter_Approach','Force_of_Nature','Warmog_Armor']
character1.apply_item_to_role(character1, test_item_list1)


if character1.max_health != 3050 or character1.current_damage_number != 160 or character1.current_armor != 210 or character1.current_magic_resistance != 212:
    print("items test false")
else:
    print("items test pass")

print("\n")

print('######################################################################################################\n')
#test rune keystone
print("character's attributs affect by rune keystone test:")
#reset character's damage number
character1.current_damage_number = 75
character1.apply_rune_keystone_to_role(character1, 'Lethal Tempo')
if character1.current_damage_number == 100:
    print("rune keystone test pass")
else:
    print("rune keystone test fail")
print('\n')

print('rune keystone existence test:')
current = rune_keystones.head
length = 0
while current:
    length += 1
    current = current.next

if length != 1:
    print('rune keystone existence test fail')
else:
    print('rune keystone existence test pass')
