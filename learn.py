## String formatter
name = 'bob'
Today = 'Wednesday'
greeting = f"Hello, {name}, Today is {Today}"
greetings = "Hello, {}, Today is {}"

# print(greeting)
# print(greetings.format("Rolf", "Tuesday"))

## List, Tuple, set
List = ['hello', 'Hi', 'Holla'] #can change, remove, add, keep order of element
Tuple = ('Volla', 'Voddo', 'vello') #cant change, remove, add, can keep order of element
Set = {'Vodacom', 'Tigo', 'Airtel'} # cant have duplicate elements

List.append('Monster Truck')
List.remove('Hi')
# print(List)
Set.add('shmuck')
# print(Set)
# print('hello' in List)
cont = True
go = True
# Simple while loop program for fun
while(cont):
    userName = input('What is your name: ')
    if(userName != ''):
        while(go):
            suggest = input('Tell me something!')
            if suggest in Set:
                print(f'huh, {userName}, Best try!')
                q = int(input('0 for Quit '))
                if(q == 0):
                    go = False
                    cont = False
                    break
            else:
                print(f'Tell Me something, {userName}')
    else:
        print('Please Tell Me your name!!')