maths = float(input('Enter marks in maths : '))
physics = float(input('Enter marks in physics : '))
chemistry = float(input('Enter marks in chemistry : '))
if maths < 35 or physics < 35 or chemistry < 35:
    print('Student has failed!!!')
else:
    print('Student has Passed!!!')
    average = (maths + physics + chemistry) / 3
    if average <= 59:
        print('Grade : C')
    elif average <= 69:
        print('Grade : B')
    else:
        print('Grade : A')
