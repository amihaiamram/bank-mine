from classes import *

ppl = [account(1,9999,2659,"amihai amram"),
       account(2,100000,31344,"daniel amram")]#might update code later on to use with txt file based database, it would be able to read and write
bank_on = True
flag = 0
while bank_on:
    print("what activity would you like to preform")
    current_acc = int(input(" what is your account number "))
    current_pass = int(input(" what is your password "))
    for account in ppl :
        if account.acc_num == current_acc:
            if account.pass_check(current_pass) == True:
                print(" well hello " + account.name + " your balance is :" ,account.balace)
                answer = str(input(
                    " for deposting press d \n for witdrawing press w\n for transfering funds press t\n for changing password press p \n "))
                if answer.isnumeric() == False:
                    output = answer.lower()

                    if output == 'd':
                        account.add(int(input("please state amount : ")))
                        bank_on = True
                    elif output == "w":
                        account.take(int(input("please state amount : ")))
                        bank_on = True
                    elif output == "t":
                        amount1=int(input("please state amount : "))
                        recipiant1= int(input("please state which account : "))
                        account.take(amount1)
                        for account in ppl:
                            if account.acc_num == recipiant1:
                              account.add(amount1)
                        bank_on = True
                    elif output == "p":
                        account.change_pass(input("please enter new password "))
                        bank_on = True
                    else:
                        print("please give a correct input")
                        bank_on = True
                else:
                    print("wrong input please try again ")
                    bank_on = True
            else :
                if flag <2:
                    flag = flag +1
                    print( "you have " ,3 - flag, " more attempts before system shut down")
                else:
                    print("account locked")
                    bank_on=False


