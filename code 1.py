import keyword
def decrypt_clue(text: str) -> list:
    final_ans = []
    for i in keyword.kwlist:
            if text.find(i) != -1:
                final_ans.append(i)
    print(final_ans)

txt = input()
decrypt_clue(txt)