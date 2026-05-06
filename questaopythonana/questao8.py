novo= 0
jovem=0
adulto=0
idoso=0
while True:
    continuar= input('deseja continuar? (s/n)')
    if continuar == "s":
        a = int(input('diga sua idade:'))
        if a >=0 and a<=25:
            novo=1
        elif a == 26:
            jovem=1
        elif a == 60:
            adulto=1
        elif a > 60:
            idoso=1
    else: 
        break
print(f"novo: {novo}, jovem: {jovem}, adulto: {adulto}, idoso: {idoso}")