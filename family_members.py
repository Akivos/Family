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

class Parent(Members):
	def __init__(self, first_name, middle_name, age, hobby, similar_kids=None):
		super().__init__(first_name, middle_name, age, hobby)
		if similar_kids is None:
			self.similar_kids = []
		else:
			self.similar_kids = similar_kids

	def add_kid(self, kid):
		if kid not in self.similar_kids:
			self.similar_kids.append(kid)

	def remove_kid(self, kid):
		if kid in self.similar_kids:
			self.similar_kids.remove(kid)

	def print_kids(self):
		for kid in self.similar_kids:
			print(kid.full_name)

member1 = Members("Meir", "Shneior", 24, "Soccer")
dad = Parent("Zion", "Saaid", 52, "Science")
dad.add_kid(member1)
dad.print_kids()
