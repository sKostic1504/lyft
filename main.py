from datetime import datetime

import car
from Engine import capulet_engine
from Battery import nubbin_battery

cap = capulet_engine.Capulet(15000, 10000)
bat = nubbin_battery.Nubbin(datetime.now(), datetime(2017,4,15))
c = car.Car(cap, bat)
output = c.needsService()


print(output)