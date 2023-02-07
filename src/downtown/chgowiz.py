from area import Area, Category

#Tavern,Inn,Blacksmith,Carpenter,Woodcrafter,Chirurgeon,Drover,Jeweler,Mason,Merchant,Leathersmith,Tailor,Acater,Apothecary,Bowyer,Armorsmith,Weaponsmith,Locksmith

class Tavern(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.TAVERN, [])

class Inn(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.INN, [])
class Blacksmith(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.BLACKSMITH, [])
class Carpenter(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.CARPENTER, [])
class Woodcrafter(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.WOODCRAFTER, [])
class Chirurgeon(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.CHIRURGEON, [])
class Drover(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.DROVER, [])
class Jeweler(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.JEWELER, [])
class Mason(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.MASON, [])
class Merchant(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.MERCHANT, [])
class Leathersmith(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.TAVERN, [])
class Tailor(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.TAILOR, [])
class Acater(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.ACATER, [])
class Apothecary(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.APOTHECARY, [])
class Bowyer(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.BOWYER, [])
class Armorsmith(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.ARMORSMITH, [])
class Weaponsmith(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.WEAPONSMITH, [])
class Locksmith(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.LOCKSMITH, [])
		
	
