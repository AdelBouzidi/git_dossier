
from modsim import *
import matplotlib.pyplot as plt



bikestate = State(moulin=10, mailly=5)

bikestate.moulin += 1
bikestate.moulin -= 1

# cette fonction envoie moulin vers mailly
def moulin_vers_mailly():
    bikestate.moulin -= 1
    bikestate.mailly += 1
    # print("\n velo_vers_mailly")

moulin_vers_mailly()
print(bikestate)

def mailly_vers_moulin():
    bikestate.moulin += 1
    bikestate.mailly -= 1
    # print("\n velo_vers_mailly")
    
print("\n _____________________________________________________")
print(bikestate)


p1 = 0.5
p2 = 1
def step(p1, p2):
    if flip(p1):
        moulin_vers_mailly()
    if flip(p2):
        mailly_vers_moulin()

# flip c un random   

for i in range(10):
    step(p1,p2)   
    

results = TimeSeries()
results[0] = bikestate.mailly

for i in range(60 * 14 * 30):
    # print(f"step {i}")
    step(0.5, 0.5)
    results[i + 1] = bikestate.mailly

fig, ax = plt.subplot()
ax.plot(results)
ax.set_title("Velo à mailly")
ax.set_xlabel("temps")
ax.set_ylabel("Nombre de vélos à Mailly")   
plt.show()



