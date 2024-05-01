x = 10
while x >= 0:
   print(x)
   x = x - 1

for x in range(0 ,10):
  x += 1
  print(x)
  
number = int(input("Digite um número:"))
begin = int(input("De:"))
end = int(input("Até:"))

x = begin

while x <= end:
  print(f"{number} x {x} = {number * x}")
  x = x + 1