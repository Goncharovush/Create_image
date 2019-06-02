import numpy as np
from PIL import Image

X = np.arange(0, 100, 0.1)
Y = np.arange(0, 100, 0.1)

XX, YY = np.meshgrid(X, Y)
data = np.zeros([1000, 1000], dtype=np.uint8)
array = np.zeros([1000, 1000, 3], dtype=np.uint8)
array[:, :, :] = np.random.randint(255, size=3)
for i in range(50):
    obj = np.random.randint(255, size=3)
    for j in range(50):
        a, b = np.random.uniform(low=0, high=100, size=2)
        std_1, std_2 = np.random.uniform(low=1, high=50, size=2)
        d = np.exp(-(XX - a) ** 2 / std_1 - (YY - b) ** 2 / std_2)
        d[d < 0.5] = 0
        d[d >= 0.5] = 1
        array[np.nonzero(d)[0], np.nonzero(d)[1], :] = obj
        data[np.nonzero(d)[0], np.nonzero(d)[1]] = i


bord = np.zeros([1000, 1000], dtype=np.uint8)
for j in range(len(data)-1):
    bord[j+1] = data[j+1]-data[j]
data = data.transpose()
bord = bord.transpose()
for j in range(len(data)-1):
    bord[j+1] += (data[j+1]-data[j])
bord = bord.transpose()
bord[np.where(bord != 0.0)] = 1
array[np.nonzero(bord)[0], np.nonzero(bord)[1], :] = [0., 0., 0.]

img = Image.fromarray(array)
img.save('image1.png')