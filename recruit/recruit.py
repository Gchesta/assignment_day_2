class Recruit(object)
:	"""
	A program designed for the Kenya Defence Forces that will be used to take in new recruits into the army

	"""
	
	
	def __init__(self, full_name, age, national_id, military_id):
		"""A function to initialize the new recruit"""
		
		self.full_name = full_name #full_name of recruit
		self.age = age #age f recruit
		self.national_id = national_id #recruits national id
		
	
	def __hiv_scholarship(self, amount):
		"""setting a private method to make use of encapsulation"""
		self.amount = amount
		
 class Prefect(Student):
	"""setting up a new prefect - employing inheritance"""
	def __init__(self, admin_num, name, kcpe_marks, age, hostel, stream, former_school, reward_points=0, rank):
		Student.__init__(self, admin_num, name, kcpe_marks, age, hostel, stream, former_school, reward_points=0 )
		self.rank = rank
		
		
	