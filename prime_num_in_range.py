def prime_range(start, end):
   if start > end:
      start, end = end, start

   if start >= 1:
      start = 2

   prime_numbers = []

   for number in range(start,end+1):
      count = 0
      for factor in range(1,number+1):
         if number % factor == 0:
            count += 1
      if not count > 2:
         prime_numbers.append(number)
   return prime_numbers

def main():
   result = prime_range(2,10)
   print(result)

if __name__ == '__main__':
   main()
