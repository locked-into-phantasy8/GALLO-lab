def pront (arg):
    print(arg)
fattore = []

for i in range(11):
    fattore.append(i)


tabellina = []

tav_pitagorica = []

for j in range(11):
    tabellina = []
    for i in range(11):
        tabellina.append(fattore[i]*fattore[j])
    tav_pitagorica.append (tabellina)
        
pront(tav_pitagorica[3][4])