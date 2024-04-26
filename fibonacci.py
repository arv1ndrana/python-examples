series = [0, 1, 1]
N = 10

a = series[1]
b = series[2]

for i in range(1,N - 2):
    c = a + b
    series.append(c)
    a , b = b , c
print(series)
