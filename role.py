from character import Role
from rune_keystone import Lethal_Tempo

character1 = Role('yasuo',
                  750,
                  75,
                  30, 27,
                  Lethal_Tempo)

Enemy = Role('nasher',
             200,
             35,
             10, 7,
             None)

test_item_list1 = ['Plated_Steelcaps','Mercurys_Treads','B_F_Sword',
            'Hearthbound_Axe','Aegis_of_the_Legion',
            'Randuin_Omen','Abyssal_Mask',
            'Winter_Approach','Force_of_Nature','Warmog_Armor']
test_item_list2 = []

# test items
print("character's attributes affect by items:\n")
character1.apply_item_to_role(character1, test_item_list2)
print("character's original max health: "+str(character1.max_health))
print("character's original damage number: "+str(character1.current_damage_number))
print("character's original armor: "+str(character1.current_armor))
print("character's original maical resistance: "+str(character1.current_magic_resistance)+'\n')
print('After equipping items:\n')
character1.apply_item_to_role(character1, test_item_list1)
print("character's max health changes to: "+str(character1.max_health))
print("character's damage number changes to: "+str(character1.current_damage_number))
print("character's armor changes to: "+str(character1.current_armor))
print("character's maical resistance changes to "+str(character1.current_magic_resistance))
print('###########################################################')
#test rune keystone
print("character's attributs affect by rune keystone: \n")
#reset character's damage number
character1.current_damage_number = 75
print("character's original damage number: "+ str(character1.current_damage_number)+'\n')
print('After equipping rune keystone:\n')
character1.apply_rune_keystone_to_role(character1, 'Lethal Tempo')
print("character's damage number changes to: "+ str(character1.current_damage_number))
