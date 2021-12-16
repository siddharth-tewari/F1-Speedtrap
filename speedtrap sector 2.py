import fastf1 as ff1, fastf1
from matplotlib import pyplot as plt
import numpy as np

fastf1.Cache.enable_cache('cache')
                          
laps = ff1.get_session(2021, 'Abu Dhabi', 'R').load_laps()

ham = laps.pick_driver('HAM').pick_fastest()
ver = laps.pick_driver('VER').pick_fastest()
per = laps.pick_driver('PER').pick_fastest()
sai = laps.pick_driver('SAI').pick_fastest()
lec = laps.pick_driver('LEC').pick_fastest()
nor = laps.pick_driver('NOR').pick_fastest()
ric = laps.pick_driver('RIC').pick_fastest()
gas = laps.pick_driver('GAS').pick_fastest()
tsu = laps.pick_driver('TSU').pick_fastest()
msc = laps.pick_driver('MSC').pick_fastest()
rai = laps.pick_driver('RAI').pick_fastest()
gio = laps.pick_driver('GIO').pick_fastest()
vet = laps.pick_driver('VET').pick_fastest()
stroll = laps.pick_driver('STR').pick_fastest()
alo = laps.pick_driver('ALO').pick_fastest()
oco = laps.pick_driver('OCO').pick_fastest()
rus = laps.pick_driver('RUS').pick_fastest()
lat = laps.pick_driver('LAT').pick_fastest()
bot = laps.pick_driver('BOT').pick_fastest()

hamilton = ham['SpeedI2']
bottas = bot['SpeedI2']
verstappen = ver['SpeedI2']
perez = per['SpeedI2']
leclerc = lec['SpeedI2']
sainz = sai['SpeedI2']
lando = nor['SpeedI2']
ricciardo = ric['SpeedI2']
gasly = gas['SpeedI2']
tsunoda = tsu['SpeedI2']
alonso = alo['SpeedI2']
ocon = oco['SpeedI2']
lance = stroll['SpeedI2']
vettel = vet['SpeedI2']
kimi = rai['SpeedI2']
giovinazzi = gio['SpeedI2']
russell = rus['SpeedI2']
latifi = lat['SpeedI2']
mick = msc['SpeedI2']

print("Hamilton")
print(hamilton, "Kmph", '\n')

print("Bottas")
print(bottas, "Kmph" '\n')

print("Verstappen")
print(verstappen, "Kmph" '\n')

print("Perez")
print(perez, "Kmph" '\n')

print("Leclerc")
print(leclerc, "Kmph" '\n')

print("Sainz")
print(sainz, "Kmph" '\n')

print("Ricciardo")
print(ricciardo, "Kmph" '\n')

print("Norris")
print(lando, "Kmph" '\n')

print("Alonso")
print(alonso, "Kmph" '\n')

print("Ocon")
print(ocon, "Kmph" '\n')

print("Gasly")
print(gasly, "Kmph" '\n')

print("Tsunoda")
print(tsunoda, "Kmph" '\n')

print("Vettel")
print(vettel, "Kmph" '\n')

print("Stroll")
print(lance, "Kmph" '\n')

print("Russell")
print(russell, "Kmph" '\n')

print("Latifi")
print(latifi, "Kmph" '\n')

print("Raikkonen")
print(kimi, "Kmph" '\n')

print("Giovinazzi")
print(giovinazzi, "Kmph" '\n')

print("Schumacher")
print(mick, "Kmph" '\n')





