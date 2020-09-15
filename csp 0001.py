import keyboard
def myString():
    print("The Program must have interface as below:")
    mystring  =   input()
    print("Please enter string:", mystring )
    print("The old string", mystring) 
    new =   mystring[::-1]
    print ("The reversed string:", new)
    print("Press enter to continue another reverse, ESC to exit")
    print(keyboard.is_pressed('Enter'))
    while True:
        if keyboard.is_pressed('Enter'):
            myString()
        if keyboard.is_pressed('ESC'):
            print('You Pressed ESC Key!')
            break 
myString()
