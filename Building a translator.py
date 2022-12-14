def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                 translation = translation + "G"
            else:
                 translation = translation + "g"
        else:
            translation = translation + letter # why this error is always there unable to understand
     return translation

print(translate(input("Enter a phrase: ")))