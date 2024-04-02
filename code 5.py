from random import randint
from time import time

def int2bin(integer : int) -> str:
    binary = bin(integer)
    if integer <= 1:
        zero_str = "000"
    elif integer > 1 and integer < 4:
        zero_str = "00"
    elif integer >= 4 and integer < 8:
        zero_str = "0"
    else:
        zero_str = ""
    return zero_str + binary[2:]

def exam_numbers():
    start = time()
    print("You have 20 seconds to answer")
    ans_stat = []
    while time() - start < 20:
        num = randint(0, 15)
        print(int2bin(num))
        try:
            guess_num = int(input())
            if guess_num == num:
                ans_stat.append("True")
            else:
                ans_stat.append("False")
        except ValueError:
            print("whether you didn't enter any value or a wrong one please enter an integer !")
    print(f"Time's Up\nHere's your result\n{ans_stat}")

exam_numbers()