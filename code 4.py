def unlock_vault(clues :list) -> str:
    '''
    this program is created to unlock the answer by taking each clues' first letter from the very first to end
    '''

    final_ans = ""
    while clues != "":
        final_ans += clues[0]
        clues = input()
    return final_ans

text = input("Enter the elemets of the list : (tap void enter to exit)\n")
print(unlock_vault(text))