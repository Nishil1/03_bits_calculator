# checks input is a number more than 0

def num_check(question, low):
	valid = False
	while not valid:
		
		error=" please enter an integer that is more than or equal to {}".format(low)
		
		try: 
			# ask user to enter a number

			response = int(input(question))
			
			# check if the number is more than 0
			
			if response >= low:
				return response  

			#outputs error if the input is invalid

			else:
				print(error)
				print()
		except ValueError: 
			print(error)
			

keep_going = ""
while keep_going == "":
	print()

	var_integer = num_check("Enter an integer: ", 0)
	print()

	image_width = num_check("Image width: ", 1)
	print()
	image_height = num_check("Image height: ", 1)
			
			
			
			
			
			

