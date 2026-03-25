import random 

class Client:
    def __init__(self,id ,name,email):
        self.id = id
        self.name=name
        self.email= email
        self.accounts=[]
    
    def show(self):
        print(f"ID: {self.id}")
        print(f"NAME: {self.name}")
        print(f"EMAIL: {self.email}")
