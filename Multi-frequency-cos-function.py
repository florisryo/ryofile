import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['font.family'] = 'Times New Roman' #フォント一括
plt.rcParams["font.size"] = 20
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.direction'] = 'in'

fig = plt.figure()
pi = np.pi
ims = []

sin2 = []
for i in range(1000):
    sin2.append(0)

for i in range(1,10):
    x = []
    x2 = []
    for j in range(1000):
        x.append(j/(pi*100))
        sin2[j] += np.cos(i*j/100)
    im = plt.plot(x,sin2,color = "blue")
    ims.append(im)

    
ani = animation.ArtistAnimation(fig, ims, interval=200)
plt.show()
