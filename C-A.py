ord = input(str("Skriv ett ord: ")).lower()
#funktion som kollar om ord är enpalidrome
def palindrome(ord):
    if ord == ord[::-1]:
        print("Ja ordet är en palindrome")
    else:
        print("Nej ordet är inte en palindrome")

palindrome(ord)

