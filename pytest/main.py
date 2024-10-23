def f(x):
    return 25*x**4 - 149*x**2 + 196
a = 0
b = 2
m = 0
while b - a > 0.001:
    m = (a + b)/2
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
print(f"Ekvationen har en rot x = ", round(m,3))



