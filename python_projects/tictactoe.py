print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")

tahta = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

def yazTahta(tahta):
    
    print(tahta['1'] + '|' + tahta['2'] + '|' + tahta['3'])
    print("-+-+-")
    print(tahta['4'] + '|' + tahta['5'] + '|' + tahta['6'])
    print("-+-+-")
    print(tahta['7'] + '|' + tahta['8'] + '|' + tahta['9'])
    
def kimKazandi(tahta , simge):
    
    if tahta['1'] == tahta['2'] == tahta['3'] == simge:     #Yatay
        return True  
    elif tahta['4'] == tahta['5'] == tahta['6'] == simge:
        return True
    elif tahta['7'] == tahta['8'] == tahta['9'] == simge:
        return True
    
    elif tahta['1'] == tahta['4'] == tahta['7'] == simge:   #Dikey
        return True
    elif tahta['2'] == tahta['5'] == tahta['8'] == simge:
        return True
    elif tahta['3'] == tahta['6'] == tahta['9'] == simge:
        return True
    
    elif tahta['1'] == tahta['5'] == tahta['9'] == simge:   #Çarpraz
        return True
    elif tahta['3'] == tahta['5'] == tahta['7'] == simge:
        return True
    
    else:
        return False
    
simge = "X"

for i in range (9):
    print(simge + ", nereye yerleştirilsin?")
    gir = input()
    tahta[gir] = simge
    if simge == "X":
        simge = "O"
    else:
        simge = "X"
    yazTahta(tahta)
    
    if kimKazandi(tahta , "X"):
        print("Oyunu 'X' kazandı")
        break
    if kimKazandi(tahta , "O"):
        print("Oyunu 'O' ")
        break
    
if kimKazandi(tahta , "O") == False and kimKazandi(tahta , "X") == False:
    print("Oyun berabere kaldı..  :/")    
        