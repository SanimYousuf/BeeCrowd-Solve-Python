a, b, c, d = map(int, input().split())

con = [
    b==d,
    a==c,
    (a==c) != (b==d)
]
if all(con):
    print("O JOGO DUROU 0 HORA(S) E 0 MINUTO(S)")
else:
    if b > d:
        d += 60
        c -= 1
    m = d - b

    if a > c:
        c += 24
    h = c - a

    if h == 0 and m==0:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")  
