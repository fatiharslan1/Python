
# Functions

def print_five():
    print(5)
print_five()

def return_number(number):
    return number
return_number(5)

def return_big_number(a,b):
    if a>b:
        return a
    else:
        return b

print(return_big_number(4,8))

def print_text(a,b):
    big_number = return_big_number(a,b)
    text="{} more big number".format(big_number)
    print(text)

print_text(5,7)

# *args
" ".join(["kate","bishop"])

def full_name(args):
    return" ".join(args)
print(full_name("jack","snow"))


#**kwargs

def print_name(**kwargs):
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')

print_name(name="arya")










