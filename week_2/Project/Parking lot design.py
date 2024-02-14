class Car:
    def __init__(self,license_plate,brand) -> None:
        self.license_plate=license_plate
        self.brand=brand

class ParkingLot:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.available_spots=capacity
        self.parked_cars=[]
        self.fee_rates={
            'hourly':10,
            'daily':50
        }

    def park_car(self,car):
        if self.available_spots>0:
            self.parked_cars.append(car)
            self.available_spots-=1
            print(f'car with license plate {car.license_plate} parked successfully')
        else:
            print('parking lot is full')

    def remove_car(self,car):
        if car in self.parked_cars:
            self.parked_cars.remove(car)
            self.available_spots+=1
            print(f'Car with license plate {car.license_plate} remove sucesfully')
        else:
            print('Car is not parked in the parking lot')

    def get_parked_cars(self):
        for car in self.parked_cars:
            print(f'License plate: {car.license_plate} Brand:{car.brand}')


    def search_car_by_license_plate(self,license_plate):
        for car in self.parked_cars:
            if car.license_plate==license_plate:
                print(f'car with license plate {license_plate} is parked')
                return
        print(f'No car with license plate {license_plate} found in the parking lot ')

    
    def calculate_fee(self,car,duration,rate_type):
        if rate_type in self.fee_rates:
            rate=self.fee_rates[rate_type]
            fee=rate*duration
            print(f'Fee for car eith license plate {car.license_plate} {rate_type}: {fee}')
        else:
            print(f'invalid rate type : {rate_type}')


    def set_fee_rate(self,rate_type,rate):
        self.fee_rates[rate_type]=rate
        print(f'Fee rate {rate_type}: {rate} updated')

    

#Create car objects
car1=Car('ABC123','Toyota')
car2=Car('DEF123','Honda')
car3=Car('EFG123','Ford')

#Create parking lot object with capacity of 2 cars
parking_lot=ParkingLot(2)

# park cars

parking_lot.park_car(car1)
parking_lot.park_car(car2)

# try parking another car( parking lot is full)
parking_lot.park_car(car3)

# remove a car 
parking_lot.remove_car(car1)

print('parked cars:')
parking_lot.get_parked_cars()

# search for a car by license plate
parking_lot.search_car_by_license_plate('ABC123')
parking_lot.search_car_by_license_plate('DEF123')

# calculate fee for a parked car
parking_lot.calculate_fee(car2,5,'hourly')
parking_lot.calculate_fee(car2,2,'daily')

#set a new fee rates
parking_lot.set_fee_rate('monthly',500)
parking_lot.calculate_fee(car2,2,'monthly')