import random

class Equipment:
    def __init__(self, item_level, type, refine_level):
        self.ItemLevel = item_level
        self.Type = type
        self.RefineLevel = refine_level

class RefineCalculator:
    def IsUserVIP(self, equipments, isVIP):
        if isVIP:
            equipments.ItemLevel -= 1
        else:
            equipments.ItemLevel = 0

    def RefineWeapon(self, equipments, upgradeRate, isVIP):
            if equipments.ItemLevel == 1:
                if equipments.RefineLevel < 7:
                    equipments.ItemLevel += 1
                elif equipments.RefineLevel < 9:
                    if upgradeRate < 60:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
                else:
                    if upgradeRate < 20:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
            elif equipments.ItemLevel == 2:
                if equipments.RefineLevel < 7:
                    equipments.ItemLevel += 1
                elif equipments.RefineLevel < 9:
                    if upgradeRate < 30:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
                else:
                    if upgradeRate < 15:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
            else:
                if equipments.RefineLevel < 5:
                    equipments.ItemLevel += 1
                elif equipments.RefineLevel < 7:
                    if upgradeRate < 40:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
                else:
                    if upgradeRate < 10:
                        equipments.ItemLevel += 1
                    else:
                        self.IsUserVIP(equipments, isVIP)
                        
    def RefineArmor(self, equipments, upgradeRate, isVIP):
        if equipments.RefineLevel < 5:
            equipments.ItemLevel += 1
        else:
            if upgradeRate < (10 - equipments.RefineLevel) * 10:
                equipments.ItemLevel += 1
            else:
                self.IsUserVIP(equipments, isVIP)

    def RefineEquipments(self, equipments, isVIP):
        for e in equipments:
            if e.ItemLevel < 10:
                upgradeRate = random.randint(0, 100)
                if e.Type == "Weapon":
                    self.RefineWeapon(e, upgradeRate, isVIP)
                elif e.Type == "Armor":
                    self.RefineArmor(e, upgradeRate, isVIP)