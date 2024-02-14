# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,compay_name) -> None:
        self.company_name=compay_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

class User(ABC):
    def __init__(self,name ,email,nid) -> None:
        self.name=name
        self.email=email
        self.__nid=nid # ei nid amra jokhon tokhon share korbo na 
        # TODO: set user id dynamically
        self.__id=0
        self.wallet=0 # rider or driver or user er wallet initially 0 thakbe

    @abstractmethod # amader ei class ta jara inherit korbe tader k implement kortei hobe 
    def display_profile(self):
        raise NotImplementedError    #kew call korle implement kortei hobe 


class Rider(User):# rider hocche ekdhoroner user....rider ekjon passenger
    def __init__(self, name, email, nid, current_location,initial_amount) -> None:
        self.current_ride=None # initially se kono drive e thakbe na 
        self.wallet=initial_amount
        self.current_location=current_location #
        super().__init__(name, email, nid)

    def display_profile(self): # jehetu user class e display profile method abstract base korche tie j j inherit korbe take must be oi method abar likhte hobe 
        print(f'Rider: with name : {self.name} and email: {self.email}')

    def load_cash(self,amount): # rider tar wallet e taka add korbe 
        if amount>0:
            self.wallet+=amount

    def update_location(self, current_location): # ek jaiga theke arek jaiga gele amra amader current location ta update kore felbo
        self.current_location=current_location
    
    
    """  """
    def request_ride(self,ride_sharing,destination):#location=None
        if not self.current_ride:
            print('looking for a ride')
            # TODO : set ride properly
            # TODO : set current ride via ride match
            ride_request= Ride_Request(self,destination)
            ride_matcher=Ride_Matching(ride_sharing.drivers)
            ride=ride_matcher.find_driver(ride_request)#amar ekta ride er request ache tumi amake ekta driver dao
            print('got the ride',ride)
            self.current_ride=ride

    def show_current_ride(self):
        print(self.current_ride)



class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location # driver er current location ta kothai seta amader jana lagbe
        self.wallet=0 #initially driver er wallet e kono taka thakbe na 

    def display_profile(self): # driver jehetu ekjon user tie display profile ta ditei hobe 
        print(f'Driver with name: {self.name} and email: {self.email}')

    def accept_ride(self,ride):
        ride.set_driver(self) # driver jodi ride ta accept korte chay then ei func kaj korbe 


class Ride:
    def __init__(self,start_location, end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location #ride er start and end location lagve
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None 
        self.estimated_fare=None # tar vara koto lagbe setar joonno but ekhono set kori nie amra

    def set_driver(self, driver): #ekta rider er khetre amra driver k save kore dibo
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self,rider, amount):
        self.end_time=datetime.now() # datetime ekta build in function 
        self.rider.wallet-=self.estimated_fare # rider taka dibe tie - minus hobe
        self.driver.wallet+=self.estimated_fare # driver er wallet ei amount ta add kore dibo

    def __repr__(self) -> str:
        return f'Ride details: Started: {self.start_location} to {self.end_location}'

class Ride_Request:
    def __init__(self, rider, end_location) -> None: # init ta ke define kore dilam
        self.rider=rider # ekhane rider ta k and se kothai jabe or last location ta kothai 
        self.end_location=end_location

class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.available_drivers=drivers

    def find_driver(self, ride_request): # ride er request onujayi ekjon driver k khujtechi 
        if len(self.available_drivers)>0:
            # TODO: find the closest driver of the rider
            print('looking for a driver')
            driver=self.available_drivers[0] # available driver er first jon k nilam
            ride=Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride) # end_location ta directly ride request e ache but current_location ta ride request er rider er moddhe ache tie evabe likhte hoiche
            return ride

class Vehicle(ABC):

    speed={
        'car':50,
        'bike':60,
        'cng':15
    }
    def __init__(self ,vehicle_type, license_plate,rate) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        self.status='available'

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status='available'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status='available'


# check the class integration
niye_jao=Ride_Sharing('Niye jao')
sakib=Rider("sakib khan",'sakib@khan.com',2343,'mohakhali',1200)
niye_jao.add_rider(sakib)
kala_pakhi=Driver('kala pakhi','kala@sada.com',3454,'gulsan1')
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.request_ride(niye_jao,'uttara')
print(sakib.show_current_ride())