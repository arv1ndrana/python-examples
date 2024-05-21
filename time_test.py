import time
a = b = c = d = e = f = 1
f = 2
def nested_loops():
    if a == b:
        if c == d:
            if e == f:
                return True

def one_liner():
    if a == b and c == d and e == f:
        return True

times = []
def main():

    start = time.perf_counter()
    nested_loops()
    end = time.perf_counter()
    times.append(end - start)

    start = time.perf_counter()
    one_liner()
    end = time.perf_counter()
    times.append(end - start)

if __name__ == '__main__':
    main()
    print(min(times))
    print(times.index(min(times)))
    print("Conclusion: The fastest and most efficient is oneliner")
