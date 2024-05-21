def fibonacci(n):
    a,b = 0,1
    fibonacci_series = [a,b]
    for i in range(n - 2):
        a,b = b, a + b
        fibonacci_series.append(b)
    return fibonacci_series

result = fibonacci(10)
print(result)
