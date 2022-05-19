def EveryOtherLetter(string):
    # new_string = ''
    for num, i in enumerate(string):
        if num%2==0:
            new_string += i
    return new_string

String = "house"

print(EveryOtherLetter(String))