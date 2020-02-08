import unittest
from family_members import Members

class TestFamily(unittest.TestCase):

	def setUp(self):
		self.member1 = Members("Meir", "Shneior", 24, "Soccer")
		self.member2 = Members("Akiva", "Nissim", 22, "Music")

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

	def test_email(self):
		self.assertEqual(self.member1.email, "Meir.24@gmail.com")
		self.assertEqual(self.member2.email, "Akiva.22@gmail.com")






if __name__ == "__main__":
	unittest.main()


