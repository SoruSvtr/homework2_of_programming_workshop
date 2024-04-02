def digit_Info(num : int, operation : str) -> int:
    digit_list = list(map(int, str(num).strip()))
    if operation == "digitSum":
        return sum(digit_list)
    elif operation == "digitCount":
        return len(digit_list)
    else:
        print("operation isn't Valid\nplease try again")
        operation = input()
    
def magic_check(num : int) -> bool:
    sum = "digitSum"
    count = "digitCount"
    while(digit_Info(num, count) > 1):
        num = digit_Info(num, sum)
    if num == 1:
        return True
    else:
        return False
def calculate_magic_numbers(start : int, end : int) -> list:

    final_list = []

    for i in range(start, end):
        if(magic_check(i)):
            final_list.append(i)
    print(final_list)

while True:
    try:
        a = int(input("Enter the starting point: "))
        b = int(input("Enter the ending point : "))
        break
    except (TypeError, ValueError):
        print("Invalid Type\nplease Enter two integers\nAnd also every time you enter an invalid type it'll start from the beginning :]")
        continue
    except EOFError:
        break 
calculate_magic_numbers(a, b)