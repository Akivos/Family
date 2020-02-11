import unittest
from family_members import Members 
from family_members import Parent


member1 = Members("Meir", "Shneior", 24, "Soccer")
member2 = Members("Akiva", "Nissim", 22, "Music")
dad = Parent("Zion", "Saaid", 52, "Science")
mom = Parent("Sharon", "Elisheva", 50, "Reading")
dad.add_kid(member1.full_name)
mom.add_kid(member2.full_name)

class TestFamily(unittest.TestCase):

	def setUp(self):
		self.member1 = member1
		self.member2 = member2
		self.dad = dad
		self.mom = mom

	def test_firtsname(self):
		self.assertEqual(self.member1.first_name, "Meir")
		self.assertEqual(self.member2.first_name, "Akiva")

	def test_middlename(self):
		self.assertEqual(self.member1.middle_name, "Shneior")
		self.assertEqual(self.member2.middle_name, "Nissim")

	def test_age(self):
		self.assertEqual(self.member1.age, 24)
		self.assertEqual(self.member2.age, 22)

	def test_hobby(self):
		self.assertEqual(self.member1.hobby, "Soccer")
		self.assertEqual(self.member2.hobby, "Music")

	def test_fullname(self):
		self.assertEqual(self.member1.full_name, "Meir Shneior")
		self.assertEqual(self.member2.full_name, "Akiva Nissim")

	def test_email(self):
		self.assertEqual(self.member1.email, "Meir.24@gmail.com")
		self.assertEqual(self.member2.email, "Akiva.22@gmail.com")
		self.assertEqual(self.dad.email, "Zion.52@gmail.com")

	def test_similar(self):
		self.assertEqual(self.dad.similar_kids, ["Meir Shneior"])
		self.assertEqual(self.mom.similar_kids, ["Akiva Nissim"])




if __name__ == "__main__":
	unittest.main()







