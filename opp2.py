class Client:
    def __init__(self,id ,name,email):
        self.id = id
        self.name=name
        self.email= email
        self.accounts=[]
    
    def show(self):
        print(self.id)
        print(self.name)
        print(self.email)
        