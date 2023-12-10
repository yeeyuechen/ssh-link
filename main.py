import os

os.system('cls')

print('SSH Link Manager')
print('ver.1.0-py')
print('Press "help" to get help')

var = 1

while var == 1 :
    comm_input = input('>>')
    if comm_input == "help" :
        print('SSH Link is a simple SSH link manager')
        print("command list: \n run —— to run a data file \n cat —— to review a data file \n new —— to creat a new SSH link data file \n delete —— to remove the SSH link data file \n help —— to get help \n exit —— to exit SSH Link")
    if comm_input == "new" :
        print('Enter the name of this data file')
        DataFileName = input("Echo>>>")
        print('Enter the SSH host address')
        SSH_Host_ADDRESS = input('Echo>>>')
        print('Enter the SSH login username')
        SSH_LOGIN_Username = input('Echo>>>')

        while var == 1 :
            NEW_input = SSH_LOGIN_Username + "@" + SSH_Host_ADDRESS
            print(NEW_input)
            finalecho = "data/" + DataFileName + ".txt"
            f = open(finalecho, "w", encoding='utf-8')
            f.write(NEW_input)
            f.flush
            f.close
            break
        print("You must exit the APP to save changes")

    if comm_input == "cat" :
        os.system('tree /F data')
        print('Which data do you want to review?')
        CAT_Input = input("Enter>>>")
        with open("data/" + CAT_Input, "r") as cat:
            CAT_Output = cat.read()
        print(CAT_Output)

    if comm_input == "exit" :
        print('See you next time. ')
        break
    
    if comm_input == "delete" :
        print('Whitch data do you want to remove? ')
        os.system('tree /F data')
        DEL_Input = input("Enter>>>")
        os.remove("data/" + DEL_Input)
        print("Success")

    if comm_input == "run" :
        print("To make the SSH Link data running , you must choose a datafile. ")
        print('Whitch data do you want to remove? ')
        os.system('tree /F data')
        RUN_Input = input("Enter>>>")
        with open("data/" + RUN_Input, "r") as run:
            RUN_Output = run.read()
        print("Enter the port of the SSH host")
        PORT_Input = input("Enter the port，Example：22 >>")
        FINALE_Run = "ssh " + RUN_Output + " -p " + PORT_Input
        os.system("cls")
        print("Loading...")
        os.system(FINALE_Run)
    else :
        print("Unknow command")