a,b = map(int,input().split())

if a==1:
    r = 4.00*b
    print(f"Total: R$ {r:.2f}")

elif a==2:
    r = 4.50*b
    print(f"Total: R$ {r:.2f}")

elif a==3:
    r = 5.00*b
    print(f"Total: R$ {r:.2f}")

elif a==4:
    r = 2.00*b
    print(f"Total: R$ {r:.2f}")

elif a==5:
    r = 1.50*b
    print(f"Total: R$ {r:.2f}")