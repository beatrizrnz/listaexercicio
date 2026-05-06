num = int(input("digite um numero:"))
if num % 2 == 0:
   print(f"o numero {num} e par")
   for i in range(0, num + 1,2):
      print(i)
else:
   print(f"o nuemro {num} e impar")
   for i in range(1, num + 1,2):
      print(i)