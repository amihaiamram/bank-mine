class account:
    def __init__(self, acc_num, balance, password,name):
        self.acc_num = acc_num
        self.balace = balance
        self.password = password
        self.name = name
    def pass_check (self,word):
        if self.password == word :
            return True
        else :
            return print(" wrong password")
    def change_pass(self,new_pass):
            self.password=new_pass
            print("the password is " + self.password + " password changed ")
    def add(self, amount):
         self.balace = self.balace + amount
    def take(self, amount):
            if amount > self.balace:
                print ("you dont have enough money")
            else :
                self.balace = self.balace - amount
    """
    
decrease_person = None
for person in ppl:
    if person.name == decrease_name:
        decrease_person = person
        break
    decrease_person = None
    
    def transfer(self, amount,recipiant):
            self.take(amount)
            recipiant.add(amount)
            if decrease_person is None:
    print("No person with that name was found.")
     
    donor = input ()
    
    acc1 = none 
    if account in ppl 
       if account.acc_num == donor  
          donor = acc1
       
       
        """


"""class person:
    def __init__(self, num, perpass,name):
        # perpass is personal password to avoid confusion
        self.num = num
        self.password = perpass
    def transfer (money):
        account.nu
        #this is to add new ppl now to use existing ones
class bank :
    def __int__(self):
        self.peopel =[]"""