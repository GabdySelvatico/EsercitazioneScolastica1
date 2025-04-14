import datetime
import random
#PAOLETTI GABRIELE 4G

#TRACCIA: scrivere un programma in python che simuli il funzionamento di una scelta su menù del MCDonald

spesa = 0 # HO CREATO UNA VARIABILE CHIAMATA "spesa" PER CALCOLARE LA SPESA TOTALE
num = random.randint(1, 10)
conta = 0


while conta == 0:
print("Salve, benvenuto al McDonald!")
print("Scegli un panino tra i seguenti:\n")

print("1) BIG MAC - - 7€")
print("2) CRISPY MC BACON - - 5.80€")
print("3) MC CHICKEN - - 4.80€\n")

print("- - - - - - - - - - - - - - - - ")

scelta = int(input()) #COMANDO PER SCRIVERE IN INPUT UN NUMERO INTERO, IN QUESTO CASO SERVIRA' PER SCEGLIERE IL PRODOTTO

print("- - - - - - - - - - - - - - - - \n")

if scelta == 1:
    spesa = spesa + 7
elif scelta == 2:
    spesa = spesa + 5.8        #IF, ELIF, ED ELSE PER STABILIRE QUALE SCELTA PRENDERA' L'UTENTE
elif scelta == 3:
    spesa = spesa + 4.8
else:
    print("ERRORE, non hai selezionato un panino presente nel menù")

print("Perfetto, scelga un secondo:\n")

print("1) PATATINE - - 3.50€")
print("2) NUGGETS - - 4.80€")
print("3) ALETTE DI POLLO - - 3.50€\n")

print("- - - - - - - - - - - - - - - - ")

scelta2 = int(input())

print("- - - - - - - - - - - - - - - - \n")

if scelta2 == 1:
    spesa = spesa + 3.5
elif scelta2 == 2:
    spesa = spesa + 4.8
elif scelta2 == 3:
    spesa = spesa + 3.5
else:
    print("ERRORE, non hai selezionato un panino presente nel menù")

print("Ottimo, ora il dessert:\n")
print("1) CAFFE' - - 1.20€")
print("2) MC FLURRY - - 2.80€")
print("3) MILKSHAKE - - 3.50€\n")

print("- - - - - - - - - - - - - - - - ")

scelta3 = int(input())

print("- - - - - - - - - - - - - - - - \n")

if scelta3 == 1:
    spesa = spesa + 1.2
elif scelta == 2:
    spesa = spesa + 2.8
elif scelta3 == 3:
    spesa = spesa + 3.5
else:
    print("ERRORE, non hai selezionato un panino presente nel menù")
    

ciclo = (input())    
print("Vuoi ordinare un altro menù?")
if ciclo = "si" or "Si":
    print("prego ordini un altro menù")
else:
    conta +=1
    break

print("Grazie per la pazienza, deve pagare:", spesa)
print("Preferisce pagare con carta o contante? Se desidera usare il contante, la prossima volta che verrà al McDonegani")
print("riceverà un buono del 10% di sconto!")

scelta4 = (input())

if scelta4 == "Carta":
    print("Perfetto, ecco il buono del 10% valido per la prossima volta che verrà")
else:
    print("Perfetto. Grazie per essere venuto!")

file = open("Scontrino.txt","a")

file.write("Spesa totale: " + str(spesa) + "   " + "Data dell'acquisto: " + str(datetime.datetime.now) + "   " + "Numero ordine: " + str(num) + "\n")

file.close()




