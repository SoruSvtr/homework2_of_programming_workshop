def solve_puzzles(puzzles : str) -> list:
    solve = []
    while puzzles != "\\":
        solve.append(bool(puzzles))
        puzzles = input()
    print(solve)

text = input("Enter the list : (enter \ to exit)\n")
solve_puzzles(text)