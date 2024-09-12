a, b = map(int, input().split())

if a<b:
    r = b - a
else:
    r = b + 24 - a

print(f"O JOGO DUROU {r} HORA(S)")