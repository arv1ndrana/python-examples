def bricks(Width, Height): 
   brick = ''
   for _ in range(Height):
      for _ in range(Width):
         brick += '*'
      brick += '\n'
   return brick[:-1]

def main():
   result = bricks(4,5)
   print(result)

if __name__ == "__main__":
   main()
