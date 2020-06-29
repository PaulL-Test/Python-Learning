
'''Define a function which receives a string as a parameter. The function splits the string
 into pairs of two characters. If the string contains an odd number of characters then it should
 replace the missing second character of the final pair with an underscore ('_').
### Examples:
 solution('abc') # should return ['ab', 'c_']
 solution('abcdef') # should return ['ab', 'cd', 'ef'] '''

def String_Split(text):

        x = text
        n = text.__len__()

        if n % 2 == 0:
            print([x[i:i + 2] for i in range(0, len(x), 2)])
        else:
            str1 = text + '_'
            print([str1[i:i + 2] for i in range(0, len(str1), 2)])

String_Split("abc")
String_Split ("abcdef")

def string_reverese(str):
    print(str [::-1])

string_reverese("This is an example!")


class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

def God():
    Adam = Man()
    Eva = Woman()
    return [Adam, Eva]
