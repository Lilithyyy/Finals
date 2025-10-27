stanice_subor = open('meteo_stanice.txt', 'r')
lines = stanice_subor.readlines()
info, temperatures = [], []

for line in lines:
    info.append(line.rstrip('\n').split(' '))
print(info)

for cast in info:
    print(cast[3])
    temperatures.append(cast[3].replace(',','.'))

highest, average = 0, 0
for i in range (len(temperatures)):

    if float(temperatures[i][1:]) > highest:
        highest=float(temperatures[i][1:])
        kod = info[i][0]

    if temperatures[i][:1] == '+':
        average+= float(temperatures[i][1:])
    if temperatures[i][:1] == '-':
        average-= float(temperatures[i][1:])

print(f'Pocet merani je {len(info)}')
print(f'Najvyssia namerana hodnota je: {highest}, namerana v {kod}')
print(f'Priemer vsetkych hodnot je: {average / len(temperatures)}')
stanice_subor.close()