from tkinter import *
import random
import time
window=Tk()
window.title("Kingdoms")
def update_day():
    global day,money,buildmaterials,moneypro,buildmaterialspro,food,foodpro,pop,popgrowth,popdeath,gorranpop,gorranpopgrowth,gorranpopdeath
    if pop<=0:
        display_area.config(text="Your population went to 0. You lose.")
        time.sleep(3)
        window.destroy()
    day=day+1
    money=money+moneypro
    buildmaterials=buildmaterials+buildmaterialspro
    popgrowth=int(pop/75)
    pop=int(pop+popgrowth)
    popdeath=int(pop/200)
    pop=pop-popdeath
    gorranpopgrowth=int(gorranpop/80)
    gorranpop=gorranpop+gorranpopgrowth
    gorranpopdeath=int(gorranpop/150)
    gorranpop=gorranpop-gorranpopdeath
    food=food+foodpro
    if food<pop:
        starved=pop-food
        pop=pop-starved
        food=int(food-pop)
        display_area.config(text="You did not have enough food, so "+str(starved)+" people died of hunger.")
    else:
        food=int(food-pop)
    dayDisplay.config(text="Day "+str(day))
    moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
    buildDisplay.config(text=str(buildmaterials)+" building materials (producing "+str(buildmaterialspro)+"/day)")
    foodDisplay.config(text=str(food)+" food (producing "+str(foodpro)+"/day)")
    popDisplay.config(text="Population: "+str(pop)+" (Birth rate: "+str(popgrowth)+"/day, Death rate: "+str(popdeath)+"/day. Overall population growth: "+str(popgrowth-popdeath)+")")
    window.after(2000,update_day)
def update_level():
    global points,level,levelup,age,spells
    if points>=levelup:
        level=level+1
        points=0
        levelup=int(levelup*1.5)
        display_area.config(text="-----------\n|LEVEL UP!|\n-----------")
        if level==5:
            display_area.config(text="You have entered the Copper Age!\nYou gain a new unit: Soldier!")
            age="Copper Age"
            ageDisplay.config(text=age,fg="orange")
            soldier.config(text="Buy a soldier for $"+str(soldierprice)+" (you have "+str(soldiers)+")")
        if level==10:
            display_area.config(text="You have entered the Bronze Age!\nYou gain a new unit: Mortar!")
            age="Bronze Age"
            ageDisplay.config(text=age,fg="orangered")
            mortar.config(text="Buy a mortar for $"+str(mortarprice)+" (you have "+str(mortars)+")")
        if level==15:
            display_area.config(text="You have entered the Iron Age!\nYou gain a new unit: Missile!\n(Hey, I never said this was historically accurate, so I DON'T WANT TO HEAR IT)")
            age="Iron Age"
            ageDisplay.config(text=age,fg="silver")
            missile.config(text="Buy a missile for $"+str(missileprice)+" (you have "+str(missiles)+")")
        if level==20:
            display_area.config(text="You have entered the Middle Ages!\nYou gain a new unit: Nuke!\n(You can file a complaint to didIAskForYourOpinion@stopbotheringme.goaway)")
            age="Middle Ages"
            ageDisplay.config(text=age,fg="brown")
            nuke.config(text="Buy a nuke for $"+str(nukeprice)+" (you have "+str(nukes)+")")
        if level==25:
            display_area.config(text="You have entered the Modern Age!\nYou gain a new unit: H-bomb!")
            age="Modern Age"
            ageDisplay.config(text=age,fg="yellow")
            hbomb.config(text="Buy a H-bomb for $"+str(hbombprice)+" (you have "+str(hbombs)+")")
        if level==30:
            display_area.config(text="You have entered the Future Age!\nYou gain a new unit: Black Hole Bomb!\n(Wow. You've made it this far. I salute you, and give you 2 of every spell as a reward)")
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
            ageDisplay.config(text=age,fg="gold")
            bhbomb.config(text="Buy a Black hole bomb for $"+str(bhbombprice)+" (you have "+str(bhbombs)+")")
        levelDisplay.config(text="Level "+str(level))
    pointsDisplay.config(text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)")
    window.after(33,update_level)
def upgrade_money():
    global moneypro,moneyprolevel,moneyproupgradeprice,buildmaterials,points
    if moneyproupgradeprice<=buildmaterials:
        buildmaterials=buildmaterials-moneyproupgradeprice
        moneyprolevel=moneyprolevel+1
        moneypro=moneypro+int((1.5*moneyprolevel))
        moneyproupgradeprice=moneyproupgradeprice+(25*moneyprolevel)
        points=points+(level*200)
        display_area.config(text="Successfully upgraded!")
        buildDisplay.config(text=str(buildmaterials)+" building materials (producing "+str(buildmaterialspro)+"/day)")
        moneyUpg.config(text="Upgrade money production for "+str(moneyproupgradeprice)+" building materials (current level: "+str(moneyprolevel)+")")
        pointsDisplay.config(text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)")
def upgrade_bm():
    global money,buildmaterialspro,buildprolevel,buildproupgradeprice,points
    if buildproupgradeprice<=money:
        money=money-buildproupgradeprice
        buildprolevel=buildprolevel+1
        buildmaterialspro=buildmaterialspro+int((1.5*buildprolevel))
        buildproupgradeprice=buildproupgradeprice+(25*buildprolevel)
        points=points+(level*200)
        display_area.config(text="Successfully upgraded!")
        moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
        buildUpg.config(text="Upgrade building materials production for $"+str(buildproupgradeprice)+" (current level: "+str(buildprolevel)+")")
        pointsDisplay.config(text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)")
def upgrade_food():
    global money,foodpro,foodproupgradeprice,foodprolevel,points
    if foodproupgradeprice<=money:
        money=money-foodproupgradeprice
        foodprolevel=foodprolevel+1
        foodpro=foodpro+int((100*foodprolevel))
        foodproupgradeprice=foodproupgradeprice+(15*buildprolevel)
        points=points+(level*200)
        display_area.config(text="Successfully upgraded!")
        moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
        foodUpg.config(text="Upgrade food production for $"+str(foodproupgradeprice)+" (current level: "+str(foodprolevel)+")")
        pointsDisplay.config(text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)")
def upgrade_defense():
    global defenseupgradeprice,defenseupgradebuildcost,defenseupgradelandcost,land,money,buildmaterials,defenselevel,points
    if defenseupgradeprice<=money and defenseupgradebuildcost<=buildmaterials and defenseupgradelandcost<=land:
        buildmaterials=buildmaterials-defenseupgradebuildcost
        money=money-defenseupgradeprice
        land=land-defenseupgradelandcost
        defenselevel=defenselevel+1
        defenseupgradeprice=defenseupgradeprice+(25*defenselevel)
        defenseupgradebuildcost=defenseupgradebuildcost+(25*defenselevel)
        display_area.config(text="Successfully upgraded!")
        points=points+level*100
        pointsDisplay.config(text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)")
        moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
        buildDisplay.config(text=str(buildmaterials)+" building materials (producing "+str(buildmaterialspro)+"/day)")
        landDisplay.config(text=str(land)+" land")
        defenseUpg.config(text="Upgrade defenses for $"+str(defenseupgradeprice)+" and "+str(defenseupgradebuildcost)+" building materials and "+str(defenseupgradelandcost)+" land (current level: "+str(defenselevel)+")")
def explore():
    global land,spells,money,exploreprice,points
    landgain=int((0.5*land)+1)
    if money>=exploreprice:
        money=money-exploreprice
        land=land+landgain
        exploreprice=int(1.5*exploreprice)
        exploregainNum=random.randint(1,9)
        if exploregainNum==1:
            spells.append("Spell of Prosperity")
            display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Prosperity!")
        elif exploregainNum==2:
            spells.append("Spell of Fertility")
            display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Fertility!")
        elif exploregainNum==3:
            spells.append("Spell of Wealth")
            display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Wealth!")
        elif exploregainNum==4:
            spells.append("Spell of Work")
            display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Work!")
        elif exploregainNum==5:
            if level<5:
                spells.append("Spell of Sword")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Sword!")
            elif level>=5 and level<10:
                spells.append("Spell of War")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of War!")
            elif level>=10 and level<15:
                spells.append("Spell of Attack")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Attack!")
            elif level>=15 and level<20:
                spells.append("Spell of Defense")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Defense!")
            elif level>=20 and level<25:
                spells.append("Spell of Destruction")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Destruction!")
            elif level>=25 and level<30:
                spells.append("Spell of Waste")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Waste!")
            else:
                spells.append("Spell of Death")
                display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land. You also found a spellbook that tought you the Spell of Death!")
        else:
            display_area.config(text="You went exploring and found "+str("{:,}".format(landgain))+" land.")
        points=points+level*150
    landDisplay.config(text=str(land)+" land")
    moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
    exploreB.config(text="Explore new land for $"+str(exploreprice))
    spellsDisplay.config(text="Your spells: "+str(spells))
def cast_spell():
    global spells,pop,buildprolevel,moneyprolevel,foodprolevel,moneypro,buildmaterialspro,foodpro,sword,war,attack,defense,destruction,waste,death
    for num in range(10):
        if "Spell of Prosperity" in spells:
            foodprolevel=foodprolevel+1
            foodpro=foodpro+(100*foodprolevel)
            thing=spells.index("Spell of Prosperity")
            spells.pop(thing)
            foodUpg.config(text="Upgrade food production for $"+str(foodproupgradeprice)+" (current level: "+str(foodprolevel)+")")
        if "Spell of Fertility" in spells:
            pop=pop+100
            thing=spells.index("Spell of Fertility")
            spells.pop(thing)
            popDisplay.config(text="Population: "+str(pop)+" (Birth rate: "+str(popgrowth)+"/day, Death rate: "+str(popdeath)+"/day. Overall population growth: "+str(popgrowth-popdeath)+")")
        if "Spell of Wealth" in spells:
            moneyprolevel=moneyprolevel+1
            moneypro=moneypro+int((1.5*moneyprolevel))
            thing=spells.index("Spell of Wealth")
            spells.pop(thing)
            moneyUpg.config(text="Upgrade money production for "+str(moneyproupgradeprice)+" building materials (current level: "+str(moneyprolevel)+")")
        if "Spell of Work" in spells:
            buildprolevel=buildprolevel+1
            buildmaterialspro=buildmaterialspro+int((1.5*buildprolevel))
            thing=spells.index("Spell of Work")
            spells.pop(thing)
            buildUpg.config(text="Upgrade building materials production for $"+str(buildproupgradeprice)+" (current level: "+str(buildprolevel)+")")
        if "Spell of Sword" in spells:
            sword=1.1
            thing=spells.index("Spell of Sword")
            spells.pop(thing)
        if "Spell of War" in spells:
            war=1.5
            thing=spells.index("Spell of War")
            spells.pop(thing)
        if "Spell of Attack" in spells:
            attack=1.7
            thing=spells.index("Spell of Attack")
            spells.pop(thing)
        if "Spell of Defense" in spells:
            defense=2
            thing=spells.index("Spell of Defense")
            spells.pop(thing)
        if "Spell of Destruction" in spells:
            destruction=2.5
            thing=spells.index("Spell of Destruction")
            spells.pop(thing)
        if "Spell of Waste" in spells:
            waste=2.7
            thing=spells.index("Spell of Waste")
            spells.pop(thing)
        if "Spell of Death" in spells:
            death=3
            thing=spells.index("Spell of Death")
            spells.pop(thing)
    display_area.config(text="Casted all available spells!")
    spellsDisplay.config(text="Your spells: "+str(spells))
def DecWar():
    global points,tradewith,money,buildmaterials,food,pop,land,sword,war,attack,defense,destruction,waste,death,defenselevel,soldiers,mortars,missiles,nukes,hbombs,bhbombs,gorranpop
    gorranwarpoints=int((5*gorrandefenselevel)+(0.25*gorranpop)+(5*gorransoldiers)+(15*gorranmortars)+(30*gorranmissiles)+(50*gorrannukes)+(100*gorranhbombs)+(200*gorranbhbombs))
    tradewith=0
    warpoints=int(sword*war*attack*defense*destruction*waste*death*((5*defenselevel)+(0.25*pop)+(5*soldiers)+(15*mortars)+(30*missiles)+(50*nukes)+(100*hbombs)+(200*bhbombs)))
    if warpoints>gorranwarpoints:
        winby=warpoints-gorranwarpoints
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
        display_area.config(text="You won! You looted their city and got many items:\n- $"+str("{:,}".format(moneyadd))+"\n- "+str("{:,}".format(buildadd))+" building material(s)\n- "+str("{:,}".format(landadd))+" new land\n- "+str("{:,}".format(foodadd))+" more food\nHowever, you no longer have a treaty with Gorran and cannot trade with them. You also have lost "+str("{:,}".format(int(0.1*pop)))+" people in the war.")     
        pop=int(0.9*pop)
    elif gorranwarpoints>warpoints:
        loseby=gorranwarpoints-warpoints
        moneysubtract=int(0.5*loseby)
        buildsubtract=int(0.5*loseby)
        landsubtract=int(0.5*land)
        foodsubtract=int(0.5*loseby)
        food=food-foodsubtract
        land=land-landsubtract
        gorranpop=gorranpop-(0.1*gorranpop)
        money=money-moneysubtract
        buildmaterials=buildmaterials-buildsubtract
        points=points-level*100
        display_area.config(text="You lost. They looted your city and got many items:\n- $"+str("{:,}".format(moneysubtract))+"\n- "+str("{:,}".format(buildsubtract))+" building material(s)\n- "+str("{:,}".format(landsubtract))+" land- "+str("{:,}".format(foodsubtract))+" food\nYou have also lost "+str("{:,}".format(int(0.5*pop)))+" people in the war.\nYou also have lost your treaty with Gorran and can no longer trade with them.")
        pop=int(0.5*pop)
    elif gorranwarpoints==warpoints:
        display_area.config(text="You tied. Neither of you lost anything. However, you no longer have a treaty with Gorran.")
    else:
        display_area.config(text="If you're seeing this message, something is seriously wrong.")
    moneyDisplay.config(text="$"+str(money)+" (producing $"+str(moneypro)+"/day)")
    buildDisplay.config(text=str(buildmaterials)+" building materials (producing "+str(buildmaterialspro)+"/day)")
    foodDisplay.config(text=str(food)+" food (producing "+str(foodpro)+"/day)")
    popDisplay.config(text="Population: "+str(pop)+" (Birth rate: "+str(popgrowth)+"/day, Death rate: "+str(popdeath)+"/day. Overall population growth: "+str(popgrowth-popdeath)+")")
    landDisplay.config(text=str(land)+" land")
def buy_soldier():
    global soldiers,soldierprice,money,points,level
    if level>=5:
        if money>=soldierprice:
            money=money-soldierprice
            soldierprice=soldierprice+(15*soldiers)
            soldiers=soldiers+1
            display_area.config(text="Successfully bought!")
            soldier.config(text="Buy a soldier for $"+str(soldierprice)+" (you have "+str(soldiers)+")")
def buy_mortar():
    global mortars,mortarprice,money,points,level
    if level>=10:
        if money>=mortarprice:
            money=money-mortarprice
            mortarprice=mortarprice+(15*mortars)
            mortars=mortars+1
            display_area.config(text="Successfully bought!")
            mortar.config(text="Buy a mortar for $"+str(mortarprice)+" (you have "+str(mortars)+")")
def buy_missile():
    global missiles,missileprice,money,points,level
    if level>=15:
        if money>=missiles:
            money=money-missileprice
            missileprice=missileprice+(15*missiles)
            missiles=missiles+1
            display_area.config(text="Successfully bought!")
            missile.config(text="Buy a missile for $"+str(missileprice)+" (you have "+str(missiles)+")")
def buy_nuke():
    global nukes,nukeprice,money,points,level
    if level>=20:
        if money>=nukeprice:
            money=money-nukeprice
            nukeprice=nukeprice+(15*nukes)
            nukes=nukes+1
            display_area.config(text="Successfully bought!")
            nuke.config(text="Buy a nuke for $"+str(nukeprice)+" (you have "+str(nukes)+")")
def buy_hbomb():
    global hbombs,hbombprice,money,points,level
    if level>=25:
        if money>=hbombprice:
            money=money-hbombprice
            hbombprice=hbombprice+(15*hbombs)
            hbombs=hbombs+1
            display_area.config(text="Successfully bought!")
            hbomb.config(text="Buy a H-bomb for $"+str(hbombprice)+" (you have "+str(hbombs)+")")
def buy_bhbomb():
    global bhbombs,bhbombprice,money,points,level
    if level>=30:
        if money>=bhbombprice:
            money=money-bhbombprice
            bhbombprice=bhbombprice+(15*bhbombs)
            bhbombs=bhbombs+1
            display_area.config(text="Successfully bought!")
            bhbomb.config(text="Buy a Black hole bomb for $"+str(bhbombprice)+" (you have "+str(bhbombs)+")")
age="Stone Age"
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
spells=[]
sword=1
war=1
attack=1
defense=1
destruction=1
waste=1
death=1
consumpmult=1
prodmult=1
birthmult=1
dayDisplay=Label(window,text="Day "+str(day),fg="white",bg="black")
dayDisplay.pack()
ageDisplay=Label(window,text=age,fg="gray",bg="black")
ageDisplay.pack()
levelDisplay=Label(window,text="Level "+str(level),fg="white",bg="black")
levelDisplay.pack()
pointsDisplay=Label(window,text="Points "+str(points)+" (you need "+str(levelup)+" more points for the next level)",fg="blue",bg="black")
pointsDisplay.pack()
moneyDisplay=Label(window,text="$"+str(money)+" (producing $"+str(moneypro)+"/day)",fg="green",bg="black")
moneyDisplay.pack()
buildDisplay=Label(window,text=str(buildmaterials)+" building materials (producing "+str(buildmaterialspro)+"/day)",fg="khaki",bg="black")
buildDisplay.pack()
foodDisplay=Label(window,text=str(food)+" food (producing "+str(foodpro)+"/day)",fg="limegreen",bg="black")
foodDisplay.pack()
landDisplay=Label(window,text=str(land)+" land",fg="darkkhaki",bg="black")
landDisplay.pack()
popDisplay=Label(window,text="Population: "+str(pop)+" (Birth rate: "+str(popgrowth)+"/day, Death rate: "+str(popdeath)+"/day. Overall population growth: "+str(popgrowth-popdeath)+")",fg="tan",bg="black")
popDisplay.pack()
spellsDisplay=Label(window,text="Your spells: "+str(spells),fg="lightblue",bg="black")
spellsDisplay.pack()
moneyUpg=Button(window,text="Upgrade money production for "+str(moneyproupgradeprice)+" building materials (current level: "+str(moneyprolevel)+")",command=upgrade_money)
moneyUpg.pack()
buildUpg=Button(window,text="Upgrade building materials production for $"+str(buildproupgradeprice)+" (current level: "+str(buildprolevel)+")",command=upgrade_bm)
buildUpg.pack()
foodUpg=Button(window,text="Upgrade food production for $"+str(foodproupgradeprice)+" (current level: "+str(foodprolevel)+")",command=upgrade_food)
foodUpg.pack()
defenseUpg=Button(window,text="Upgrade defenses for $"+str(defenseupgradeprice)+" and "+str(defenseupgradebuildcost)+" building materials and "+str(defenseupgradelandcost)+" land (current level: "+str(defenselevel)+")",command=upgrade_defense)
defenseUpg.pack()
exploreB=Button(window,text="Explore new land for $"+str(exploreprice),command=explore)
exploreB.pack()
declareWar=Button(window,text="Declare war on Gorran!",command=DecWar,bg="red")
declareWar.pack()
spellCast=Button(window,text="Cast your spells!",command=cast_spell)
spellCast.pack()
soldier=Button(window,text="?????",command=buy_soldier)
soldier.pack()
mortar=Button(window,text="?????",command=buy_mortar)
mortar.pack()
missile=Button(window,text="?????",command=buy_missile)
missile.pack()
nuke=Button(window,text="?????",command=buy_nuke)
nuke.pack()
hbomb=Button(window,text="?????",command=buy_hbomb)
hbomb.pack()
bhbomb=Button(window,text="?????",command=buy_bhbomb)
missile.pack()
display_area=Label(window,text="",fg="crimson",bg="black")
display_area.pack()
window.after(2000,update_day)
window.after(33,update_level)
window.mainloop()
