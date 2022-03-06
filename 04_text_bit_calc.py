def text_bits():


    print()

    var_text = input("Enter some text: ")
    var_lenght = len(var_text)
    num_bits = 8 * var_lenght 

    print()
    print("\'{}\' has {} chracters...".format(var_text, var_lenght))
    print("# of bits is {} * 8...".format(var_lenght))
    print("We need {} of bits to represent {}".format(num_bits, var_text))
    print()

    return ""

text_bits()


    
    




