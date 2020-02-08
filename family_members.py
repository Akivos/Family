class Members:
	def __init__(self, first_name, middle_name, age, hobby):
		self.first_name = first_name
		self.middle_name = middle_name
		self.age = age
		self.hobby = hobby

	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.first_name, self.age)

	def __repr__(self):
		return f"{self.first_name}{self.middle_name}{self.age}{self.hobby}"

	def __str__():
		return f"{self.first_name}. Hobby - {self.hobby}"



