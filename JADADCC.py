import time
import menu





menu.mainmenu()

valinta = menu.retry(menu.valinta(),1,4)
while valinta in range (1,5,1):	
	if valinta == 4:
		menu.end()
		quit()
	if valinta == 3:
		menu.credits()
		valinta=menu.valinta()
	if valinta == 2:
		menu.info()
		valinta=menu.valinta()
	if valinta == 1:
		menu.menu1()
		valinta = 0

noppavairandom = menu.retry(menu.valinta(),1,2)
if noppavairandom == 1:
	allstats=menu.menu1_1()
if noppavairandom == 2:
	allstats=menu.menu1_2()

abilityscore = menu.menu2(allstats)
abilitymod = menu.menu2_1(abilityscore)
time.sleep(2)

rotu=[]
rotu.append(menu.menu3_1())

alirodut=[1,2,3,5,6]
if rotu[0] in alirodut:
	rotu.append(menu.menu3_1_2(rotu[0]))
else:
	rotu.append(1)	
	
tausta=[]
tausta.append(menu.menu3_2())

luokka=[]
luokka.append(menu.menu3_3())
if luokka[0] == 5:
	temp = menu.menu3_ranger(menu.menu3_ranger(0))

elif luokka[0] == 10:
	temp = menu.menu3_sorcerer(1)
	if temp == 1:
		temp = menu.menu3_sorcerer(2)	
		
else:
	luokka.append(menu.menu3_3_2(luokka[0]))

if luokka[0] == 11:	
	taiat = menu.menu4(luokka[0],luokka[1])
else:
	taiat = menu.menu4(luokka[0],[0])


