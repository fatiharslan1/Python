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

# for loop

names = ["Jack William","Nick Cage","Andrew Blake","Bob Marly","Alica Clark","Kate Snow","Sonya Zack"]
name_no = 0

#for name in names:
#    print(name)

for n in names:
    name_no +=1
    name, surname = n.split()[0], n.split()[1]
    print('{0}. Name {1} surname {2}.'.format(name_no,name,surname))

# Tupple

tup1 = (1,2,3,4,5)
for no in tup1:
    print(no)

list1 = [[1,2,3],[4,5,6]]
for x,y,z in list1:
    print(y)

#Dictionary

users = {
    'name' : 'Kate',
    'surname' : 'Bishop'
}

for n,s in users.items():
    print("Key:  {} \tvalue: {}".format(n,s))


# While loop
x = 0

while x < 10:
    print("{}  is smaller than 10 ".format(x))
    x +=1
else:
    print("{}  is not  smaller than 10 ".format(x))


# factorial
number = 5
answer = 1

while number > 0:
    answer = answer * number
    number -= 1

print(answer)

# Range

list(range(10))

[*range(10)]

[*range(2,7)]

[*range(2,8,2)]

for number in range(5):
    print(number)


# Enumerate

names = ["Jack William","Nick Cage","Andrew Blake","Bob Marly","Alica Clark","Kate Snow","Sonya Zack"]
for name in enumerate(names):
    print(name)

for index, name in enumerate(names):
    print(index,name)

# Zip

names = ["Jack ","Nick ","Andrew ","Bob ","Alica ","Kate ","Sonya "]
lastName =["William","Cage","Blake","Marly","Clark","Snow","Zack"]

for name in zip (names,lastName):
    print(name)

# break

names = ["Jack William","Nick Cage","Andrew Blake","Bob Marly","Alica Clark","Kate Snow","Sonya Zack"]*5
for index,name in enumerate(names):
    if name == "Bob Marly":
        print(index)
        break

# continue

for number in range(1,12):
    if number%2==0:
        continue
    print(number)

# pass

for number in range(1,12):
    if number%2==0:
        pass
    else:
        print(number)



