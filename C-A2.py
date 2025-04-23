import random
min = int(input("min värde:"))
max = int(input("max värde:"))
mål = int(input("Vilken tal vill du söka kompinationer till?: "))
lista = [x for x in range(min,max+1)]
random.shuffle(lista)
svar =[]

for i in lista:
    for j in lista[::-1]: 
        if i != j:
            if j + i == mål:
                svar.append((j,i))
        
print(svar)