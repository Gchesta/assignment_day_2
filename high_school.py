class Student(object):
	"""a school program that has been designed to create new students in a school
		
	The attributes of a new student in Form 1 are:
	
	1. Admission Number 2. Name 3. KCPE Marks 4. Age 5. Hostel 6 Stream 7. Reward points"""
	
	
	def __init__(self, admin_num, name, kcpe_marks, age, hostel, stream, former_school, reward_points=0 ):
		"""A funtion to initialize the new student"""
		
		self.admin_num = admin_num #student admission number
		self.name = name #student name
		self.kcpe_marks = kcpe_marks #a student's KCPE marks
		self.age = age #student age
		self.hostel = hostel #student's allocated hostel
		self.stream = stream #students allocated 
		self.former_school = former_school #the name of the student's fomer school
		self.reward_points = reward_points #reward points based on the behavior of student in school
	
	def __hiv_scholarship(self, amount):
		"""setting a private method to make use of encapsulation"""
		self.amount = amount
		
 class Prefect(Student):
	"""setting up a new prefect - employing inheritance"""
	def __init__(self, admin_num, name, kcpe_marks, age, hostel, stream, former_school, reward_points=0, rank):
		Student.__init__(self, admin_num, name, kcpe_marks, age, hostel, stream, former_school, reward_points=0 )
		self.rank = rank
		
		
	