class Recruit(object):
	"""
	A program designed for the Kenya Defence Forces that will be used to take in new recruits into the army

	"""
	
	def __init__(self, full_name, age, national_id, military_id):
		"""A function to initialize the new recruit"""
		self.full_name = full_name #full_name of recruit
		self.age = age #age f recruit
		self.national_id = national_id #recruits national id
		self.military_id = military_id
		compact_name = "".join(full_name.split())

		#checking validity of enries
		if not (compact_name).isalpha():
			raise TypeError("Names MUST contain ONLY alphabetic charaters")

		elif not str(self.age).isdigit():
			raise TypeError("The age MUST contain ONLY characters 0 - 9")

		elif not str(self.national_id).isdigit():
			raise TypeError("The national ID MUST contain ONLY characters 0 - 9")

		elif not str(self.military_id).isdigit():
			raise TypeError("The military ID MUST contain ONLY characters 0 - 9")

		elif len(str(self.military_id)) != 8 or len(str(national_id)) != 8:
			raise ValueError("zThe length of the national/military ID MUST be 8 digits")

		elif self.age < 18:
			raise ValueError("A recruit cannot be less than 18 years old")
				
class ServiceMan(Recruit):
	"""setting up a new ServiceMan - employing inheritance"""
	def __init__(self, full_name, age, national_id, military_id, grade):
		Recruit.__init__(self, full_name, age, national_id, military_id)

		self.grade = grade.upper()
		allowed_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+"]
		
		if self.age > 22:
			raise ValueError("A serviceman cannot be more than 22 years old")

		elif self.grade not in allowed_grades:

			raise ValueError("A serviceman should have scored at least D+ and above in KCSE")

	def skills(self): 
		#Demonstrating polymorphism
		"""These are the skills that are required of a serviceman"""
		return ["Teamworking", "Communication", "Act Fast", "Rapid Response", "Understand & Follow Instructions"]

	def equip(self): 
		#Demonstrating polymorphism
		"""Equipping the serviceman"""
		return ["9-Month Basic Training", "Service Uniform", "M16 Rifles"]

class GsoCadet(Recruit):
	"""setting up a new General Service Officer Cadet - employing inheritance"""
	def __init__(self, full_name, age, national_id, military_id, grade):
		Recruit.__init__(self, full_name, age, national_id, military_id)

		self.grade = grade.upper()
		allowed_grades = ["A", "A-", "B+", "B"]

		if self.age > 26:
			raise ValueError("A General Service Officer Cadet cannot be more than 26 years old")

		elif self.grade not in allowed_grades:

			raise ValueError("A General Service Officer Cadet should have scored at least B and above in KCSE")

	def skills(self):
		"""These are the skills that are required of a general serivce officer cadet"""
		return ["Teamworking", "Leadership" "Communication", "Act Fast", "Rapid Response", "Understand & Follow Instructions", "Analytical"]
	
	def equip(self): 
		#Demonstrating polymorphism
		"""Equipping the GSO Cadet"""
		return ["9-Month Basic Training", "BSC, Military Science", "Service Uniform", "M16 Rifle"]
	
class SoCadet(Recruit):
	"""setting up a new Specialist Officer Cadet - employing inheritance"""
	def __init__(self, full_name, age, national_id, military_id, profession):
		Recruit.__init__(self, full_name, age, national_id, military_id)
		self.profession = profession
		needed_professions = ["Doctor", "Nurse", "Chaplain", "Clinical Officer", "Engineer"]

		if self.age > 29:
			raise ValueError("A Specialist Officer Cadet cannot be more than 29 years old")

		elif self.profession not in needed_professions:
			raise ValueError("Too bad. We currently don't have any need for " + self.profession)

	def skills(self):
		"""These are the skills that are required of a specialist officer cadet"""
		return ["Teamworking", "Leadership" "Communication", "Act Fast", "Growth Mindset" "Problem Solving", "Analytical", "Creative"]

	def equip(self): 
		#Demonstrating polymorphism
		"""Equipping the SO Cadet"""
		return ["9-Month Basic Training", "Service Uniform", "Professional Membership"]

class Constabulary(Recruit):
	"""setting up a new Specialist Officer Cadet - employing inheritance"""
	def __init__(self, full_name, age, national_id, military_id, experience):
		Recruit.__init__(self, full_name, age, national_id, military_id)

		self.experience = experience

		if self.age < 30 or self.age > 49:
			raise ValueError("A constabulary must be between 30 and 49 years of age")

		elif self.experience < 3:
			raise ValueError("A constabulary must have at least 3 years worth of experince in the KDF")

	def skills(self):
		"""These are the skills that are required of a constabulary"""
		return ["Communication", "Act Fast", "Attention To Detail", "Understand & Follow Instructions"]

	def equip(self): 
		#Demonstrating polymorphism
		"""Equipping the SO Cadet"""
		return ["Refresher Training", "Service Uniform", "M16 Rifle"]
			
