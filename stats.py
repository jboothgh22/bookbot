import string

def count_words(the_text):
    wordz = the_text.split()
    
    the_count = len(wordz)
    return the_count

def count_characters(the_text):
    # This will count the individual letter occurences
   
    the_alphabet = string.ascii_lowercase

    char_count_dict = {}

    the_new_text = the_text.lower()
    
    for the_char in the_alphabet:
        n_char = the_new_text.count(the_char)
        char_count_dict[the_char] = n_char
        

    return char_count_dict

def sorted_list(input_dict):
    # This will take the input dictionary of letters and
    # number of their occurences and make a new
    # list of dictionaries: [{'char':'a', 'num':10}, 
    #                              {'char':'b', 'num':3}...]
    #
    my_list = []

    # Read through the dictionary and make a list of 
    # dictionaries with the keys "char" and "num"
    for key, val in input_dict.items():
        
        my_list.append({"char":key, "num":val})

    # Sort this list by the "num" key and report them in reverse 
    # numerical order
    my_sorted_list = sorted(my_list, key = lambda d: d['num'] ,reverse = True )
    
    return my_sorted_list
