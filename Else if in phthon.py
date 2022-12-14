is_male = False
is_tall = False

if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("You are short male")

elif not(is_male) and  (is_tall):
        print("You are short but not a male")

else:
    print("you are neither a tall noif r a male")