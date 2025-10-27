zoznamjedal = open('objednane_jedla.txt', 'r').readlines()
z, c, m, o = 0, 0, 0, 0

for i in range(len(zoznamjedal)):
    zoznamjedal[i] = zoznamjedal[i].rstrip("\n").split(" ")
    match zoznamjedal[i][1]:
        case 'z':
            z+=1
        case 'c':
            c+=1
        case 'm':
            m+=1
        case 'o':
            o+=1
if z < 20:
    print('z')
else:
    print('Zelenych jedal je viac ako 20')

if c < 20:
    print('c')
else:
    print('Cervenych jedal je viac ako 20')

if m < 20:
    print('m')
else:
    print('Modrych jedal je viac ako 20')

if o < 20:
    print('o')
else:
    print('Oranzovych jedal je viac ako 20')

print(f'Celkovy pocet objednanych jedal je {len(zoznamjedal)}')
print(f'z: {z}, c: {c}, m: {m}, o: {o}')