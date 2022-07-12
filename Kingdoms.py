import time
import random
age="Stone Age"
relationship=5
endgame=False
soldiers=0
soldierprice=100
points=0
level=1
levelup=200
endgame=0
popgrowth=5
gorranpopgrowth=5
popdeath=1
gorranpopdeath=2
death=True
war=0
land=1
buildmaterials=50
buildmaterialspro=1
money=50
day=1
pop=300
buildproupgradeprice=10
buildprolevel=1
moneypro=1
moneyprolevel=1
moneyproupgradeprice=10
defenselevel=1
defenseupgradeprice=10
defenseupgradebuildcost=10
gorranpop=300
gorrandefenselevel=1
exploreprice=10
defenseupgradelandcost=1
gorransoldiers=0
mortars=0
mortarprice=500
gorranmortars=0
missiles=0
missileprice=2000
gorranmissiles=0
nukes=0
nukeprice=7000
gorrannukes=0
hbombs=0
hbombprice=10000
gorranhbombs=0
bhbombs=0
bhbombprice=20000
gorranbhbombs=0
food=300
foodpro=300
foodproupgradeprice=50
foodprolevel=1
daysuntil=0
birth=True
birthres=0
foodres=0
foodprocan=True
spells=[]
sword=1
war2=1
attack=1
defense=1
destruction=1
waste=1
death=1
consumpmult=1
prodmult=1
birthmult=1
diffmult=1
print("Welcome to Kingdoms, a kingdom role playing game where you upgrade, level up, and try to defeat your enemies.\n")
time.sleep(1)
print("Please select a difficulty:")
print("1: Super Easy")
print("2: Easy")
print("3: Normal")
print("4: Hard")
print("5: Almost Impossible")
d=int(input())
if d==1:
    diffmult=2
elif d==2:
    diffmult=1.5
elif d==4:
    diffmult=0.7
elif d==5:
    diffmult=0.5
else:
    diffmult=1
con=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vow=["a","e","i","o","u"]
name=""
numofletterpairs=random.randint(2,4)
for i in range(numofletterpairs):
    name=name+random.choice(con)
    name=name+random.choice(vow)
    name=name.capitalize()
kingdomname=str(input("What do you name your kingdom?: "))
rulername=str(input("What is your name, your majesty?: "))
print()
print("Welcome "+str(rulername)+", ruler of "+str(kingdomname)+".\n")
print("You start with 300 people in your kingdom. You start with 50 building materials, 50$, 300 food, and have 1 land. Your people produce 300 food/day, 1 building material per day, and 1$ per day.\n\n")
print("They neighboring kingdom of "+name+" proposed a treaty! What do you do? If you accept, you will not be able to attack them, but you will be able to trade with them.")
print("A: Accept the treaty")
print("B: Don't accept")
treaty1=str(input())
if treaty1=="a" or treaty1=="A":
    tradewith=1
    relationship=5
    print("You have successfully set up a treaty with "+name+". You are friends now :)\n")
    time.sleep(1)
elif treaty1=="b" or treaty1=="B":
    relationship=3
    tradewith=0
    print(name+" doesn't like this, but you're fine for now.\n")
    time.sleep(1)
else:
    tradewith=1
    print("You have successfully set up a treaty with "+name+". You are friends now :)\n")
    time.sleep(1)
while endgame==False:
    if points>=levelup:
        level=level+1
        points=0
        levelup=int(levelup*1.5)
        print("\n\n\n\n-----------\n|LEVEL UP!|\n-----------\n\n\n\n")
        time.sleep(2)
        if level==5:
            print("You have entered the Copper Age!\nYou gain a new unit: Soldier!\n\n\n")
            age="Copper Age"
            time.sleep(1)
        if level==10:
            print("You have entered the Bronze Age!\nYou gain a new unit: Mortar!\n\n\n")
            age="Bronze Age"
            time.sleep(1)
        if level==15:
            print("You have entered the Iron Age!\nYou gain a new unit: Missile!\n(Hey, I never said this was historically accurate, so I DON'T WANT TO HEAR IT)\n\n")
            age="Iron Age"
            time.sleep(1)
        if level==20:
            print("You have entered the Middle Ages!\nYou gain a new unit: Nuke!\n(You can file a complaint to didIAskForYourOpinion@stopbotheringme.goaway)\n\n")
            age="Middle Ages"
            time.sleep(1)
        if level==25:
            print("You have entered the Modern Age!\nYou gain a new unit: H-bomb!\n\n\n")
            age="Modern Age"
            time.sleep(1)
        if level==30:
            print("You have entered the Future Age!\nYou gain a new unit: Black Hole Bomb!\n(Wow. You've made it this far. I salute you, and give you 2 of every spell as a reward)\n\n")
            age="Future Age"
            spells.append("Spell of Prosperity")
            spells.append("Spell of Fertility")
            spells.append("Spell of Wealth")
            spells.append("Spell of Work")
            spells.append("Spell of Sword")
            spells.append("Spell of War")
            spells.append("Spell of Attack")
            spells.append("Spell of Defense")
            spells.append("Spell of Destruction")
            spells.append("Spell of Waste")
            spells.append("Spell of Death")
            spells.append("Spell of Prosperity")
            spells.append("Spell of Fertility")
            spells.append("Spell of Wealth")
            spells.append("Spell of Work")
            spells.append("Spell of Sword")
            spells.append("Spell of War")
            spells.append("Spell of Attack")
            spells.append("Spell of Defense")
            spells.append("Spell of Destruction")
            spells.append("Spell of Waste")
            spells.append("Spell of Death")
            time.sleep(1)
    if points<0:
        if level>1:
            points=0
            level=level-1
            levelup=int(levelup/2)
            print("\n\n\n\n-------------\n|Level down.|\n-------------\n\n\n\n")
            time.sleep(2)
        else:
            points=0
            print("\n\n\n\n--------------------------------------\n|Your points went below 0. Be careful!|\n--------------------------------------\n\n\n\n")
            time.sleep(2)
    print("\nDay "+str("{:,}".format(day))+":\n")
    print(age)
    print("\nLevel: "+str("{:,}".format(level))+"\n")
    print("Points: "+str("{:,}".format(points))+"\n")
    print("Points needed for next level: "+str("{:,}".format(levelup))+"\n")
    buildmaterials=int(buildmaterials+(prodmult*buildmaterialspro))
    gorranpopgrowth=int(gorranpop/90)
    gorranpopdeath=int(gorranpop/150)
    money=int(money+(prodmult*moneypro))
    if birth==True:
        popgrowth=int(pop/95)
        pop=int(pop+(birthmult*popgrowth))
    else:
        if daysuntil>=birthres:
            birth=True
            daysuntil=0
            birthres=0
        else:
            daysuntil=daysuntil+1
    if death==True:
        popdeath=int(pop/200)
        pop=pop-popdeath
    if foodprocan==True:
        food=food+foodpro
    else:
        if fooddaysuntil>=foodres:
            foodprocan=True
            foodpro=2*foodpro
            food=food+foodpro
        else:
            fooddaysuntil=fooddaysuntil+1
    consumption=int(consumpmult*pop)
    if food<consumption:
        starved=pop-food
        pop=pop-starved
        food=food-pop
        print("You did not have enough food, so "+str(starved)+" people died of hunger.")
        time.sleep(1)
    else:
        food=int(food-consumption)
    gorranpop=gorranpop+gorranpopgrowth
    gorranpop=gorranpop-gorranpopdeath
    r1=int(40*diffmult)
    r2=int(40*diffmult)
    r3=int(50*diffmult)
    r4=int(70*diffmult)
    r5=int(100*diffmult)
    r6=int(150*diffmult)
    r7=int(200*diffmult)
    ranint=random.randint(1,r1)
    ranint2=random.randint(1,r2)
    ranint3=random.randint(1,r3)
    ranint4=random.randint(1,r4)
    ranint5=random.randint(1,r5)
    ranint6=random.randint(1,r6)
    ranint7=random.randint(1,r7)
    if ranint==1:
        gorrandefenselevel=gorrandefenselevel+1
    if level>=5:
        if ranint2==1:
            gorransoldiers=gorransoldiers+1
    if level>=10:
        if ranint3==1:
            gorranmortars=gorranmortars+1
    if level>=15:
        if ranint4==1:
            gorranmissiles=gorranmissiles+1
    if level>=20:
        if ranint5==1:
            gorrannukes=gorrannukes+1
    if level>=25:
        if ranint6==1:
            gorranhbombs=gorranhbombs+1
    if level>=30:
        if ranint7==1:
            gorranbhbombs=gorranbhbombs+1
    print("Building materials: "+str("{:,}".format(buildmaterials)))
    print("Building materials production: "+str("{:,}".format(int(prodmult*buildmaterialspro)))+"/day.")
    print("Money: $"+str("{:,}".format(money)))
    print("Money production: $"+str("{:,}".format(int(prodmult*moneypro)))+"/day.")
    print("Food: "+str("{:,}".format(food)))
    print("Food production: "+str("{:,}".format(foodpro))+"/day")
    print("Birth rate: "+str("{:,}".format(int(birthmult*popgrowth)))+"/day")
    print("Death rate: "+str("{:,}".format(popdeath))+" (overall population growth today: "+str("{:,}".format((birthmult*popgrowth)-popdeath))+")")
    print("Land: "+str("{:,}".format(land)))
    print("Population: "+str("{:,}".format(pop)))
    print("Relationship with "+name+": "+str(relationship)+"/5")
    print()
    print("What do you wish to do, "+rulername+"?")
    print("A: Upgrade building materials production for $"+str("{:,}".format(buildproupgradeprice))+" (current level: "+str("{:,}".format(buildprolevel))+")")
    print("B: Upgrade money production for "+str("{:,}".format(moneyproupgradeprice))+" building materials (current level: "+str("{:,}".format(moneyprolevel))+")")
    print("C: Upgrade defenses for $"+str("{:,}".format(defenseupgradeprice))+" and "+str("{:,}".format(defenseupgradebuildcost))+" building materials and "+str("{:,}".format(defenseupgradelandcost))+" land (current level: "+str("{:,}".format(defenselevel))+")")
    print("D: Upgrade food production for $"+str("{:,}".format(foodproupgradeprice))+" (current level: "+str("{:,}".format(foodprolevel))+")")
    print("E: Try to trade with "+name)
    print("F: Declare war on "+name)
    print("G: Explore for new land for $"+str("{:,}".format(exploreprice)))
    print("H/any other key: Next day")
    print("I: Wild card")
    print("J: Cast a spell")
    print("R: Regulate the law of the land")
    print("T: Manage your treaty relations with "+name)
    if level>=5:
        print("K: Train a soldier for $"+str("{:,}".format(soldierprice))+" (you currently have "+str("{:,}".format(soldiers))+")")
    if level>=10:
        print("L: Train a super mortar for $"+str("{:,}".format(mortarprice))+" (you currently have "+str("{:,}".format(mortars))+")")
    if level>=15:
        print("M: Train a missile for $"+str("{:,}".format(missileprice))+" (you currently have "+str("{:,}".format(missiles))+")")
    if level>=20:
        print("N: Train a nuke for $"+str("{:,}".format(nukeprice))+" (you currently have "+str("{:,}".format(nukes))+")")
    if level>=25:
        print("O: Train a H-bomb for $"+str("{:,}".format(hbombprice))+" (you currently have "+str("{:,}".format(hbombs))+")")
    if level>=30:
        print("P: Train a black hole bomb for $"+str(bhbombprice)+" (you currently have "+str(bhbombs)+")")
    dailydecision=str(input())
    if dailydecision=="a" or dailydecision=="A":
        if buildproupgradeprice>money:
            print("Not enough money!\n\n")
            points=points-level*50
            day=day+1
        else:
            money=money-buildproupgradeprice
            buildprolevel=buildprolevel+1
            buildmaterialspro=buildmaterialspro+int((1.5*buildprolevel))
            buildproupgradeprice=buildproupgradeprice+(25*buildprolevel)
            print("Successfully upgraded!\n\n")
            time.sleep(1)
            points=points+level*100
            day=day+1
    elif dailydecision=="r" or dailydecision=="R":
        print("What law would you like to change?")
        print("A: Birth laws")
        print("B: Work laws")
        d=str(input())
        if d=="A" or d=="a":
            print("What part do you want to change?")
            print("A: Change birth law to Limited (1/2x regular)")
            print("B: Change birth law to Regular (default)")
            print("C: Change birth law to Abundant (2x regular)")
            d1=str(input())
            if d1=="A" or d1=="a":
                birthmult=0.5
                print("Successfully changed!")
            elif d1=="C" or d1=="c":
                birthmult=2
                print("Successfully changed!")
            else:
                birthmult=1
                print("Successfully changed!")
            day=day+1
            time.sleep(1)
        else:
            print("What part do you want to change?")
            print("A: Change work law to Slow (people consume x1/2 food than regular, but money and building material production x1/2)")
            print("B: Change work law to Regular (default)")
            print("C: Change work law to Efficient (money and building material production x2, but people consume x2 more food than regular)")
            d2=str(input())
            if d2=="A" or d2=="a":
                consumpmult=0.5
                prodmult=0.5
                print("Successfully changed!")
            elif d2=="C" or d2=="c":
                consumpmult=2
                prodmult=2
                print("Successfully changed!")
            else:
                consumpmult=1
                prodmult=1
                print("Successfully changed!")
            day=day+1
            time.sleep(1)
    elif dailydecision=="b" or dailydecision=="B":
        if moneyproupgradeprice>buildmaterials:
            print("Not enough building materials!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        else:
            buildmaterials=buildmaterials-moneyproupgradeprice
            moneyprolevel=moneyprolevel+1
            moneypro=moneypro+int((1.5*moneyprolevel))
            moneyproupgradeprice=moneyproupgradeprice+(25*moneyprolevel)
            print("Successfully upgraded!\n\n")
            time.sleep(1)
            points=points+level*100
            day=day+1
    elif dailydecision=="c" or dailydecision=="C":
        if defenseupgradeprice>money:
            print("Not enough money!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        elif defenseupgradebuildcost>buildmaterials:
            print("Not enough building materials!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        elif defenseupgradelandcost>land:
            print("Not enough land!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        else:
            buildmaterials=buildmaterials-defenseupgradebuildcost
            money=money-defenseupgradeprice
            land=land-defenseupgradelandcost
            defenselevel=defenselevel+1
            defenseupgradeprice=defenseupgradeprice+(25*defenselevel)
            defenseupgradebuildcost=defenseupgradebuildcost+(25*defenselevel)
            print("Successfully upgraded!\n\n")
            time.sleep(1)
            points=points+level*100
            day=day+1
    elif dailydecision=="d" or dailydecision=="D":
        if foodproupgradeprice>money:
            print("Not enough money!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        else:
            money=money-foodproupgradeprice
            foodprolevel=foodprolevel+1
            foodpro=foodpro+(100*foodprolevel)
            foodproupgradeprice=foodproupgradeprice+(15*foodprolevel)
            print("Successfully upgraded!\n\n")
            time.sleep(1)
            points=points+level*100
            day=day+1
    elif dailydecision=="e" or dailydecision=="E":
        if tradewith==1:
            trade=str(input("What do you want to trade for ('b' for building materials, and 'm' for money): "))
            if trade=="b" or trade=="B":
                print(name+" will trade you building materials for 1 dollar each.")
                tradenum=int(input("How many do you wish to trade for?: "))
                if tradenum>money:
                    print("Not enough money!\n\n")
                    time.sleep(1)
                    points=points-level*50
                    day=day+1
                elif tradenum==0:
                    print("You cannot trade for 0 money/building materials!\n\n")
                    time.sleep(1)
                    day=day+1
                else:
                    money=money-tradenum
                    buildmaterials=buildmaterials+tradenum
                    print("You successfully traded for "+str("{:,}".format(tradenum))+" build material(s)!\n\n")
                    time.sleep(1)
                    points=points+level*100
                    day=day+1
            elif trade=="m" or trade=="M":
                print(name+" will trade $1 each for building materials.")
                tradenum=int(input("How many do you wish to trade for?: "))
                if tradenum>buildmaterials:
                    print("Not enough building materials!\n\n")
                    time.sleep(1)
                    points=points-level*50
                    day=day+1
                elif tradenum==0:
                    print("You cannot trade for 0 money/building materials!\n\n")
                    time.sleep(1)
                    day=day+1
                else:
                    money=money+tradenum
                    buildmaterials=buildmaterials-tradenum
                    print("You successfully traded for $"+str("{:,}".format(tradenum))+"!\n\n")
                    time.sleep(1)
                    points=points+level*100
                    day=day+1
        else:
            print("You do not have a treaty with "+name+"!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
    elif dailydecision=="f" or dailydecision=="F":
        if tradewith==1:
            print("You have a treaty with "+name+", so you cannot attack them.")
            time.sleep(1)
            day=day+1
        else:
            relationship=relationship-2
            if relationship<0:
                relationship=0
            gorranwarpoints=int((7*gorrandefenselevel)+(0.25*gorranpop)+(7*gorransoldiers)+(15*gorranmortars)+(30*gorranmissiles)+(50*gorrannukes)+(100*gorranhbombs)+(200*gorranbhbombs))
            warpoints=int(sword*war2*attack*defense*destruction*waste*death*((7*defenselevel)+(0.25*pop)+(7*soldiers)+(15*mortars)+(30*missiles)+(50*nukes)+(100*hbombs)+(200*bhbombs)))
            if warpoints>gorranwarpoints:
                winby=warpoints-gorranwarpoints
                print("\n\nYou won! You looted their city and got many items:")
                moneyadd=int(0.5*winby)
                buildadd=int(0.5*winby)+11
                landadd=int((0.5*winby))
                foodadd=int((0.5*winby))+50
                gorranpop=gorranpop-(0.5*gorranpop)
                money=money+moneyadd
                buildmaterials=buildmaterials+buildadd
                land=land+landadd
                food=food+foodadd
                points=points+level*100
                pop=pop-(0.1*pop)
                print("- $"+str("{:,}".format(moneyadd)))
                print("- "+str("{:,}".format(buildadd))+" building material(s)")
                print("- "+str("{:,}".format(landadd))+" new land")
                print("- "+str("{:,}".format(foodadd))+" more food\n")
                print("However, you have lost "+str("{:,}".format(int(0.1*pop)))+" people in the war.\n\n")
                time.sleep(2)
                day=day+1
            elif gorranwarpoints>warpoints:
                loseby=gorranwarpoints-warpoints
                print("\n\nYou lost. They looted your city and got many items:")
                moneysubtract=int(0.5*loseby)
                buildsubtract=int(0.5*loseby)
                landsubtract=int(0.5*land)
                foodsubtract=int(0.5*loseby)
                food=food-foodsubtract
                if food<0:
                    foodsubtract=foodsubtract+food
                    food=0
                land=land-landsubtract
                gorranpop=gorranpop-(0.1*gorranpop)
                pop=int(0.5*pop)
                money=money-moneysubtract
                if money<0:
                    moneysubtract=moneysubtract+money
                    money=0
                buildmaterials=buildmaterials-buildsubtract
                if buildmaterials<0:
                    buildsubtract=buildsubtract+buildmaterials
                    buildmaterials=0
                points=points-level*100
                print("- $"+str("{:,}".format(moneysubtract)))
                print("- "+str("{:,}".format(buildsubtract))+" building material(s)")
                print("- "+str("{:,}".format(landsubtract))+" land")
                print("- "+str("{:,}".format(foodsubtract))+" food\n")
                print("You have also lost "+str("{:,}".format(int(0.5*pop)))+" people in the war.")
                time.sleep(2)
                day=day+1
            elif gorranwarpoints==warpoints:
                print("You tied. Neither of you lost anything.")
                time.sleep(1)
                day=day+1
            else:
                print("If you're seeing this message, something is seriously wrong.")
    elif dailydecision=="g" or dailydecision=="G":
        if exploreprice>money:
            print("Not enough money!\n\n")
            time.sleep(1)
            points=points-level*50
            day=day+1
        else:
            landgain=int((0.5*land)+1)
            money=money-exploreprice
            land=land+landgain
            exploreprice=3*exploreprice
            exploregainNum=random.randint(1,9)
            if exploregainNum==1:
                spells.append("Spell of Prosperity")
                print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Prosperity!\n\n")
            elif exploregainNum==2:
                spells.append("Spell of Fertility")
                print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Fertility!\n\n")
            elif exploregainNum==3:
                spells.append("Spell of Wealth")
                print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Wealth!\n\n")
            elif exploregainNum==4:
                spells.append("Spell of Work")
                print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Work!\n\n")
            elif exploregainNum==5:
                if level<5:
                    spells.append("Spell of Sword")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Sword!\n\n")
                elif level>=5 and level<10:
                    spells.append("Spell of War")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of War!\n\n")
                elif level>=10 and level<15:
                    spells.append("Spell of Attack")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Attack!\n\n")
                elif level>=15 and level<20:
                    spells.append("Spell of Defense")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Defense!\n\n")
                elif level>=20 and level<25:
                    spells.append("Spell of Destruction")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Destruction!\n\n")
                elif level>=25 and level<30:
                    spells.append("Spell of Waste")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Waste!\n\n")
                else:
                    spells.append("Spell of Death")
                    print("You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Death!\n\n")
            else:
                print("You went exploring and found "+str("{:,}".format(landgain))+" land.")
            time.sleep(1)
            points=points+level*50
            day=day+1
    elif dailydecision=="i" or dailydecision=="I":
        wildcard=random.randint(1,10)
        if wildcard==1:
            moneygain=int(0.7*money)+1
            print("Some farmers found a hidden treasure chest containing "+str("{:,}".format(moneygain))+" in the ground while tilling their field.\n\n")
            time.sleep(1)
            money=money+moneygain
            day=day+1
        elif wildcard==2:
            buildloss=int(0.3*buildmaterials)
            print("A clumsy worker dropped "+str("{:,}".format(buildloss))+" building materials into the endless pit of endlessness, where they are never seen again.\n\n")
            time.sleep(1)
            buildmaterials=buildmaterials-buildloss
            day=day+1
        elif wildcard==3:
            foodgain=int(0.3*food)+2
            print("Some travellers found an abandoned storehouse with "+str("{:,}".format(foodgain))+" food in it.\n\n")
            time.sleep(1)
            food=food+foodgain
            day=day+1
        elif wildcard==4:
            popgrowth=0
            pop=pop-50
            birth=False
            birthres=10
            print("A meteor struck the land, causing the death of 50 people. The radiation also caused the birth rate to become 0 for 10 days.\n\n")
            time.sleep(1)
            day=day+1
        elif wildcard==5:
            pointsneeded=levelup-points
            points=points+pointsneeded
            print("You came across a sorceror's hut and he graciously gave you enough points to level up!\n\n")
            time.sleep(1)
            day=day+1
        elif wildcard==6:
            tradewith=0
            print("Your incompetent royal advisor accidentally sent a mean note to "+name+". This made them mad, and so they terminated your treaty.\n\n")
            time.sleep(1)
            day=day+1
        elif wildcard==7:
            buildgain=int(0.4*buildmaterials)+1
            buildmaterials=buildmaterials+buildgain
            print("You found a building in pretty good shape, and knocked it down to reuse its "+str("{:,}".format(buildgain))+" building materials.\n\n")
            time.sleep(1)
            day=day+1
        elif wildcard==8:
            foodloss=int((0.3*food)-1)
            food=food-foodloss
            foodpro=int(0.5*foodpro)
            foodres=3
            fooddaysuntil=0
            foodprocan=False
            print("Do to a draught, you lose "+str("{:,}".format(foodloss))+" food and your food production is halved for 3 days.\n\n")
            day=day+1
        elif wildcard==9:
            if level<5:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Sword")
                    print("You got the Spell of Sword! This spell will grant you 1.1 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=5 and level<10:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of War")
                    print("You got the Spell of War! This spell will grant you 1.5 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=10 and level<15:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Attack")
                    print("You got the Spell of Attack! This spell will grant you 1.7 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=15 and level<20:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Defense")
                    print("You got the Spell of Defense! This spell will grant you 2 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=20 and level<25:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Destruction")
                    print("You got the Spell of Destruction! This spell will grant you 2.5 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=25 and level<30:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Waste")
                    print("You got the Spell of War! This spell will grant you 2.7 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
            elif level>=30:
                sp=random.randint(1,5)
                if sp==1:
                    spells.append("Spell of Prosperity")
                    print("You got the Spell of Prosperity! This spell will level you up 1 level in food production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==2:
                    spells.append("Spell of Fertility")
                    print("You got the Spell of Fertility! This spell will grant you 100 population.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==3:
                    spells.append("Spell of Wealth")
                    print("You got the Spell of Wealth! This spell will level you up 1 level in money production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==4:
                    spells.append("Spell of Work")
                    print("You got the Spell of Work! This spell will level you up 1 level in building materials production.\n\n")
                    time.sleep(1)
                    day=day+1
                elif sp==5:
                    spells.append("Spell of Death")
                    print("You got the Spell of Death! This spell will grant you 3 times your war points in battle.\n\n")
                    time.sleep(1)
                    day=day+1
        else:
            points=points-(points+1)
            print("A mean sorceror caused your points to go below 0 so now you leveled down.")
            time.sleep(1)
            day=day+1
    elif dailydecision=="j" or dailydecision=="J":
        print("Here are the spells you own:")
        print(spells)
        if level<5:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            spe=str(input())
        elif level>=5 and level<10:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            spe=str(input())
        elif level>=10 and level<15:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            print("G: Spell of Attack")
            spe=str(input())
        elif level>=15 and level<20:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            print("G: Spell of Attack")
            print("H: Spell of Defense")
            spe=str(input())
        elif level>=20 and level<25:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            print("G: Spell of Attack")
            print("H: Spell of Defense")
            print("I: Spell of Destruction")
            spe=str(input())
        elif level>=25 and level<30:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            print("G: Spell of Attack")
            print("H: Spell of Defense")
            print("I: Spell of Destruction")
            print("J: Spell of Waste")
            spe=str(input())
        elif level>=30:
            print("A: Spell of Prosperity")
            print("B: Spell of Fertility")
            print("C: Spell of Wealth")
            print("D: Spell of Work")
            print("E: Spell of Sword")
            print("F: Spell of War")
            print("G: Spell of Attack")
            print("H: Spell of Defense")
            print("I: Spell of Destruction")
            print("J: Spell of Waste")
            print("K: Spell of Death")
            spe=str(input())
        if spe=="a" or spe=="A":
            if "Spell of Prosperity" in spells:
                print("You suddenly hear the sound of plants growing...\n\n")
                foodprolevel=foodprolevel+1
                foodpro=foodpro+(100*foodprolevel)
                thing=spells.index("Spell of Prosperity")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="b" or spe=="B":
            if "Spell of Fertility" in spells:
                print("You suddenly hear the sound of babies crying...\n\n")
                pop=pop+100
                thing=spells.index("Spell of Fertility")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="c" or spe=="C":
            if "Spell of Wealth" in spells:
                print("You suddenly hear the sound of coins jingling...\n\n")
                moneyprolevel=moneyprolevel+1
                moneypro=moneypro+int((1.5*moneyprolevel))
                thing=spells.index("Spell of Wealth")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="d" or spe=="D":
            if "Spell of Work" in spells:
                print("You suddenly hear the sound of hammers clanking...\n\n")
                buildprolevel=buildprolevel+1
                buildmaterialspro=buildmaterialspro+int((1.5*buildprolevel))
                thing=spells.index("Spell of Work")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="e" or spe=="E":
            if "Spell of Sword" in spells:
                print("You suddenly hear the sound of swords swishing...\n\n")
                sword=1.1
                thing=spells.index("Spell of Sword")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="f" or spe=="F":
            if "Spell of War" in spells:
                print("You suddenly hear the sound of a battle cry...\n\n")
                war2=1.5
                thing=spells.index("Spell of War")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="g" or spe=="G":
            if "Spell of Attack" in spells:
                print("You suddenly hear the sound of troops rushing into battle...\n\n")
                attack=1.7
                thing=spells.index("Spell of Attack")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="h" or spe=="H":
            if "Spell of Defense" in spells:
                print("You suddenly hear the sound of swords hitting shields...\n\n")
                defense=2
                thing=spells.index("Spell of Defense")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="i" or spe=="I":
            if "Spell of Destruction" in spells:
                print("You suddenly hear the sound of a building collapsing...\n\n")
                destruction=2.5
                thing=spells.index("Spell of Destruction")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="j" or spe=="J":
            if "Spell of Waste" in spells:
                print("You suddenly hear the sound of withering...\n\n")
                waste=2.7
                thing=spells.index("Spell of Waste")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
        elif spe=="k" or spe=="K":
            if "Spell of Death" in spells:
                print("You suddenly hear the sound of screams...\n\n")
                death=3
                thing=spells.index("Spell of Death")
                spells.pop(thing)
                day=day+1
            else:
                print("You do not have this spell!\n\n")
                points=points-level*50
                day=day+1
    elif dailydecision=="k" or dailydecision=="K":
        if level>=5:
            if soldierprice>money:
                print("Not enough money!\n\n")
                time.sleep(1)
                points=points-level*50
                day=day+1
            else:
                money=money-soldierprice
                soldiers=soldiers+1
                soldierprice=soldierprice+(15*soldiers)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*100
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="l" or dailydecision=="L":
        if level>=10:
            if mortarprice>money:
                print("Not enough money!\n\n")
                time.sleep(1)
                points=points-level*50
                day=day+1
            else:
                money=money-mortarprice
                mortars=mortars+1
                mortarprice=mortarprice+(15*mortars)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*150
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="m" or dailydecision=="M":
        if level>=15:
            if missileprice>money:
                print("Not enough money!\n\n")
                time.sleep(1)
                points=points-level*50
                day=day+1
            else:
                money=money-missileprice
                missiles=mortars+1
                missileprice=missileprice+(15*missiles)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*150
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="n" or dailydecision=="N":
        if level>=20:
            if nukeprice>money:
                print("Not enough money!\n\n")
                time.sleep(1)
                points=points-level*50
                day=day+1
            else:
                money=money-nukeprice
                nukes=nukes+1
                nukeprice=nukeprice+(15*nukes)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*150
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="o" or dailydecision=="O":
        if level>=25:
            if hbombprice>money:
                print("Not enough money!\n\n")
                time.sleep(1)
                points=points-level*50
                day=day+1
            else:
                money=money-hbombprice
                hbombs=hbombs+1
                hbombprice=hbombprice+(15*hbombs)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*150
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="p" or dailydecision=="P":
        if level>=30:
            if bhbombprice>money:
                print("Not enough money!\n\n")
                points=points-level*50
                time.sleep(1)
                day=day+1
            else:
                money=money-bhbombprice
                bhbombs=bhbombs+1
                bhbombprice=bhbombprice+(15*bhbombs)
                print("Successfully trained!\n\n")
                time.sleep(1)
                points=points+level*150
                day=day+1
        else:
            day=day+1
            print()
            print()
    elif dailydecision=="t" or dailydecision=="T":
        print("What would you like to do?")
        print("1: Cancel an existing treaty")
        print("2: Propose a treaty")
        t=int(input())
        if t==1:
            if tradewith==0:
                print("There is no treaty to cancel!")
                time.sleep(1)
                day=day+1
            else:
                tradewith=0
                relationship=relationship-1
                print("Treaty cancelled!")
                time.sleep(1)
                day=day+1
        else:
            if tradewith==1:
                print("You already have a treaty!")
                time.sleep(1)
                day=day+1
            else:
                if relationship>=4:
                    tradewith=1
                    relationship=5
                    print("Treaty created!\n\n")
                    time.sleep(1)
                    day=day+1
                elif relationship==3:
                    r=random.randint(1,3)
                    if r==1:
                        print(name+" has rejected your treaty proposal!\n\n")
                        time.sleep(1)
                        day=day+1
                    else:
                        tradewith=1
                        relationship=4
                        print(name+" has accepted your treaty proposal!\n\n")
                        time.sleep(1)
                elif relationship==2 or relationship==1:
                    r=random.randint(1,3)
                    if r==1:
                        tradewith=1
                        relationship=relationship+random.randint(1,2)
                        print(name+" has cautiously accepted your treaty proposal!\n\n")
                        time.sleep(1)
                        day=day+1
                    else:
                        print(name+" has rejected your treaty proposal!\n\n")
                        time.sleep(1)
                        day=day+1
                else:
                    r=random.randint(1,5)
                    if r==1:
                        tradewith=1
                        relationship=relationship+random.randint(1,2)
                        print(name+" has cautiously accepted your treaty proposal!\n\n")
                        time.sleep(1)
                        day=day+1
                    else:
                        print(name+" has rejected your treaty proposal!\n\n")
                        time.sleep(1)
                        day=day+1
    else:
        day=day+1
        print()
        print()
    if pop<=0:
        print("Your population went to zero. Your kingdom...")
        time.sleep(1)
        print("\nis gone.")
        time.sleep(0.5)
        print("You lose.")
        time.sleep(2)
        break
