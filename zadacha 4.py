import os
path_to_file = 'C:/Users/Àלטנ/test/Zadacha4/text.txt'
file = open(path_to_file, "r")

try:
    if (os.stat(path_to_file).st_size > 0):
        print("file opened successfully")
    if (os.stat(path_to_file).st_size == 0):
        print("Error: empty file")
except OSError:
    print("cannot open file")

def Sequence(file,needed_integer ):
    string = file.read() 
    temp_int = ''
    needed_number = 0
    if (len(string) == 0):
        print("Error: empty file")
        exit(-3)
    for index in range(len(string)): 
        if (string[index] != ' ') and (string[index] != '\n'):
            temp_int += string[index]
        if (string[index] == ' ') or (string[index] == '\n') or (index == (len(string) - 1)):
            try:
                current_integer = int(temp_int) 
            except ValueError:
                pass
                ## ignores non-integer characters
            if (current_integer == needed_integer):
                needed_number += 1
            else:
                pass
            temp_int = ''
    return needed_number
            
def Autotest():
    test_file = open("C:/Users/Àלטנ/test/Zadacha4/test.txt", "r")
    answer = 0
    answer = Sequence(test_file, 228)
    if (answer == 1):
        print("Autotest passed... Respect+")
    else:
        print("Autotest not passed. Program has been stopped")
        exit(-1)

Autotest()a=int(input("Vvedite iskomoe chislo   "))
answer = 0
answer = Sequence(file, a)
if (answer == 0):
    print("There are no needed integers in the sequence")
else:
    print("There are {} needed integers in the sequence".format(answer))
    