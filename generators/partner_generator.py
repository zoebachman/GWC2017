#could change this so that it asks for user input into how many people are in each group
#would probs use modulo

import random

list_of_students = ["Aditi Dam", "Afroza Akther", "Ananya Hajra", "Andrea Ortiz","Anjana Thomas","Ariana Berry","Ashley Lagares","Caitlin Hall","Cemre Tugcu","Christine Na","Debbie Rogelberg","Iesha James","Iliana Cardenales","Jasmyne Roberts","Michelle Li","Nicole Avidon","nour Desouki","Ria Jaisinghani","Uzma Kapadia","Bethany Isabel Barber"]


while len(list_of_students) > 0:

	student1 = random.choice(list_of_students)
	student2 = random.choice(list_of_students)

	if student1 != student2:
		list_of_students.remove(student1)
		list_of_students.remove(student2)
		print student1 +", " + student2

	
