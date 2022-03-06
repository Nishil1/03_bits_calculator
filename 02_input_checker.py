# checks users choice is integer, text or image
def user_choice():

	valid = True 
	while valid:
		response = input("File type (integer / text/ image): ").lower()  
		
		text_ok = ["text", "t", "txt"]
		integer_ok = ["integer", "int", "#", "number"]
		image_ok = ["image", "img", "pix", "picture", "pic"]

		if response in text_ok:
			return "text"
		elif response in integer_ok:
			return "integer"
		elif response in image_ok:
			return "image"
		elif response == "i":
			want_integer = input("Press <enter> for an integer or any key for image")
			if want_integer == "":
				return "integer"
			else:
				return "image"



		else:
			print("Please choose a valid file type!")
			print()



# Manin routine goes here
keep_going = ""
while keep_going == "":
	
	print("You chose file type: ", user_choice())  
	print()																						