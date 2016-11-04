# students = [
# 	 {'first_name' : 'Michael', 'last_name' : 'Jordan'},
# 	 {'first_name' : 'John', 'last_name' : 'Rosales'},
# 	 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	 {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for num in students:
# 	print num['first_name'], num['last_name']

users = {
	'Students': [ 
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	],
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'}
	]
}

for key, data in users.items():
	print key
	count=0
	for value in data:
		count+= 1
		print count, '-', value['first_name'], value['last_name'], '-', len(value['first_name'])+len(value['last_name'])


# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13