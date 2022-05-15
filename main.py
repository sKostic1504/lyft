from datetime import datetime

from Car import car
from Engine import engine
from Battery import battery
from Engine import capulet_engine, willoughby_engine, sternman_engine
from Battery import spindler_battery, nubbin_battery

cap = capulet_engine.Capulet(15000, 10000)
bat = nubbin_battery.Nubbin(datetime.now(), datetime(2017,4,15))
c = car.Car(cap, bat)
output = c.needsService()


print(output)