name = input('Name:')
print('Hello, ' + name)
age = int(input(f"How old are you {name} ?"))

if age < 18:
    print("Adult Supervision is required!")
    parentname = input("What is your parent/guardian's name?")
    print('We need some more details.')
    parentage = int(input(f'How old is {parentname} ?'))
    if parentage < 18:
        print('Sorry! According to the age you have entered, your parent/guardian is not an adult. \nSee you next time!')
    if parentage >= 18:
        print(f"Age accepted. Welcome {name} and {parentname} !")
if age >= 18:
    print(f"Age accepted. Welcome {name}!")


    


