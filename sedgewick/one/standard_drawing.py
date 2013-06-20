# see http://matplotlib.org/users/pyplot_tutorial.html
import numpy as np
import matplotlib.pyplot as plt

# Points
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 20, 0, 20])

# Circles
circle = plt.Circle(
    (10, 10), 5,
    facecolor="none",
    edgecolor="b"
)

# Polygons
pa = np.array([
    [15, 15],
    [10, 10],
    [5, 5],
    [0, 4],
])
polygon = plt.Polygon(pa, edgecolor="g")

fig1 = plt.figure(1)
axis1 = fig1.gca()
axis1.add_artist(circle)
axis1.add_artist(polygon)

fig2 = plt.figure(2)
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')

fig3 = plt.figure(3)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
