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

def int_bits():

	var_integer = num_check("Please enter an integer: ", 0)

	var_binary = "{0:b}".format (var_integer)

	num_bits = len(var_binary)

	print()
	print("{} in binary is {}".format(var_integer, var_binary))
	print("# of bits is {}".format(num_bits))
	print()

	return ""

int_bits()