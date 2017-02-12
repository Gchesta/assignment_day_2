import unittest
from recruit import Recruit, ServiceMan, GsoCadet, SoCadet, Constabulary
class TestRecruitClasses(unittest.TestCase):
	#testing the exceptions to be raised in Recruit Class
	def test_if_name_is_alphabets_only(self):
		self.assertRaises(Exception, Recruit, "George Nyongesa23", 21, 25896536, 11122256)

	def test_if_age_is_digits_only(self):
		self.assertRaises(Exception, Recruit, "George Nyongesa", "d21", 25896536, 11122256)

	def test_if_national_id_is_digits_only(self):
		self.assertRaises(Exception, Recruit,"George Nyongesa", 21, "2s896536", 11122256)

	def test_if_military_id_is_digits_only(self):
		self.assertRaises(Exception, Recruit, "George Nyongesa", 21, 28965436, "11d22256")

	def test_if_national_id_length_is_8_digits(self):
		self.assertRaises(Exception, Recruit, "George Nyongesa", 21, 289688536, 11122256)

	def test_if_military_id_length_is_8_digits(self):
		self.assertRaises(Exception, Recruit, "George Nyongesa", 21, 28968853, 896536)

	#Testing the exceptions to be raised in the Serviceman sublcass

	def test_serviceman_age(self):
		self.assertRaises(Exception, ServiceMan, "George Nyongesa", 26, 289688536, 28968536, "c-")

	def test_serviceman_grade(self):
		self.assertRaises(Exception, ServiceMan, "George Nyongesa", 20, 289688536, 28965036, "d-")

	#testing the values returned in the Servieman class
	def test_serviceman_skills(self):
		serviceman_skills = ["Teamworking", "Communication", "Act Fast", "Rapid Response", "Understand & Follow Instructions"]
		george = ServiceMan("George Nyongesa", 22, 28885346, 28965366, "C-")
		self.assertEqual(serviceman_skills, george.skills())

	def test_serviceman_skills(self):
		serviceman_equipment = ["9-Month Basic Training", "Service Uniform", "M16 Rifles"]
		george = ServiceMan("George Nyongesa", 22, 28688536, 28965366, "C-")
		self.assertEqual(serviceman_equipment, george.equip())

	#Testing the exceptions to be raised in the General service Officer sublcass

	def test_general_service_cadet_age(self):
		self.assertRaises(Exception, GsoCadet, "George Nyongesa", 29, 28968836, 28966536, "A")

	def test_serviceman_grade(self):
		self.assertRaises(Exception, GsoCadet, "George Nyongesa", 23, 28968536, 28976536, "D-")

	#testing the values returned in the General service officer cadet class
	def test_general_service_cadet_skills(self):
		gso_cadet_skills = ["Teamworking", "Leadership" "Communication", "Act Fast", "Rapid Response", "Understand & Follow Instructions", "Analytical"]
		george = GsoCadet("George Nyongesa", 22, 28688536, 28965366, "A")
		self.assertEqual(gso_cadet_skills, george.skills())

	def test_general_service_cadet_equipment(self):
		gso_cadet_equipment = ["9-Month Basic Training", "BSC, Military Science", "Service Uniform", "M16 Rifle"]
		george = GsoCadet("George Nyongesa", 22, 28688536, 28965366, "A")
		self.assertEqual(gso_cadet_equipment, george.equip())

	#Testing the exceptions to be raised in the Specialist service Officer sublcass

	def test_specialist_service_cadet_age(self):
		self.assertRaises(Exception, SoCadet, "George Nyongesa", 52, 28968836, 28965376, "Doctor")

	def test_specialist_profession(self):
		self.assertRaises(Exception, SoCadet, "George Nyongesa", 27, 28968536, 28965365, "Watchman")

	#testing the values returned in the specialist service officer cadet class
	def test_specialist_service_cadet_skills(self):
		sso_cadet_skills = ["Teamworking", "Leadership" "Communication", "Act Fast", "Growth Mindset" "Problem Solving", "Analytical", "Creative"]
		george = SoCadet("George Nyongesa", 27, 28688536, 28965366, "Doctor")
		self.assertEqual(sso_cadet_skills, george.skills())

	def test_specialist_service_cadet_equipment(self):
		sso_cadet_equipment = ["9-Month Basic Training", "Service Uniform", "Professional Membership"]
		george = SoCadet("George Nyongesa", 27, 28688536, 28965366, "Nurse")
		self.assertEqual(sso_cadet_equipment, george.equip())

	#Testing the exceptions to be raised in the constabulary sublcass

	def test_constabulary_age(self):
		self.assertRaises(Exception, Constabulary, "George Nyongesa", 22, 28968836, 28965376, 5)

	def test_constabulary_experience(self):
		self.assertRaises(Exception, Constabulary, "George Nyongesa", 31, 28968536, 28965365, 1)

	#testing the values returned in the specialist service officer cadet class
	def test_constabulary_skills(self):
		constabulary_skills = ["Communication", "Act Fast", "Attention To Detail", "Understand & Follow Instructions"]
		george = Constabulary("George Nyongesa", 31, 28688536, 28965366, 5)
		self.assertEqual(constabulary_skills, george.skills())

	def test_constabulary_equipment(self):
		constabulary_equipment = ["Refresher Training", "Service Uniform", "M16 Rifle"]
		george = Constabulary("George Nyongesa", 31, 28688536, 28965366, 5)
		self.assertEqual(constabulary_equipment, george.equip())

if __name__ == "__main__":
    unittest.main()
