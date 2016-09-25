from taxi_class import Taxi,UnreliableCar,SilverServiceTaxi

prius1 = Taxi('Prius1',100)
prius1.drive(40)
prius1.start_fare()
prius1.drive(100)
print(prius1)

chev = UnreliableCar('chevete',100,30)
print(chev)
chev.drive(60)
print(chev)

pont = SilverServiceTaxi('pontiac',150,1.5)
print(pont)

# test for SilvereService
mazda = SilverServiceTaxi('mazda',200,2)
mazda.drive(10)
print(mazda.get_fare)
#