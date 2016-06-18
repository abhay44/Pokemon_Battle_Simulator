import random
from Pokemon import FirePokemon,GrassPokemon,WaterPokemon
print 'Welcome to Pokemon Battle :D\nYou wanna support Trainer1 or Trainer2?'
user_input=str(raw_input())
pokemons_trainer1=['growlithe','gogoat','popplio']
pokemons_trainer2=['charmander','skiddo','clauncher']
trainer1_count=0
trainer2_count=0
trainer1=[]
trainer2=[]
for i in range(0,3):
	trainer1.append(random.choice(pokemons_trainer1))
for i in range(0,3):
	trainer2.append(random.choice(pokemons_trainer2))
if not (user_input == "Trainer1"  or user_input == "Trainer2"):
	print 'Please select Trainer1 or Trainer2 -_-'
	
else:
	for i in range(0,3):
		growlithe=FirePokemon('fire',100)
		gogoat=GrassPokemon('grass',80)
		popplio=WaterPokemon('water',50)
		charmander=FirePokemon('fire',70)
		skiddo=GrassPokemon('grass',90)
		clauncher=WaterPokemon('water',60)
		print 'Trainer1 picks ' + trainer1[i] + ' and Trainer2 picks ' + trainer2[i]
		while eval(trainer1[i]).gethp()>0 and eval(trainer2[i]).gethp()>0:
			eval(trainer1[i]).burn(eval(trainer2[i]))
			print str(trainer1[i]) + ' attacks ' + str(trainer2[i])
			print  '%s hp is: ' % trainer1[i] + str(eval(trainer1[i]).gethp())
			print  '%s hp is: ' % trainer2[i] + str(eval(trainer2[i]).gethp())
			eval(trainer2[i]).burn(eval(trainer1[i]))
			print str(trainer2[i]) + ' attacks ' + str(trainer1[i])
			print  '%s hp is: ' % trainer1[i] + str(eval(trainer1[i]).gethp())
			print  '%s hp is: ' % trainer2[i] + str(eval(trainer2[i]).gethp())
		if eval(trainer1[i]).gethp()>eval(trainer2[i]).gethp():
			trainer1_count+=1
			print trainer1[i].upper() + ' WON'
		else:
			trainer2_count+=1
			print trainer2[i].upper() + ' WON'
		print "----------------------------"
if trainer1_count>trainer2_count and (user_input=='Trainer1'):
	print 'Trainer1 Won the battle!! :D'
elif trainer1_count<trainer2_count and (user_input=='Trainer2'):
	print 'Trainer2 Won the battle!! :D'
elif trainer1_count>trainer2_count and (user_input=='Trainer2'):
	print 'Trainer1 Won the battle!! Better luck next time :('
elif trainer1_count<trainer2_count and (user_input=='Trainer1'):
	print 'Trainer2 Won the battle!! Better luck next time :('



