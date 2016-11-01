# print "Hello World"

# my_string = "hello world"
# print my_string.find("el")

# for count in range(0,5):
# 	print "looping - ", count

# def evens_odds(a,b):
# 	count = 1
# 	for count in range(a,b):
# 		if count % 2 != 0:
# 			print "Number is ", count 
# 			print "The number is odd."
# 		if count % 2 == 0:
# 			print "Number is ", count
# 			print "The number is even."
# print evens_odds(1,2001)


# a = [2,4,10,16]
# def multiply(arr):
#     for i in range(len(arr)):
#         arr[i] = arr[i] * 5
#     return arr

# b = multiply(a)
# print b
# for i in range(1,2001):
#     if i % 2 == 0:
#         print 'Number is ' + str(i) + '. This is an odd number.'
#     else:
#         print 'Number is ' + str(i) + '. This is an even number.'


# def scores_grades(arr):
# 	for i in range(len(arr)):
# 		if(arr[i]>= 60 and arr[i] <= 69):
# 			print 'Score: ' + str(arr[i]) + '. Your grade is D.'
# 		if(arr[i]>= 70 and arr[i] <= 79):
# 			print 'Score: ' + str(arr[i]) + '. Your grade is C.'
# 		if(arr[i]>= 80 and arr[i] <= 89):	
# 			print 'Score: ' + str(arr[i]) + '. Your grade is B.'
# 		if(arr[i]>= 90 and arr[i] <= 100):
# 			print 'Score: ' + str(arr[i]) + '. Your grade is A.'
# print scores_grades([87, 67, 95, 100, 75, 90, 89, 72, 60, 89])

# from random import randint

# print "Scores and Grades"
# for count in range(0, 10):
# 	score = randint(70, 100)

# 	if(score <= 70):
# 		grade = "D"
# 	elif(score <= 80):
# 		grade = "C"
# 	elif(score <= 90):
# 		grade = "B"
# 	else:
# 		grade = "A"

# 	print "Score: %d; Your grade is %s" %(score, grade)

# print "End of program. Bye!"

		
# x = [4,6,1,3,5,7,25]
# def draw_starsI(num_list):
#     for num in num_list:
#         output = ''
#         for i in range(num):
#             output += '*'
#         print output 

# draw_stars2(x)

# y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
# def draw_stars2(my_list):
#     for item in my_list:
#         output = ''
#         if type(item) is int:
#             for i in range(item):
#                 output += '*'
#         elif type(item) is str:
#             first_letter = item[0].lower()
#             for i in range(len(item)):
#                 output += first_letter
#         print output

# draw_stars2(y)


# import random
# import math

# print 'Starting the program'

# head_count = 0
# tail_count = 0
# for i in range(1,5001):
#     rand = round(random.random())  
#     if rand == 0:
#         face = 'tail'
#         tail_count += 1
#     else:
#         face = 'head'
#         head_count += 1
#     print "Attempt #"+str(i)+": Throwing a coin...It's a "+face+"!...Got "+str(head_count)+" head(s) and "+str(tail_count)+" tail(s) so far"

# print 'Ending the program, thank you!'


my_students =  [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


for blah in my_students:
	print blah["first_name"], blah["last_name"]


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
 
for key, value in users.iteritems():
	print (key)
	for idx, person in enumerate(value):
		print("{} - {}{} - {}".format(idx + 1, person["first_name"], person["last_name"], len(person["first_name"]+person["last_name"])))

#BUBBLE SORT
def bubbleSort(arr):
	for n in range(len(arr)-1,0,-1):
		for i in range(n):
			if arr[i]>arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i+1]= temp
arr = [34, 35, 79, 1, 4, 55]
bubbleSort(arr)
print(arr)



