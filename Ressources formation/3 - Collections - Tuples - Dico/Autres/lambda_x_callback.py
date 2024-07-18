names = ["nathan", "jules", "jerome", "lisa"]

def convert_and_print_list(list_str: list, print_function):
    converted_list = map(lambda word: word.upper(), list_str)
    print_function(converted_list)

def print_list(list_to_print):
    for element in list_to_print:
        print(element)
        
convert_and_print_list(names, print_list)