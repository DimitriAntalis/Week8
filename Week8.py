import os
def main():
    directory = input("Please enter the complete address of directory where you want to store the file:  ")
    filename = input("Please enter the name of the file that you want to create: ")
    name = input("Please enter your name : ")
    address = input("Please enter your address : ")
    phone_number = input("Please enter your phone number : ")
    #Now we have to check whether the entered directory exists or not.
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+','+address+','+phone_number+'\n')
        writeFile.close()
        print("The file has the following contents that have been stored there:")
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry!!! The directory that you have entered is invalid.")
main()