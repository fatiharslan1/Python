#if

number = 16

if number == 15 :
    print(number)
elif number > 15 :
    print("True")
else:
    print("false")


# using if on list
list_1 = ['d','a','n','i','e','l']
target_char = 'b'
if target_char in list_1:
    print("Find it!!")
else:
    list_1.append(target_char)

    print('I appended it!!')
    print('New list {}'.format(list_1))





























