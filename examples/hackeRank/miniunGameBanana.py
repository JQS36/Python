def minion_game(string):
    vowels = 'AEIOU'
    kevin_score, stuart_score = 0, 0
    strlen = len(string)
    for i in range(strlen):
        if string[i] in vowels:
            kevin_score += strlen-i
        else:
            stuart_score += strlen-i
    print(kevin_score, stuart_score, sep=" - ")
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

minion_game("BBANANA")