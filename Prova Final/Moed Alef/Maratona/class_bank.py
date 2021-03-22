class Bank:

    def _init_(self,name,last_name,id,age,salary = 5500):        
        self.name = name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.salary = salary
        self.email = name+"."+last_name+"@bank.co.il"        
        self.account = 0
        
    def desposit(self,amount):
        self.account += amount

    def withdraw(self, amount):
        if self.age <= 20 and amount > self.account:
            print("not possible to withdraw")
        else:
            self.account -= amount
        
    def loan(self, amount):
        if self.age <= 20: 
            print("not possible to loan")
        elif amount <= self.salary*12