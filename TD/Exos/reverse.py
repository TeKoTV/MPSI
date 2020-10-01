def reverseWord(w):
    finalWord = ""
    for char in w:
        finalWord = char + finalWord
        # On ajoute les char au début du mot
    return finalWord

print(reverseWord("Nathan"))