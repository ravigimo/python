print('============= Welcome to the script world =========')
print('===================================================')
print('Please enter you Name: ')
name = input()
print('Your Name is : ' + name)

print('===================================================')
time = input('What is the Time (0-24Hours) : ')
print('Hi ' + name + ' the time will be shown as below....')
if int(time) == 24:
    print('Today finished, Next day started')
if int(time) < 12:
    print('Current Time is ' + str(time) + ' AM')
else:
    print('Current Time is ' + str(int(time)-12) + ' PM')
print('================BYE BYE============================')