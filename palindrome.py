def palindromic(text):
    nxt = 0
    if len(text) == 1 or text == "":
        return True
    else:
        if text[0] == text[-1]:
            return palindromic(text[nxt+1:-(nxt+1)])
        else: return False


if __name__ == "__main__":
    print(palindromic(input()))