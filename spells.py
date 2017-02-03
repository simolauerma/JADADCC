import menu
import time
lvl1 = ["Alarm",
		"Animal Friendship",
		"Armor Of Aghatys",
		"Arms Of Hadar",
		"Bane",
		"Bless",
		"Burning Hands",
		"Charm Person",
		"Chromatic Orb",
		"Color Spray",
		"Command",
		"Comprehend Languages",
		"Create Or Destroy Water",
		"Cure Wounds",
		"Detect Evil And Good",
		"Detect Magic",
		"Detect Poison And Disease",
		"Disguise Self",
		"Dissonant Whispers",
		"Entangle",
		"Expeditious Retreat",
		"Faerie Fire",
		"False Life",
		"Feather Fall",
		"Find Familiar",
		"Fog Cloud",
		"Goodberry",
		"Grease",
		"Guiding Bolt",
		"Healing Word",
		"Hellish Rebuke",
		"Heroism",
		"Hex",
		"Identify",
		"Illusory Script",
		"Inflict Wounds",
		"Jump",
		"Longstrider",
		"Mage Armor",
		"Magic Missile",
		"Protection From Evil And Good",
		"Purify Food And Drink",
		"Ray Of Sickness ",
		"Sanctuary",
		"Shield",
		"Shield Of Faith",
		"Silent Image",
		"Sleep",
		"Speak With Animals",
		"Tasha's Hideous Laugter",
		"Tenser's Floating Disk",
		"Thunderwave",
		"Unseen Servant",
		"Witch Bolt" ]
		
lvl0 = ["Acid Splash",
		"Blade Ward",
		"Chill Touch",
		"Dancing Lights",
		"Druidcraft",
		"Eldritch Blast",
		"Fire Bolt",
		"Friends",
		"Guidance",
		"Light",
		"Mage Hand",
		"Mending",
		"Message",
		"Minor Illusion",
		"Poison Spray",
		"Prestidigitation",
		"Produce Flame",
		"Ray Of Frost",
		"Resistance",
		"Sacred Flame",
		"Shillelagh",
		"Shocking Grasp",
		"Spare The Dying",
		"Thaumaturgy",
		"Thorn Whip",
		"Thunderclap",
		"True Strike",
		"Vicious Mockery" ]


def empty(x):
	menu.empty(x)
			

	
def bard():
	numlvl1 = [2,5,8,12,14,16,18,19,22,24,30,32,34,35,38,47,48,49,50,52,53]
	numlvl0 = [2,4,8,10,11,12,13,14,16,26,27,28]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|    As you might imagine, spells are a major part of being a bard   |"
		print "|          As a bard you'll choose 4 lvl 1 spells to learn           |"
		print "|   alongside 2 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 2 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(25+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1],"and", menu.space(21+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"?", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 4 lvl 1 spells                   |"
		print "|                (input all 4 numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(18+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu3 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu4 = menu.retry(menu.valinta,1,len(wizlvl1))

		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1]," ", menu.space(16+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1]," ", menu.space(16+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		print "|                          ",wizlvl1[valittu3-1],"and", menu.space(14+max(pituuslvl1)-(pituuslvl1[valittu3-1])),"|"
		print "|                          ",wizlvl1[valittu4-1],"?", menu.space(16+max(pituuslvl1)-(pituuslvl1[valittu4-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2,valittu3,valittu4]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus


def cleric():
	numlvl1 = [5,6,11,13,14,15,16,17,29,30,36,41,42,44,46]
	numlvl0 = [9,10,12,19,20,23,24]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a cleric   |"
		print "|   As a cleric, you can cast any spells from the cleric spell list  |"
		print "|   alongside 3 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 3 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(26+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu3 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1]," ", menu.space(24+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"and", menu.space(22+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		print "|                          ",wizlvl0[valittu3-1],"?", menu.space(24+max(pituuslvl0)-(pituuslvl0[valittu3-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2,valittu3]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|     Next I'll just print all the cleric spells for you to see.     |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(12+max(pituuslvl1)-pituuslvl1[i-1]),"|"
			time.sleep(0.1)
		empty(1)
		time.sleep(3)
		
		valitut = []
		for i in range (1,len(numlvl1)+1,1):
			valitut.append(i)
		return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus

	
def druid():
	numlvl1 = [2,8,13,14,16,17,20,22,26,27,30,37,38,42,49,52]
	numlvl0 = [5,9,12,15,17,19,21,25]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a druid    |"
		print "|   As a druid, you can cast any spells from the druid spell list    |"
		print "|   alongside 2 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 2 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(28+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1],"and", menu.space(24+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"?", menu.space(26+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|     Next I'll just print all the druid spells for you to see.      |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(16+max(pituuslvl1)-pituuslvl1[i-1]),"|"
			time.sleep(0.1)
		empty(1)
		time.sleep(3)
		
		valitut = []
		for i in range (1,len(numlvl1)+1,1):
			valitut.append(i)
		return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus


def sorcerer():
	numlvl1 = [7,8,9,10,12,16,18,21,23,24,26,37,39,43,45,47,48,52,54]
	numlvl0 = [1,2,3,4,7,8,10,11,12,13,14,15,18,22,27]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a sorcerer |"
		print "|         As a sorcerer you'll choose 2 lvl 1 spells to learn        |"
		print "|   alongside 4 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 4 cantrips                    |"
		print "|                (input all 4 numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(27+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu3 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu4 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1]," ", menu.space(25+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1]," ", menu.space(25+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		print "|                          ",wizlvl0[valittu3-1],"and", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu3-1])),"|"
		print "|                          ",wizlvl0[valittu4-1],"?", menu.space(25+max(pituuslvl0)-(pituuslvl0[valittu4-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2,valittu3,valittu4]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 2 lvl 1 spells                   |"
		print "|                (input both numbers separately)                     |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(21+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))

		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1],"and", menu.space(17+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1],"?", menu.space(19+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus

	
def fey():
	numlvl1 = [3,4,8,12,21,22,31,33,35,41,48,53,54]
	numlvl0 = [2,3,6,8,11,14,15,16,27]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a warlock  |"
		print "|         As a warlock you'll choose 2 lvl 1 spells to learn         |"
		print "|   alongside 2 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 2 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(25+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1],"and", menu.space(21+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"?", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 2 lvl 1 spells                   |"
		print "|                (input both numbers separately)                     |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(12+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))

		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1],"and", menu.space(8+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1],"?", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus
	
def fiend():
	numlvl1 = [3,4,7,8,11,12,21,31,33,35,41,53,54]
	numlvl0 = [2,3,6,8,11,14,15,16,27]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a warlock  |"
		print "|         As a warlock you'll choose 2 lvl 1 spells to learn         |"
		print "|   alongside 2 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 2 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(25+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1],"and", menu.space(21+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"?", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 2 lvl 1 spells                   |"
		print "|                (input both numbers separately)                     |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(12+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))

		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1],"and", menu.space(8+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1],"?", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus
	
def old_one():
	numlvl1 = [3,4,8,12,19,21,31,33,35,41,50,53,54]
	numlvl0 = [2,3,6,8,11,14,15,16,27]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a warlock  |"
		print "|         As a warlock you'll choose 2 lvl 1 spells to learn         |"
		print "|   alongside 2 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 2 cantrips                    |"
		print "|                 (input both numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(25+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1],"and", menu.space(21+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"?", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 2 lvl 1 spells                   |"
		print "|                (input both numbers separately)                     |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(12+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))

		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1],"and", menu.space(8+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1],"?", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus

	
def wizard():
	numlvl1 = [1,7,8,9,10,12,16,18,21,23,24,25,26,28,34,35,37,38,39,40,41,43,45,47,48,50,51,52,53,54]
	numlvl0 = [1,2,3,4,7,8,10,11,12,13,14,15,16,18,22,27]
	wizlvl1 = []
	wizlvl0 = []
	for i in range (0,len(numlvl1),1):
		wizlvl1.append(lvl1[numlvl1[i]-1])
	for i in range (0,len(numlvl0),1):
		wizlvl0.append(lvl0[numlvl0[i]-1])
	
	pituuslvl1 = []
	pituuslvl0 = []
	for i in range (0,len(wizlvl1),1):
		pituuslvl1.append(len(wizlvl1[i]))
	for i in range (0,len(wizlvl0),1):
		pituuslvl0.append(len(wizlvl0[i]))
	
	def cantripvalinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                            Spellcasting                            |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|  As you would imagine, spells are a major part of being a wizard   |"
		print "|  As a wizard you'll choose 6 lvl1 spells to add to your spellbook  |"
		print "|   alongside 3 so called cantrips that can be used anytime anywhere |"
		empty(1)
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|                First let's pick your 3 cantrips                    |"
		print "|                (input all 3 numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl0)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl0[i-1],menu.space(25+max(pituuslvl0)-pituuslvl0[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl0))
		valittu3 = menu.retry(menu.valinta,1,len(wizlvl0))
	
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl0[valittu1-1]," ", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu1-1])),"|"
		print "|                          ",wizlvl0[valittu2-1],"and", menu.space(21+max(pituuslvl0)-(pituuslvl0[valittu2-1])),"|"
		print "|                          ",wizlvl0[valittu3-1],"?", menu.space(23+max(pituuslvl0)-(pituuslvl0[valittu3-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1, valittu2, valittu3]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=cantripvalinta()
			return valitut
			
	def lvl1valinta():
		print "|--------------------------------------------------------------------|"
		empty(1)
		print "|              Next we'll pick your 6 lvl 1 spells                   |"
		print "|                (input all 6 numbers separately)                    |"
		empty(1)
		for i in range (1,len(numlvl1)+1,1):
			print "|",menu.space(25-len(str(i))),str(i)+":",wizlvl1[i-1],menu.space(12+max(pituuslvl1)-pituuslvl1[i-1]),"|"
		valittu1 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu2 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu3 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu4 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu5 = menu.retry(menu.valinta,1,len(wizlvl1))
		valittu6 = menu.retry(menu.valinta,1,len(wizlvl1))
		
		print "|                        So do you want to pick:                     |"
		empty(1)
		print "|                          ",wizlvl1[valittu1-1]," ", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu1-1])),"|"
		print "|                          ",wizlvl1[valittu2-1]," ", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu2-1])),"|"
		print "|                          ",wizlvl1[valittu3-1]," ", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu3-1])),"|"
		print "|                          ",wizlvl1[valittu4-1]," ", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu4-1])),"|"
		print "|                          ",wizlvl1[valittu5-1],"and", menu.space(8+max(pituuslvl1)-(pituuslvl1[valittu5-1])),"|"
		print "|                          ",wizlvl1[valittu6-1],"?", menu.space(10+max(pituuslvl1)-(pituuslvl1[valittu6-1])),"|"
		empty(1)
		yesno = menu.YN()
		valitut = [valittu1,valittu2,valittu3,valittu4,valittu5,valittu6]
		if yesno == 1:
			empty(1)
			return valitut
		elif yesno == 2:
			empty(1)
			valitut=lvl1valinta()
			return valitut
	
	palautus = [cantripvalinta(),lvl1valinta()]
	return palautus
	
classit = { 2:bard , 3:cleric , 4:druid , 10:sorcerer , 12:wizard}
patronit = { 1:fey , 2:fiend , 3:old_one }


def spells(luokka,warlockpact):
	if luokka == 11:
		return patronit[warlockpact]()
	else:
		return classit[luokka]()
