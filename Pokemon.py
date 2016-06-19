damage=10
#main class goes here
class Pokemon():
	def __init__(self,hp,_type,name):
		self.hp=hp
		self.type=_type
		self.name=name
	def gethp(self):
		return self.hp
	def gettype(self):
		return self.type
	def changehp(self,value):
		self.hp=value

#Inherited classes
class FirePokemon(Pokemon):
	def __init__(self,name,hp):
		Pokemon.__init__(self,hp,"fire",name)
	def burn(self,Pokemon):
		Pokemon.changehp(Pokemon.gethp()-damage)

class GrassPokemon(Pokemon):
	def __init__(self,name,hp):
		Pokemon.__init__(self,hp,"grass",name)
	def burn(self,Pokemon):
		Pokemon.changehp(Pokemon.gethp()-damage)

class WaterPokemon(Pokemon):
	def __init__(self,name,hp):
		Pokemon.__init__(self,hp,"water",name)
	def burn(self,Pokemon):
		Pokemon.changehp(Pokemon.gethp()-damage)