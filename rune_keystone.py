"""
Lethal Tempo:
After 3 sperate attacks (same or different enemies, the attack speed increase by 50%),
then continue the increasment until stop attacking.
"""
class Lethal_Tempo:
    def __init__(self, attack_speed):
        self.attack_speed = attack_speed
        self.active_Lethal_Tempo = False
        self.attack_counter = 0 # the times the character attacks the enemies.
        self.check_vaildty = False
    
    def Lethal_Tempo_attack(self):
        self.attack_counter += 1

        if self.attack_counter >= 3:
            self.active_Lethal_Tempo = True
            self.attack_speed *= 1.5
    
    def Lethal_Tempo_end_attack(self):
        self.attack_counter = 0
        if self.active_Lethal_Tempo:
            self.active_Lethal_Tempo = False
            self.attack_speed /= 1.5

"""
Conqueror:
After 12 sperate attacks or skill attacks(same or different enemies), the physical attack damage increasing by 48,
and healing the character itself by 12% of the damage that enemies takes (which is omnivamp) 
"""
class Conqueror:
    def __init__(self, 
                 attack_physical_damage,
                 attack_magical_damage, 
                 omnivamp):
        self.attack_physical_damage = attack_physical_damage
        self.attack_magical_damage = attack_magical_damage
        self.omnivamp = omnivamp
        self.active_conqueror = False
        self.attack_counter = 0
        self.check_vaildty = False
    
    
    def Conqueror_attack(self):
        self.attack_counter += 1

        if self.attack_counter <= 12:
            self.attack_physical_damage += 4
        
        if self.attack_counter > 12:
            self.active_conqueror = True
            self.omnivamp += (self.attack_magical_damage, self.attack_physical_damage) * 0.12
    
    def Conqueror_end_attack(self):
        self.attack_counter = 0

        if self.active_conqueror:
            self.active_conqueror = False
            self.omnivamp = (self.attack_magical_damage, self.attack_physical_damage) * 0.12
            self.attack_physical_damage -= 48
            

"""
Dark Harvest allows a champion to gain stacks upon damaging an enemy champion below a certain health threshold. 
These stacks can be consumed to deal bonus damage on the next attack or ability
"""
class Dark_Harvest:
    def __init__(self, dark_harvest_num = 0):
        self.dark_harvest_num = dark_harvest_num
        self.check_vaildty = False
    
    
    def damage_enemy(self, 
                     enemy_health, 
                     current_physical_damage_number, 
                     current_magical_damage_number):
        damage = current_physical_damage_number + current_magical_damage_number
        enemy_health -= damage

        if enemy_health <= 0:
            self.dark_harvest_num += 1
        
        return enemy_health
    
    def consume_dark_harvest(self):
        if self.dark_harvest_num > 10:
            bonus_damage = self.dark_harvest_num * 2.2
            self.dark_harvest_num = 0
            return bonus_damage
        return 0

"""
Grasp of the Undying provides a champion with a stacking health bonus and a short-ranged attack that restores some health and deals bonus damage to the enemy
"""
class Grasp_of_the_Undying:
    def __init__(self, current_health, max_health, grasp_num=0):
        self.max_health = max_health
        self.current_health = current_health
        self.grasp_num = grasp_num
        self.attack_counter = 0  # Track the number of attacks
        self.bonus_damage_active = False  # Flag to track bonus damage activation
        self.check_vaildty = False

    def attack_enemy(self, enemy_health, current_magical_damage_number, current_physical_damage_number):
        bonus_damage = self.calculate_bonus_damage()
        enemy_health = self.apply_damage(enemy_health, current_magical_damage_number, current_physical_damage_number, bonus_damage)
        self.grasp_num += 1
        self.current_health = min(self.current_health, self.max_health)
        self.update_attack_counter()
        return enemy_health

    def calculate_bonus_damage(self):
        if self.attack_counter < 3:
            return 0
        else:
            self.bonus_damage_active = True
            return self.grasp_num * 5

    def apply_damage(self, enemy_health, current_magical_damage_number, current_physical_damage_number, bonus_damage):
        return enemy_health - (current_magical_damage_number + current_physical_damage_number + bonus_damage)

    def update_attack_counter(self):
        if self.bonus_damage_active:
            self.attack_counter = 0  # Reset the attack counter
            self.bonus_damage_active = False
        else:
            self.attack_counter += 1
