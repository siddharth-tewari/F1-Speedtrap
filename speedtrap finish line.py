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

hamilton = ham['SpeedFL']
bottas = bot['SpeedFL']
verstappen = ver['SpeedFL']
perez = per['SpeedFL']
leclerc = lec['SpeedFL']
sainz = sai['SpeedFL']
lando = nor['SpeedFL']
ricciardo = ric['SpeedFL']
gasly = gas['SpeedFL']
tsunoda = tsu['SpeedFL']
alonso = alo['SpeedFL']
ocon = oco['SpeedFL']
lance = stroll['SpeedFL']
vettel = vet['SpeedFL']
kimi = rai['SpeedFL']
giovinazzi = gio['SpeedFL']
russell = rus['SpeedFL']
latifi = lat['SpeedFL']
mick = msc['SpeedFL']

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





