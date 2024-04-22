import random

class Equipment:
    def __init__(self, item_level, type, refine_level):
        self.ItemLevel = item_level
        self.Type = type
        self.RefineLevel = refine_level

class RefineCalculator:
    def RefineEquipments(self, equipments, isVIP):
        attempRefine = self.AttemptRefine
        for e in equipments:
            if e.ItemLevel < 10:
                if e.Type == "Weapon":
                    if e.ItemLevel == 1:
                        if e.RefineLevel < 7:
                            attempRefine(100, e, isVIP)
                        elif e.RefineLevel < 9:
                            attempRefine(60, e, isVIP)
                        else:
                            attempRefine(20, e, isVIP)
                    elif e.ItemLevel == 2:
                        if e.RefineLevel < 7:
                            attempRefine(100, e, isVIP)
                        elif e.RefineLevel < 9:
                            attempRefine(30, e, isVIP)
                        else:
                            attempRefine(15, e, isVIP)
                    else:
                        if e.RefineLevel < 5:
                            attempRefine(100, e, isVIP)
                        elif e.RefineLevel < 7:
                            attempRefine(40, e, isVIP)
                        else:
                            attempRefine(10, e, isVIP)
                elif e.Type == "Armor":
                    if e.RefineLevel < 5:
                        attempRefine(100, e, isVIP)
                    else:
                        chance = 10 - e.RefineLevel
                        attempRefine(chance, e, isVIP)
    
    def AttemptRefine(self, chance, equipment, isVIP):
        tmpNumber = random.randint(0, 100)
        if tmpNumber < chance:
            equipment.ItemLevel += 1
        else:
            if isVIP:
                equipment.ItemLevel -= 1
            else:
                equipment.ItemLevel = 0