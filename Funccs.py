import time
import random

action = 0
usedability = 0
roll = 0
broll = 0
damage = 0
damageOT = 0
chavhp = 400 # hp
maxhpchav = 400 # maxhp
vicsec = 20 # ammo
chAP = 27 # ap
chamage = 0 # damage
layers = 1 # armor
flake = 5 # speed
slowness = 0 # enemy debuff
braindamage = 0 # enemy debuff
grevious = 1 # enemy debuff
OTcounter = 0 # DoT counter
endgame = 0
taAMMO = 2
drAMMO = 2
beer = 2
brHP = 800
brAP = 40
fixedHP = brHP
bramage = 0
tree = 0
brainbonked = 0


def fighter_system():
    global usedability
    global action, tree
    tree = 0
    bronzer = 0
    action = 0
    while bronzer == 0:
        print("What you want fam? (A, S, I)")
        actiont = input()
        time.sleep(0.5)
        if actiont == "A":
            bronzer = 1
            attack_system()
        elif actiont == "S":
            if usedability == 0:
                bronzer = 1
                ability_system()
            else:
                print("You've used your ability already fam.")
        elif actiont == "I":
            bronzer = 1
            item_system()
        else:
            print("Invalid Letter bruv, remember to caps fam!")


def rolling():
    print("Rolling...")
    global roll
    roll = random.randint(1, 20) + flake
    time.sleep(1.5)
    return roll


def brolling():
    print("Rolling...")
    global broll
    broll = random.randint(1, 20) - slowness + 5
    time.sleep(1.5)
    return broll


def attack_system():

        bronzer = 0
        while bronzer == 0:
            print("What attack would you like to use *chewing noises*?\n"
                  "(1) Bonk: Deals moderate damage based on bottle fullness and lowers intelligence.\n"
                  "(2) Gum Blast: Deals heavy damage and lowers speed.\n"
                  "(3) Midnight Bloom: Deals light to extreme heavy damage but has ammo.")
            actionchoose = input()
            if actionchoose == "1":
                bronzer = 1
                bonk_a()
            elif actionchoose == "2":
                bronzer = 1
                gum_a()
            elif actionchoose == "3":
                bronzer = 1
                spray_a()
            else:
                print("Invalid bruv!")
                fighter_system()


def bonk_a():
    global chamage
    global action
    global braindamage, chAP
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 20:
        print("Crit!")
        action = action + 1
        chamage = chamage + chAP + (vicsec / 5) * 2
        braindamage = braindamage + 3
        print("ARGH MY BRAIN!")
        print(f"Bonk! Did {chamage} damage!")
    elif roll >= 11:
        print("Hit!")
        action = action + 1
        chamage = chamage + chAP + (vicsec / 5)
        time.sleep(0.5)
        braindamage = braindamage + 1
        print("ARGH MY BRAIN!")
        print(f"Bonk! Did {chamage} damage!")
    else:
        print("Miss...")
        action = action + 1
        time.sleep(1)
    return action and chamage and braindamage


def gum_a():
    time.sleep(1)
    global chamage
    global slowness
    global action
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 20:
        print("Crit!")
        action = action + 1
        chamage = chAP * 3 + 10
        slowness = 3
        print(f"PTOOO! Did {chamage} damage!")
    elif roll >= 11:
        print("Hit!")
        action = action + 1
        chamage = chamage * 1.5 + 10
        time.sleep(0.5)
        slowness = 1
        print(f"PTOOO! Did {chamage} damage!")
    else:
        print("Miss...")
        action = action + 1
        time.sleep(1)
    return action and chamage and slowness


def spray_a():
    global chamage
    global action, chAP, vicsec
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 20:
        print("Crit!")
        action = action + 1
        chamage = chAP * (round(vicsec / 10)) * 2.5
        vicsec = vicsec - 10
        print(f"Spritz! Did {chamage} damage!")
    elif roll >= 11:
        print("Hit!")
        action = action + 1
        chamage = chAP * (round(vicsec / 10))
        vicsec = vicsec - 10
        time.sleep(0.5)
        print(f"Spritz! Did {chamage} damage!")
    else:
        print("Miss...")
        action = action + 1
        time.sleep(1)
        vicsec = vicsec - 10
    return action and chamage


def ability_system():
    bronzer = 0
    global usedability
    while bronzer == 0:
        print("What ability do you want *spritzing noises*?\n"
          "(1) Amber Romance: Deals damage overtime (does not stack) and prevents healing.\n"
          "(2) Love Spell: Has a chance to stun or slows.\n"
          "(3) Rush: Gives self 5 flake for 1 turn.\n")
        actionchoose = input()
        if actionchoose == "1":
            bronzer = 1
            usedability = 1
            amber_a()
        elif actionchoose == "2":
            bronzer = 1
            usedability = 1
            love_a()
        elif actionchoose == "3":
            bronzer = 1
            usedability = 1
            rush_a()
        else:
            print("Invalid bruv!")
            fighter_system()


def amber_a():
    global chAP, damageOT, grevious, OTcounter, vicsec
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 11:
        print("Hit!")
        damageOT = (chAP / 4) + (round(vicsec / 10))
        vicsec = vicsec - 10
        OTcounter = 3
        grevious = 0.4
        time.sleep(0.5)
        print(f"Spritz!")
    else:
        print("Miss...")
        time.sleep(1)
    fighter_system()


def love_a():
    global slowness, vicsec
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 20:
        print("Crit!")
        slowness = slowness - 2
        vicsec = vicsec - 10
    elif roll >= 11:
        print("Hit!")
        slowness = slowness - 1
        time.sleep(0.5)
        vicsec = vicsec - 10
        print(f"Spritz!")
    else:
        print("Miss...")
        time.sleep(1)
    return slowness


def rush_a():
    global flake, vicsec
    time.sleep(1)
    rolling()
    print(roll)
    if roll >= 20:
        print("Crit!")
        flake = flake + 3
        vicsec = vicsec - 10
    else:
        print("Hit!")
        flake = flake + 1
        time.sleep(0.5)
        vicsec = vicsec - 10
        print(f"Spritz!")
    return flake


def item_system():
    global chavhp, maxhpchav, taAMMO, drAMMO, beer, chamage, vicsec, action, chAP
    while action == 0:
        print(f"What item?\n"
              f"(1) Total Attraction (Health) x{taAMMO}\n"
              f"(2) Dream (Attack) x{drAMMO}\n"
              f"(3) Bottle of Alcohol x{beer}")
        choice = int(input())
        if choice == 1 and taAMMO >= 1 and chavhp < maxhpchav:
            time.sleep(1)
            print("Spritz!")
            chavhp = chavhp + chAP
            taAMMO = taAMMO - 1
            action = action + 1
        elif choice == 1 and taAMMO >= 1 and chavhp >= maxhpchav:
            print("You have max hp!")
        elif choice == 2 and drAMMO >= 1:
            time.sleep(1)
            print("Spritz!")
            chAP = chAP * 2 + 15 + random.randint(1, 25)
            drAMMO = drAMMO - 1
            action = action + 1
        elif choice == 3 and beer >= 1:
            time.sleep(1)
            print("Refilling...")
            time.sleep(0.5)
            vicsec = vicsec + 15
            beer = beer - 1
            action = action + 1
        else:
            print("Invalid fam.")
            fighter_system()
    fighter_system()


def enemyai():
    global tree
    tree = 1
    brolling()
    if brHP >= fixedHP * 0.75 and chamage <= 0:
        actionbr = random.randint(1, 3)
        if actionbr == 1:
            if broll >= 13:
                bible_bonk()
            else:
                print("Missed!")
        elif actionbr == 2:
            if broll >= 18:
                preach()
            else:
                print("Missed!")
        elif actionbr == 3:
            if broll >= 12:
                reflect()
            else:
                print("Missed!")
        else:
            print("Missed!")
    elif brHP >= fixedHP * 0.75 and chamage > 0:
        actionbr = random.randint(1, 3)
        if actionbr == 1:
            if broll >= 13:
                bible_bonk()
            else:
                print("Missed!")
        elif actionbr == 2:
            if broll >= 18:
                preach()
            else:
                print("Missed!")
        elif actionbr == 3:
            prayer()
        else:
            print("Missed!")
    elif brHP < fixedHP * 0.75 and chamage == 0:
        actionbr = random.randint(1, 6)
        if actionbr == 1:
            if broll >= 13:
                bible_bonk()
        elif actionbr == 2:
            if broll >= 18:
                preach()
        if actionbr == 3:
            if broll >= 13:
                bible_bonk()
        elif actionbr == 4:
            prayer()
        elif actionbr == 5:
            holy_water()
        elif actionbr == 6:
            if broll >= 16:
                suck()
    else:
        actionbr = random.randint(1, 6)
        if actionbr == 1:
            if broll >= 13:
                bible_bonk()
        elif actionbr == 2:
            if broll >= 18:
                preach()
        elif actionbr == 3:
            if broll >= 12:
                reflect()
        elif actionbr == 4:
            prayer()
        elif actionbr == 5:
            holy_water()
        elif actionbr == 6:
            if broll >= 16:
                suck()
        else:
            print("Missed!")


def suck():
    global brAP, brHP, bramage, chavhp, grevious
    print("*slurping noises*")
    bramage = chavhp * layers
    brHP = brHP + bramage * grevious
    return bramage, brHP


def holy_water():
    global brAP, brHP, grevious
    print("is that moist man spraying WASABI AND LINEN DEODORANT?! MOIST! (buff self)")
    brAP = brAP + 10
    brHP = brHP + brAP * grevious
    return brAP, brHP


def prayer():
    global brAP, vicsec, chamage, flake, layers
    print("Oh daddy in heaven, please heed my cu- call. (prays)")
    time.sleep(1)
    print("rolling...")
    if broll >= 11 and broll % 2 == 0:
        print("the teacher comes in and makes you less chav!")
        vicsec = vicsec / 2
        chamage = chamage - 5
    elif broll >= 11:
        print("Oh no fam, its raining, MY MAKEUP!")
        flake = flake - 1
        layers = layers + 0.2
    elif broll <= 10 and broll % 2 == 0:
        print("you feel more CHAV than ever!")
        chamage = chamage + 5
    else:
        print("sephora and mac are having an 80% SALE fam!")
        flake = flake + 2
    return vicsec, chamage, flake, layers


def reflect():
    global brAP, bramage
    print("Love thy neighbours as thyselves. (retaliating sounds)")
    bramage = chamage + brAP * layers / 5
    return bramage


def bible_bonk():
    global brAP, bramage, braindamage
    print("Let me remind you of JESUS *bonk*")
    bramage = brAP * layers
    return bramage, braindamage


def preach():
    global brAP, bramage, flake
    print("Live, Laugh, Jesus! (preaches)")
    flake = flake - 1
    bramage = (brAP * layers + random.randint(20, 50))
    return bramage, flake


def totaldamage():
    global chavhp, brHP, bramage, chamage, endgame, damageOT, braindamage, brainbonked
    if tree == 1:
        chavhp = chavhp - bramage
        print(f"Bible Retorter did {bramage} damage!\n"
              f"Your current HP is {chavhp}!")
        if chavhp <= 0:
            endgame = 1
            print("I ran out of bronzer... (YOU LOST...)")
    else:
        if braindamage >= 3:
            brainbonked = chamage + chAP + random.randint(10, 30) * 2
            print("oww, headache!")
            print(f"{brainbonked} damage bonus!")
            braindamage = 0
        if OTcounter > 0:
            chamage = chamage + damageOT
        brHP = brHP - (chamage + brainbonked)
        if brHP >= fixedHP * 0.75:
            print("He's still moist, fam!")
        elif brHP >= fixedHP * 0.5:
            print("He looks kinda moist fam!")
        elif brHP >= fixedHP * 0.2:
            print("He's almost fully moist!")
        else:
            print("Pretty sure he's deceased bruv!")
            if brHP <= 0:
                endgame = 1
                print("Jesus... is... my super... hero... (YOU WON!)\n"
                      "TOO moist fam, innit?")
    return True


def reset():
    global action, usedability, roll, broll, damage, bramage, tree, grevious, OTcounter, damageOT
    action = 0
    usedability = 0
    roll = 0
    broll = 0
    damage = 0
    bramage = 0
    brbrainbonked = 0
    tree = 0
    OTcounter = OTcounter - 1
    if OTcounter < 0:
        OTcounter = 0
    if OTcounter != 0:
        grevious = 1
        damageOT = 0
    return action, usedability, roll, broll, damage, bramage, tree, grevious, OTcounter


def debugsys():
    print(f"{brHP} Enemy HP")
    print(f"{slowness} Slowness")
    print(f"{braindamage} Brain Damage")
    print(f"{vicsec} Vic Sec")


while endgame != 1:
    fighter_system()
    totaldamage()
    if endgame == 1:
        break
    debugsys()
    enemyai()
    totaldamage()
    if endgame == 1:
        break
    debugsys()
    reset()
