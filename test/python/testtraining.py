import random
hero_strenght = 10

hero_name = "Abdulahi"

def trainHero(hero_strenght):
    while(True):
        
        fight_reusult = random.randint(1,3)
        trainer = "Aldulso the Great Swordmaster"
        if fight_reusult == 1:
            hero_strenght = hero_strenght + 1
            print(hero_name,"Vann fighten och känner sig starkare. Styrka: ", hero_strenght)    
        elif fight_reusult == 2:
            hero_strenght = hero_strenght - 1
            print(trainer, "won", hero_name, "är inte så bra som han troede, och behöver träna mer.", hero_strenght)
        else:
            print(hero_name, "är en äkta hjälte. Träningen avslutas.")
            return hero_strenght

result = trainHero(hero_strenght)

print("Nu har hjälten", hero_strenght)