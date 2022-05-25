def decor(func):
    def wrap():
        print("===========================")
        func()
        print("===========================")
    return wrap

def print_text():
    print("Bonjour a tous")

decorer = decor(print_text)
decorer()
print()

#ou encore

print_text = decor(print_text)
print_text()
print()

# @decor
# def print_text():
#     print("Honjour a tous")
# print_text = decor(print_text)