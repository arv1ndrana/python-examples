def fibonacci(n):
    fibonacci_series = []
    a,b = 0,1
    for i in range(n+1):
        c = a + b
        a,b = c,a
        fibonacci_series.append(a)
    return sum(fibonacci_series) * 4
print(fibonacci(5))
