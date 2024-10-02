
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


# map, filter and lambda expressions

def number_square(x):
    return x**2
print(number_square(5))

numbers = [*range(1,8)]
print(numbers)

for index in range(len(numbers)):
    numbers[index]=number_square(numbers[index])

print(numbers)

[*map(number_square,numbers)]

def even_number_filter(x):
    #if x%2==0:
    #    return x
    return x if x%2==0 else None

numbers = [*range(1,6)]
print([*filter(even_number_filter,numbers)])

list(map(lambda number: number**2, numbers))

[*filter(lambda x: x if x%2==0 else None,numbers)]


# input

input("enter a number : ")

inn = input("enter a number : ")
type(int(inn))

def app():
    inn = input("enter a number : ")
    process = input("even or odd ? ")

    if process == "even":
        if int(inn)%2==0:
            return 'even number.'
        else:
            return 'odd number.'
    elif process == "odd":
        if int(inn)%2==1:
            return 'odd number.'
        else:
            return 'even number.'

app()


