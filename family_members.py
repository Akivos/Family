class Members:
	def __init__(self, first_name, middle_name, age, hobby):
		self.first_name = first_name
		self.middle_name = middle_name
		self.age = age
		self.hobby = hobby

	@property
	def full_name(self):
		return "{} {}".format(self.first_name, self.middle_name)

	@full_name.setter
	def full_name(self, name):
		first_name, middle_name = name.split(" ")
		self.first_name = first_name
		self.middle_name = middle_name

	@full_name.deleter
	def full_name(self):
		first_name = None
		middle_name = None


	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.first_name, self.age)

	def __repr__(self):
		return f"{self.first_name} {self.middle_name} {self.age} {self.hobby}"

	def __str__(self):
		return f"{self.first_name}. Hobby - {self.hobby}"



member = Members("Shimon", "Menachem", 18, "Learning")
member.full_name = "Ayelet Hashahar"
print(member.middle_name)


