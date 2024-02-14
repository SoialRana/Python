class Bank:
    def __init__(self) -> None:
        self.client_details_list=[]
        self.loggedin=False
        self.cash=100

    def register(self,name,ph_number,password):
        cash=self.cash
        conditions=True
        if len(str(ph_number))>11 or len(str(ph_number))<11:
            print('Invalid phone number!! please enter 11 digit')
            conditions=False

        if len(password)<5 or len(password)>18:
            print('Enter password greater than 5 and less than 18 character')
            conditions=False

        