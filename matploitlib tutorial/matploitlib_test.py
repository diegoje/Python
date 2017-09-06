from matplotlib import pyplot as plt
import numpy as np

#style.use("ggplot")

x, y = np.loadtxt("data.csv",
                    unpack = True,
                    delimiter = ",")

plt.plot(x,y)

#this is a comment


plt.title("Awesome Title")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
