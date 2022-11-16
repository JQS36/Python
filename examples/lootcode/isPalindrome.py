def isPalindrome(head) -> bool:
    head_string = "".join(map(str, listT))
    head_string_reverse_string = head_string[::-1]
    return {"status": True, "head":head } if head_string == head_string_reverse_string else {"status": False, "head":head}

listT = [1, 2, 3, 2, 1]
print(isPalindrome(listT))