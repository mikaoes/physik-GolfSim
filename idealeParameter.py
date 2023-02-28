import src.winkel
import src.gwkraefte
import numpy as np
import math

weite = np.zeros((90, 20))

for winkel in range(0, 90, 1):
    for speed in range(40, 60, 1):
        vy = src.winkel.vy(speed, winkel)
        vx = src.winkel.vx(speed, winkel)

        i = 1
        while (i * vy - 0.5 * 9.81 * i**2) > 0:
            i += 0.01
        
        l = vx * i

        weite[winkel, speed-40] = l

print(np.unravel_index(np.argmax(weite), weite.shape))
print(weite[np.unravel_index(np.argmax(weite), weite.shape)])
