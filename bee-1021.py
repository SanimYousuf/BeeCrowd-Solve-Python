a = float(input())

print("NOTAS:")

a1,a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0,0

if a >= 100:
    a1 = int(a // 100)
    a = a % 100
   
if a >= 50:
    a2 = int(a // 50)
    a = a % 50
   
if a >= 20:
    a3 = int(a // 20)
    a = a % 20  

if a >= 10:
    a4 = int(a // 10)
    a = a % 10

if a >= 5:
    a5 = int(a // 5)
    a = a % 5
    
if a >= 2:
    a6 = int(a // 2)
    a = a % 2

a7 = round(a, 2)

print(f"{a1} nota(s) de R$ 100.00")
print(f"{a2} nota(s) de R$ 50.00")
print(f"{a3} nota(s) de R$ 20.00")
print(f"{a4} nota(s) de R$ 10.00")
print(f"{a5} nota(s) de R$ 5.00")
print(f"{a6} nota(s) de R$ 2.00")

print("MOEDAS:")

a = round(a7 * 100)

a1,a2,a3,a4,a5,a6 = 0,0,0,0,0,0

if a >= 100:
    a1 = int(a // 100)
    a = a % 100
   
if a >= 50:
    a2 = int(a // 50)
    a = a % 50
   
if a >= 25:
    a3 = int(a // 25)
    a = a % 25  

if a >= 10:
    a4 = int(a // 10)
    a = a % 10

if a >= 5:
    a5 = int(a // 5)
    a = a % 5
    
if a >= 1:
    a6 = int(a // 1)
    a = a % 1

print(f"{a1} moeda(s) de R$ 1.00")
print(f"{a2} moeda(s) de R$ 0.50")
print(f"{a3} moeda(s) de R$ 0.25")
print(f"{a4} moeda(s) de R$ 0.10")
print(f"{a5} moeda(s) de R$ 0.05")
print(f"{a6} moeda(s) de R$ 0.01")