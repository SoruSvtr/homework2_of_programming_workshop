from string import punctuation

def Ispunctuation_str(str) -> bool:
    punct = set(punctuation)
    if any(char in punct for char in str):
        return True
    return False

def Ismixed_up_down(str) -> bool:
    letters = set(str)
    mixed = any(letter.islower() for letter in letters) and any(letter.isupper() for letter in letters)
    if mixed:
        return True
    return False

def check_pass(people):
    for username, password in people:
        if len(password) >= 8 and Ispunctuation_str(password) and Ismixed_up_down(password):
            print(username)

final_list = [] 
line = input("Enter the list of tuples (tap enter to exit):\n") 
while line != "": 
    final_list.append(tuple(line.split())) 
    line = input() 
 
check_pass(final_list)