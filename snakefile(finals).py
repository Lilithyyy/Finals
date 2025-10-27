subor = open('snake.txt', 'r')
subor2 = open('had_kompresia.txt', 'w')
pocet=0
maximum=0

def kompresia(s):
    if s=='':
        return''
    s=s+'.'
    pismeno=s[0]
    pocet=0
    vystup=''
    for znak in s:
        if znak==pismeno:
            pocet+=1
        else: 
            vystup = vystup +'{} {}'.format(pismeno, pocet)
            pismeno=znak
            pocet=1

        return vystup
    
for riadok in subor:
    riadok = riadok.strip()
    print(riadok)
    riadok2 =kompresia(riadok)
    subor2.write(riadok2 + '\n')
    print(riadok2)
    if len(riadok) > maximum:
        maximum = len(riadok)
    pocet +=1

print('pocet riadkov v subore:', pocet)
print('pocet krokov v najdlhsej hre:', maximum)
subor.close()
subor2.close()