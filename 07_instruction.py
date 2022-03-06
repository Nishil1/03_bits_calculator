def statement_generator(text, decoration):

    # Make string with five chracters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends) 

    print()
    print(statement)
    print()

    return ""




def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image/text/integer)")
    print()
    print("This program assumes that images are being represents in 24 bit colour (ie: 24 bits per pixel). For text we assume that ascii encoding is being used(8 bits per character.)")
    print()
    print("Complete as many calculations as nessacary, press <enter> at the end of each calculation or any key to quit")
    print()
    return ""

instructions () 