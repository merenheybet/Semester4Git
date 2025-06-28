import numpy as np
import matplotlib.pyplot as plt

# Stützstellen (xi, yi) und ihre Ableitungen (yi')
x = np.array([-3, -1, 0, 4, 6])
y = np.array([5, 3, -3, 2, -1])
dy = np.array([-1.0, -2.67, -0.2, 0.33, -1.5])

# Hermite-kubisches Interpolationspolynom für ein Teilintervall
def hermite_cubic(x0, x1, y0, y1, dy0, dy1, x_vals):
    h = x1 - x0
    t = (x_vals - x0) / h
    h00 = (1 + 2*t)*(1 - t)**2
    h10 = t*(1 - t)**2
    h01 = t**2*(3 - 2*t)
    h11 = t**2*(t - 1)
    return h00*y0 + h10*h*dy0 + h01*y1 + h11*h*dy1

# Kurve vorbereiten
X_plot = []
Y_plot = []

for i in range(len(x) - 1):
    xs = np.linspace(x[i], x[i+1], 200)
    ys = hermite_cubic(x[i], x[i+1], y[i], y[i+1], dy[i], dy[i+1], xs)
    X_plot.append(xs)
    Y_plot.append(ys)

# Plot
plt.figure(figsize=(10, 6))

# Hermite-Kurven zeichnen
for xs, ys in zip(X_plot, Y_plot):
    plt.plot(xs, ys, label="", color="blue")

# Stützpunkte einzeichnen
plt.plot(x, y, 'o', color='black', label="Stützstellen")

# Tangenten an den Stützstellen
for xi, yi, dyi in zip(x, y, dy):
    xt = np.linspace(xi - 0.8, xi + 0.8, 100)
    yt = dyi * (xt - xi) + yi
    plt.plot(xt, yt, '--', color='orange', alpha=0.6)

# Plot-Dekoration
plt.title("Stückweise kubischer Hermite-Interpolant mit Tangenten")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()