class Student(object):
	"""a school program that has been designed to show the total 
	number of students in a school. It is also meant to carter for any admissions
	and expusions
	
	The attributes of a new student in Form 1 are:
	
	1. Admission Number 2. Name 3. KCPE Marks 4. Age 5. Hostel 6 Stream"""
	
	total_students = 0 #setting the initial student population at 0
	
	def __init__(self, admin_num, name, kcpe_marks, age, hostel, stream ):
		"""A funtion to initialize the new student"""
		
		self.admin_num = admin_num #student admission number
		self.name = name #student name
		self.kcpe_marks = kcpe_marks #a student's KCPE marks
		self.age = age #student age
		self.hostel = hostel #student's allocated hostel
		self.stream = stream #students allocated 
	
	