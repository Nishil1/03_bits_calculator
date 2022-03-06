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

  


def image_bits():

	image_width = num_check("Image Width? ", 1)
	image_height = num_check("Image Height? ", 1)

	num_pixels = image_width * image_height
	num_bits = num_pixels * 24

	print()
	print("# of pixels = {} * {} = {}". format(image_height, image_width, num_pixels))
	print("# of bits = {} * 24 = {}".format (num_pixels, num_bits))

	image_bits()




