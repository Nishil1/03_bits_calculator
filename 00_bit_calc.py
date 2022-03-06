# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five chracters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends) 

    print()
    print(statement)
    print()

    return ""

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


# Main routine goes here

statement_generator("Bit calculator for integers, text & images", "-")

keep_going = ""
while keep_going == "":
	data_type = user_choice()
	print("You chose", data_type)



