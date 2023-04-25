d = int(input('digite 1 parra gasolina e 2 para alcool '))
litro = float(input('quantidade em litros '))
if d == 1:
    if litro <= 20:
        vp = litro * 3.3
        vp = vp - (vp * 0.04)
        print('o valor e ', vp)
    else:
        vp = litro * 3.3
        vp = vp - (vp * 0.06)
        vp = round(vp, 2)
        print('o valor e', vp)
elif d == 2:
    if litro <= 20:
        vp = litro * 2.9
        vp = vp - (vp * 0.03)
        vp = round(vp, 2)
        print('o valor e', vp)
    else:
        vp = litro * 2.9
        vp = vp - (vp * 0.05)
        vp = round(vp, 2)
        print('o valor e', vp)
else:
    print('nao esta correto porfavor tente novamente')