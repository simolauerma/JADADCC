

def error(): #Virheen sattuessa
	print "|       An error has occurred. The Program will now close            |"
	print "|____________________________________________________________________|"
def empty(x): #Tulostaa tyhjan formatoidun rivin
	for i in range (1,x+1,1):
		print "|                                                                    |"
		
def valinta(): # User input, but hidden
	import getpass
	x = "0"
	x = x+getpass.getpass("|                                                                    |")
	x = int(float(x))
	return x
	
def end(): #ending print before closing
	print "|                    Thanks for using my program!                    |"
	print "|____________________________________________________________________|"
	
def retry(x,pieni,iso): # In case the user input is too big or small
	while x < pieni or x > iso:
		x = valinta()
	return x
	
def space(x): # Returns empty spacebar strokes
	return " "*(x-2)
	
def YN(): # simple Y/N choise
	print "|                           1: Yes                                   |"
	print "|                           2: No                                    |"
	return retry(valinta,1,2)

def mainmenu(): # aloitus paamenu
	print "______________________________________________________________________"
	print "| ________________   ______   _______   ______   _______   _______   |"
	print "| \__    _(  ___  ) (  __  \ (  ___  ) (  __  \ (  ____ \ (  ____ \  |"
	print "|    )  ( | (   ) | | (  \  )| (   ) | | (  \  )| (    \/ | (    \/  |"
	print "|    |  | | (___) | | |   ) || (___) | | |   ) || |       | |        |"
	print "|    |  | |  ___  | | |   | ||  ___  | | |   | || |       | |        |"
	print "|    |  | | (   ) | | |   ) || (   ) | | |   ) || |       | |        |" 
	print "| |\_)  ) | )   ( |_| (__/  )| )   ( |_| (__/  )| (____/\_| (____/\  |"
	print "| (____(_)|/     \(_|______(_)/     \(_|______(_|_______(_|_______/  |"
	print "|                                                                    |"
	print "|        just another dungeons and dragons character creator         |"
	print "|--------------------------------------------------------------------|"
	empty(2)
	print "|             1: Start creating your new character                   |"
	print "|             2: Info and help                                       |"
	print "|             3: Credits                                             |"
	print "|             4: Quit                                                |"
	empty(1)

def menu1(): #Ability scoret
	print "|--------------------------------------------------------------------|"
	print "|               Let's begin creating your new character              |"
	empty(1)
	print "|              First up, we're going to be determining               |"
	print "|                 your character's ability scores                    |"
	empty(2)
	print "|                 1: Roll the dice of fate yourself                  |"
	print "|                 2: Get randomly generated dicerolls                |"
def menu1_1(): # Ability scoret manuaalisesti
	print "|--------------------------------------------------------------------|"
	print "|             Now roll your dice and input your results              |"
	empty(2)
	print "|               Input the results of your first roll                 |"
	stat1=input("|                                                                    | \x1B[37D")
	print "|                       Input the second roll                        |"
	stat2=input("|                                                                    | \x1B[37D")
	print "|                       Input the third roll                         |"
	stat3=input("|                                                                    | \x1B[37D")
	print "|                       Input the fourth roll                        |"
	stat4=input("|                                                                    | \x1B[37D")
	print "|                       Input the fifth roll                         |"
	stat5=input("|                                                                    | \x1B[37D")
	print "|                       Input the final roll                         |"
	stat6=input("|                                                                    | \x1B[37D")
	allstats=[]
	allstats.append(stat1)
	allstats.append(stat2)
	allstats.append(stat3)
	allstats.append(stat4)
	allstats.append(stat5)
	allstats.append(stat6)
	allstats.sort(reverse=True)

	return allstats
def menu1_2(): # Ability scoret random nopanheittoina 
	import random
	import time
	stat = dict()
	for i in range (1,7,1):
		stat[i] = []
		for y in range(1,5,1):
			x = random.randrange(1,7,1)
			stat[i].append(x)
		stat[i].remove(min(stat[i]))
		stat[i]=sum(stat[i])
	print"|--------------------------------------------------------------------|"
	print"|             Generating Random dice rolls, hold on                  |" #The small delay gives the user a false sense of real randomness
	print"|--------------------------------------------------------------------|"
	time.sleep(0.3)
	print"|              The result for the first roll was                     |"
	empty(1)
	time.sleep(0.3)
	if stat[1] > 9:
		print"|                                -",stat[1],"-                              |"
	else:
		print"|                                 -",stat[1],"-                              |"
	print"|              The result for the second roll was                    |"
	empty(1)
	time.sleep(0.3)
	if stat[2] > 9:
		print"|                                -",stat[2],"-                              |"
	else:
		print"|                                 -",stat[2],"-                              |"	
	print"|              The result for the third roll was                     |"
	empty(1)
	time.sleep(0.3)
	if stat[3] > 9:
		print"|                                -",stat[3],"-                              |"
	else:
		print"|                                 -",stat[3],"-                              |"
	print"|              The result for the fourth roll was                    |"
	empty(1)
	time.sleep(0.3)
	if stat[4] > 9:
		print"|                                -",stat[4],"-                              |"
	else:
		print"|                                 -",stat[4],"-                              |"
	print"|              The result for the fifth roll was                     |"
	empty(1)
	time.sleep(0.3)
	if stat[5] > 9:
		print"|                                -",stat[5],"-                              |"
	else:
		print"|                                 -",stat[5],"-                              |"
	print"|              The result for the final roll was                     |"
	empty(1)
	time.sleep(0.3)
	if stat[6] > 9:
		print"|                                -",stat[6],"-                              |"
	else:
		print"|                                 -",stat[6],"-                              |"
	allstats=[]
	for abc in range (1,7,1):
		allstats.append(stat[abc])
	allstats.sort(reverse=True)
	return allstats

def menu2(allstats): # Ability scoret itse abilityihin
	pituus = 0
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|          Great, now we have ourselves some numbers                 |" 
	print "|          Next let's assign them to your abilities.                 |"
	empty(2)
	statsprint=["strength? (STR)       |", "dexterity? (DEX)      |", "constitution? (CON)   |","intelligence? (INT)   |", "wisdom? (WIS)         |", "charisma? (CHA)       |"]
	stats = []
	for stat in range (1,7,1):
		poisto=0
		print "|       What roll would you like to assign to ", statsprint[stat-1] #     |"
		empty(1)
		for roll in range (1,7-stat+1,1):
			if allstats[roll-1] > 9:
				print"|                             ",roll,": ",allstats[roll-1], "                              |"
			else:
				print"|                             ",roll,": ",allstats[roll-1], "                               |"
		poisto = retry(valinta(),1,7-stat)
		if allstats[poisto-1] >9:
			pituus=pituus+1
		stats.append(allstats[poisto-1])
		print "|--------------------------------------------------------------------|"
			   
		allstats.remove(allstats[poisto-1])
	
	empty(1)
	print "|                      Your ability scores are                       |"
	print "|         STR:",stats[0]," DEX:",stats[1]," CON:",stats[2], " INT:",stats[3]," WIS:",stats[4]," CHA:",stats[5],space(13-pituus),"|"
	empty(1)
	return stats
def menu2_1(abilityscore): #laskee ability modifierit
	abilitymod = []
	pituus = 0
	stats = abilitymod # koska olen liian laiska muuttamaan kaikkia rivin 194 stats[x]:ia abilitymod[x]:iksi
	for i in range (1,7,1):
		x=abilityscore[i-1]
		y = (x-10)/2
		abilitymod.append(y)
		if y < 0:
			pituus = pituus +1
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|                      Your ability modifiers are                    |"
	print "|         STR:",stats[0]," DEX:",stats[1]," CON:",stats[2], " INT:",stats[3]," WIS:",stats[4]," CHA:",stats[5],space(12-pituus)," |"
	empty(1)
	return abilitymod

def menu3_1(): #Main Classin valinta
	races = ["Dwarf","Elf","Hobbit","Human","Dragonborn","Gnome","Half-Elf","Half-Orc","Tiefling"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|     Next we'll dip our toes into the roleplaying aspect of your    |"
	print "|  character. Take a minute to concider who do you want to play as.  |"
	empty(1)
	print "|      We'll go over your character's Race, Background and Class.    |"
	empty(1)
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|                      Your Character's Race                         |"
	print "|  Your race defines some aspects of how your character should play  |"
	print "|          as well as some of his/her abilities and stats            |"
	empty(1)
	print "|             So, which race do you want to play as?                 |"
	empty(1)
	print "|                         1: Dwarf                                   |"
	print "|                         2: Elf                                     |"
	print "|                         3: Hobbit                                  |"
	print "|                         4: Human                                   |"
	print "|                         5: Dragonborn                              |"
	print "|                         6: Gnome                                   |"
	print "|                         7: Half-Elf                                |"
	print "|                         8: Half-Orc                                |"
	print "|                         9: Tiefling                                |"
	empty(1)
	valittu = retry(valinta,1,9)
	print "|                 So you want to play as a",races[valittu-1],"?",space(10+len(races[4])-len(races[valittu-1])),"    |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1()
		return valittu

	
def menu3_1_2(rotu): #yleinen subrace
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|                    Your character's Subrace                        |"
	empty(1)
	print "| Some of the races in Dungeons and Dragons have subraces, which are |"
	print "| small variations from the basic race. Some attributes are modified |"
	print "|                  depending on your subrace.                        |"
	empty(1)
	if rotu == 1:
		menu3_1_2_1()
	if rotu == 2:
		menu3_1_2_2()
	if rotu == 3:
		menu3_1_2_3()
	if rotu == 5:
		menu3_1_2_5()
	if rotu == 6:
		menu3_1_2_6()
		
def menu3_1_2_1(): #subrace Dwarf
	races=["Dwarf","Hill Dwarf","Mountain Dwarf"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|               Which variation of a Dwarf do you want?              |"
	empty(1)
	print "|                     1: Hill Dwarf                                  |"
	print "|                     2: Mountain Dwarf                              |"
	empty(1)
	valittu = retry(valinta,1,3)
	print "|           So you want to play as a",races[valittu-1],"?",space(14+len(races[2])-len(races[valittu-1])),"  |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1_2_1()
		return valittu
		
def menu3_1_2_2(): # subrace elf
	races=["Elf","Drow Elf","High Elf","Wood Elf"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|               Which variation of an Elf do you want?               |"
	empty(1)
	print "|                     1: Drow Elf                                    |"
	print "|                     2: High Elf                                    |"
	print "|                     3: Wood Elf                                    |"
	empty(1)
	valittu = retry(valinta,1,4)
	print "|                 So you want to play as",races[valittu-1],"?",space(8+len(races[2])-len(races[valittu-1])),"          |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1_2_2()
		return valittu
			
def menu3_1_2_3():# subrace hobbit
	races=["Hobbit","Lightfoot Hobbit","Stout Hobbit"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|               Which variation of a Hobbit do you want?             |"
	empty(1)
	print "|                     1: Lightfoot Hobbit                            |"
	print "|                     2: Stout Hobbit                                |"
	empty(1)
	valittu = retry(valinta,1,3)
	print "|         So you want to play as a",races[valittu-1],"?",space(16+len(races[1])-len(races[valittu-1])),"|"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1_2_3()
		return valittu
def menu3_1_2_5():# Ancestry Dragonborn (melkein subrace
	races=["Black","Blue","Brass","Bronze","Copper","Gold","Green","Red","Silver","White"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|              Which colour of a Dragonborn do you want?             |"
	print "|      (Colour affects your dragonborn breath weapon damage type)    |"
	empty(1)
	print "|                     1: Black                                       |"
	print "|                     2: Blue                                        |"
	print "|                     3: Brass                                       |"
	print "|                     4: Bronze                                      |"
	print "|                     5: Copper                                      |"
	print "|                     6: Gold                                        |"
	print "|                     7: Green                                       |"
	print "|                     8: Red                                         |"
	print "|                     9: Silver                                      |"
	print "|                    10: White                                       |"
	empty(1)
	valittu = retry(valinta,1,10)
	print "|           So you want to play as a",races[valittu-1],"Dragonborn?",space(6+len(races[3])-len(races[valittu-1])),"        |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1_2_5()
		return valittu
def menu3_1_2_6():# subrace gnome
	races=["Gnome","Forest Gnome","Rock Gnome"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|               Which variation of a Gnome do you want?              |"
	empty(1)
	print "|                     1: Forest Gnome                                |"
	print "|                     2: Rock Gnome                                  |"
	empty(1)
	valittu = retry(valinta,1,3)
	print "|             So you want to play as a",races[valittu-1],"?",space(12+len(races[2])-len(races[valittu-1])),"      |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_1_2_6()
		return valittu
def menu3_2(): # Backgroundin valinta
	BGs = ["Acolyte","Charlatan","Criminal","Entertainer","Folk Hero","Guild Artisan","Hermit","Noble","Outlander","Sage","Sailor","Soldier","Urchin"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|                   Your Character's Background                      |"
	print "| Your background defines a lot of how the character acts and reacts |"
	print "| around certain people, things or places. It also affects what your |"
	print "|            character has with them on their journies.              |"
	empty(1)
	print "|     So, from what background does your character stem from?        |"
	empty(1)
	print "|                      1: Acolyte                                    |"
	print "|                      2: Charlatan                                  |"
	print "|                      3: Criminal                                   |"
	print "|                      4: Entertainer                                |"
	print "|                      5: Folk Hero                                  |"
	print "|                      6: Guild Artisan                              |"
	print "|                      7: Hermit                                     |"
	print "|                      8: Noble                                      |"
	print "|                      9: Outlander                                  |"
	print "|                     10: Sage                                       |"
	print "|                     11: Sailor                                     |"
	print "|                     12: Soldier                                    |"
	print "|                     13: Urchin                                     |"
	empty(1)
	valittu = retry(valinta,1,13)
	print "|                 So you want to play as ",BGs[valittu-1],"?",space(13+len(BGs[4])-len(BGs[valittu-1])),"   |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_2()
		return valittu

		
def menu3_3():# Classin valinta
	classes=["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|                       Your Character's Class                       |"
	print "|   Your class defines who you are, what you do and how you fight.   |"
	print "|   Your class also determines whether or not you can cast spells.   |"
	print "|        Your equipment is largely determined by your class.         |"
	empty(1)
	print "|            So, what class should your character represent?         |"
	empty(1)
	print "|                      1: Barbarian                                  |"
	print "|                      2: Bard                                       |"
	print "|                      3: Cleric                                     |"
	print "|                      4: Druid                                      |"
	print "|                      5: Fighter                                    |"
	print "|                      6: Monk                                       |"
	print "|                      7: Paladin                                    |"
	print "|                      8: Ranger                                     |"
	print "|                      9: Rogue                                      |"
	print "|                     10: Sorcerer                                   |"
	print "|                     11: Warlock                                    |"
	print "|                     12: Wizard                                     |"
	empty(1)
	valittu = retry(valinta,1,12)
	print "|                 So you want to play as ",classes[valittu-1],"?",space(9+len(classes[0])-len(classes[valittu-1])),"       |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_3()
		return valittu
	
def menu3_3_2(character_class): #Classien sisaiset ability muuttujat tms
	if character_class == 3:
		palautus = menu3_cleric()
	elif character_class == 5:
		palautus = menu3_fighter()
	elif character_class == 8:
		palautus = menu3_ranger()
	elif character_class == 9:
		palautus = menu3_rogue()
	elif character_class == 10:
		palautus = menu3_sorcerer()
	elif character_class == 11:
		palautus = menu3_warlock()
	else:
		palautus = 0
	print palautus
	return palautus
	
def menu3_cleric():
	domains=["Knowledge","Life","Light","Nature","Tempest","Trickery","War"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|          The cleric class has a choice of a divine domain.         |"
	empty(1) 
	print "|        This domain affects what spells your cleric can cast.       |"
	empty(2)
	print "|           So, which divine domain do you want to pick?             |"
	empty(1)
	print "|                         1: Knowledge                               |"
	print "|                         2: Life                                    |"
	print "|                         3: Light                                   |"
	print "|                         4: Nature                                  |"
	print "|                         5: Tempest                                 |"
	print "|                         6: Trickery                                |"
	print "|                         7: War                                     |"
	empty(1)
	valittu = retry(valinta,1,7)
	print "|                 So you want to pick",domains[valittu-1],"Domain?",space(10+len(domains[0])-len(domains[valittu-1])),"    |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_cleric()	
		return valittu
	
def menu3_fighter():
	styles=["Archery","Defense","Dueling","Great Weapon Fighting","Protection","Two-weapon Fighting"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|         The fighter class has a choice of a fighting style.        |"
	empty(1) 
	print "|          This style affects how your fighter will fight.           |"
	empty(2)
	print "|           So, which fighting style do you want to pick?            |"
	empty(1)
	print "|                         1: Archery                                 |"
	print "|                         2: Defense                                 |"
	print "|                         3: Dueling                                 |"
	print "|                         4: Great Weapon Fighting                   |"
	print "|                         5: Protection                              |"
	print "|                         6: Two-weapon Fighting                     |"
	empty(1)
	valittu = retry(valinta,1,6)
	print "|             So you want to pick",styles[valittu-1],"style?",space(7+len(styles[3])-len(styles[valittu-1])),"|"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_fighter()	
		return valittu
	
def menu3_ranger(x):
	enemy=["Aberrations","Beasts","Celestials","Constructs","Dragons","Elementals","Fey","Fiends","Giants","Monstrosities","Oozes","Plants","Undead","Two classes of humanoid"]
	explore=["Arctic","Coast","Desert","Forest","Grassland","Mountain","Swamp","The Underdark"]
	if x == 0: 
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                   The Ranger class has two choises.                |"
		empty(1) 
		print "|  A choise of a preferred enemy type, that you have advantage over  |"
		print "|  And a choise of a familiar terrain, on which you have bonuses on  |"
		empty(2)
		print "|           So, which preferred enemy do you want to pick?           |"
		empty(1)
		print "|                         1: Aberrations                             |"
		print "|                         2: Beasts                                  |"
		print "|                         3: Celestials                              |"
		print "|                         4: Constructs                              |"
		print "|                         5: Dragons                                 |"
		print "|                         6: Elementals                              |"
		print "|                         7: Fey                                     |"
		print "|                         8: Fiends                                  |"
		print "|                         9: Giants                                  |"
		print "|                        10: Monstrosities                           |"
		print "|                        11: Oozes                                   |"
		print "|                        12: Plants                                  |"
		print "|                        13: Undead                                  |"
		print "|                        14: Two Classes of Humanoids                |"		
		empty(1)
		valittu = retry(valinta,1,14)
		print "|             So you want to pick the",enemy[valittu-1],"?",space(6+len(enemy[13])-len(enemy[valittu-1])),"|"
		yesno = YN()
		if yesno == 1:
			empty(1)
			return valittu
		elif yesno == 2:
			empty(1)
			valittu=menu3_ranger(1)	
			return valittu
	else:
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|          So, which familiar terrain do you want to pick?           |"
		empty(1)
		print "|                         1: Arctic                                  |"
		print "|                         2: Coast                                   |"
		print "|                         3: Desert                                  |"
		print "|                         4: Forest                                  |"
		print "|                         5: Grassland                               |"
		print "|                         6: Mountain                                |"
		print "|                         7: Swamp                                   |"
		print "|                         8: The Underdark                           |"	
		empty(1)
		valittu = retry(valinta,1,8)
		print "|             So you want to pick the",explore[valittu-1],"terrain?",space(9+len(explore[7])-len(explore[valittu-1])),"|"
		yesno = YN()
		if yesno == 1:
			empty(1)
			x=float(x)
			valittu = valittu + 0.
			valittu = valittu / 10.
			palautus = x + valittu
			return palautus
		elif yesno == 2:
			empty(1)
			valittu=menu3_ranger(2)	
			x= float(x)
			valittu = valittu + 0.
			valittu = valittu / 10.
			palautus = x + valittu
			return palautus
	
def menu3_rogue():
	prof=["2 skill proficiencies","1 skill proficiency and thieves tools"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|      The Rogue class has a choice of an expertise on a skill.      |"
	empty(1) 
	print "|     The skill or tool proficiencies that you choose will gain      |"      
	print "|             you double proficiency bonus on the skill              |"
	empty(2)
	print "|              So, which option do you want to pick?                 |"
	print "|         (the skill proficiencies will be decided later on)         |"
	empty(1)
	print "|                    1: 2 skill proficiencies                        |"
	print "|      2: 1 skill proficiency and proficiency with thieve's tools    |"
	empty(1)
	valittu = retry(valinta,1,2)
	if valittu == 1:
		print "|                 So you want to pick 2 proficiencies?               |"
	else:
		print "|  So you want to pick a skill proficiency and a tool proficiency?   |"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_rogue()	
		return valittu
	
def menu3_sorcerer(x):
	origin=["Dragonic Bloodline","Wild Magic"]
	if x == 1:
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|     The Sorcerer class has a choice of their Sorcerous origin.     |"
		empty(1) 
		print "|       The origin that you choose will affect various things.       |"      
		print "|         Please look them up from your player's handbook.           |"
		empty(2)
		print "|              So, which sorcerous origin will you pick?             |"
		empty(1)
		print "|                    1: Dragonic Bloodline                           |"
		print "|                    2: Wild Magic                                   |"
		empty(1)
		valittu = retry(valinta,1,2)
		print "|     So you want to pick the",origin[valittu-1],"as your origin?",space(5+len(origin[0])-len(origin[valittu-1])),"|"
		yesno = YN()
		if yesno == 1:
			empty(1)
			return valittu
		elif yesno == 2:
			empty(1)
			valittu=menu3_sorcerer()	
			return valittu
	else:
		races=["Black","Blue","Brass","Bronze","Copper","Gold","Green","Red","Silver","White"]
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  The Dragonic Bloodline-Sorcerer subclass has a choice of their    |"
		print "|     Dragonic ancestry, which affects some damage types of spells   |"
		empty(1)
		print "|                     1: Black                                       |"
		print "|                     2: Blue                                        |"
		print "|                     3: Brass                                       |"
		print "|                     4: Bronze                                      |"
		print "|                     5: Copper                                      |"
		print "|                     6: Gold                                        |"
		print "|                     7: Green                                       |"
		print "|                     8: Red                                         |"
		print "|                     9: Silver                                      |"
		print "|                    10: White                                       |"
		empty(1)
		valittu = retry(valinta,1,10)
		print "|                So you want to pick",races[valittu-1],"ancestry?",space(8+len(races[3])-len(races[valittu-1])),"        |"
		yesno = YN()
		if yesno == 1:
			empty(1)
			if valittu == 10:
				valittu = 1.1
			else:
				valittu = valittu + 0.
			valittu = 1. + (valittu/10)
			return valittu
		elif yesno == 2:
			empty(1)
			valittu=menu3_sorcerer(2)	
			if valittu == 10:
				valittu = 1.1
			else:
				valittu = valittu + 0.
			valittu = 1. + (valittu/10)
			return valittu		
		
def menu3_warlock():
	patron=["Archfey","Fiend","Great old one"]
	print "|--------------------------------------------------------------------|"
	empty(1)
	print "|    The Warlock class has a choice of their Otherworldy patron.     |"
	empty(1) 
	print "|       The patron that you choose will affect various things.       |"      
	print "|         Please look them up from your player's handbook.           |"
	empty(2)
	print "|          So, which otherworldy patron will you bow to?             |"
	empty(1)
	print "|                    1: The Archfey                                  |"
	print "|                    2: The Fiend                                    |"
	print "|                    3: The Great Old One                            |"
	empty(1)
	valittu = retry(valinta,1,3)
	print "|       So you want to pick the",patron[valittu-1],"as your patron?",space(8+len(patron[2])-len(patron[valittu-1])),"|"
	yesno = YN()
	if yesno == 1:
		empty(1)
		return valittu
	elif yesno == 2:
		empty(1)
		valittu=menu3_warlock()	
		return valittu

def menu4(luokka,warlockpact): #Motherfucking spellcasting on nii tyolas koodata vittu saatana
	import spells	
	if luokka in [2,3,4,10,11,12]:
		return spells.spells(luokka,warlockpact)
	else:
		return [[0],[0]]





def credits(): # tekija 
	import time
	print "|--------------------------------------------------------------------|"
	print "|         This program was created by Simo Lauerma 16D               |"
	print "|   Special thanks to the people at WoTC who created the core game   |"
	empty(1)
	time.sleep(1)
	print "|    This program is not affiliated, endorsed, or sponsored by       |"
	print "|     Wizards of the Coast or Hasbro. Dungeons & Dragons, and D&D    |"
	print "|       are registered trademarks of Wizards of the Coast.           |"
	print "|____________________________________________________________________|"
	time.sleep(10)
	mainmenu()
	
def info(): # infoa ja apua
	import time
	print "|--------------------------------------------------------------------|"
	print "|  JADACC is, as the name implies just an another character creation |"
	print "|  tool for the fifth edition of the popular tabletop roleplaying    |"
	print "|                  game Dungeons and Dragons.                        |"
	empty(1)
	print "|  It may not be the prettiest or the best one out there, but unlike |"
	print "|  all others, this is made by me, which makes it special. Kind of.  |"
	empty(2)
	print "|  I've originally made this as a student project for a programming  |"
	print "|  class, but I'm probably going to add more functionality in my     |"
	print "|  spare time. As of now (version 1.0) this tool only allows the     |"
	print "|  creation of lvl 1 characters, because of deadlines and my deadly  |"
	print "|                    habit of procrastination..                      |"
	empty(2)
	print "|   If you encounter any problems, would like to suggest changes     |"
	print "|             or just comment or talk about the project.             |"
	print "|        Feel free to contact me at simo.lauerma@protonmail.com      |"
	print "|____________________________________________________________________|"
	time.sleep(10)
	mainmenu()
