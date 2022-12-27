
def isPalindrome(text: str) -> bool:
    return text == text[::-1]

def solver(text: str, init: int, lenght: int, result: list) -> list:
    end = init + lenght
    if end <= len(text):
        cuttedText = text[init:end]
        if isPalindrome(cuttedText):
            result.append(cuttedText)
        if len(text) == lenght:
            return result
        else:
            solver(text, init + 1, lenght, result)
    else:
        if len(text) == lenght:
            return result
        else:
            solver(text, 0, lenght + 1, result)

if __name__ == '__main__':
    result = []
    solver("mamapapahiijo", 0, 1, result)
    print(result)
