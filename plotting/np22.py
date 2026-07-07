import numpy as np

x = np.linspace(-1, 2, 5)
y = np.linspace(-7, -2, 7)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

print(X.shape)
print(Y.shape)
print(Z.shape)

print("\nx:")
for e in x:
    print(e, end=" ")

print("\n\ny:")
for e in y:
    print(e, end=" ")

print("\n\nX:")
for e in X:
    print(e)

print("\nY:")
for e in Y:
    print(e)

print("\nZ:")
for e in Z:
    print(e)
