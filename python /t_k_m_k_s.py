import random as rd

secenekler = ["taş", "kağıt", "makas", "kertenkele", "spock"]

dominance_tree = {
    "taş": ["makas", "kertenkele"],
    "kağıt": ["taş", "spock"],
    "makas": ["kağıt", "kertenkele"],
    "kertenkele": ["kağıt", "spock"],
    "spock": ["taş", "makas"]
}

def determining(move1, move2, dominance_status):
    if move2 in dominance_status[move1]:
        return True
    else:
        return False

skor = [0, 0]
bitir = False
while bitir == False:
    print("Sadece taş, kağıt, makas, kertenkele veya spock üzerinden hamle yapabilirsiniz \n")
    print(f"Skor: {', '.join(map(str, skor))}. Siz {skor[0]}, ben {skor[1]}")
    hamle = input("Hamlenizi Söyleyin: ").lower()
    karsi_hamle = rd.choice(secenekler)
    kazanış = determining(hamle, karsi_hamle, dominance_tree)
    if kazanış is True:
        print("Tebrikler Kazandınız!")
        print(f"Benim hamlem {karsi_hamle} idi.")
        skor[0] += 1
    else:
        print("Maalesef kaybettiniz.")
        print(f"Benim hamlem {karsi_hamle} idi...")
        skor[1] += 1
    tekrar = input("Tekrar oynamak ister misiniz? Sadece evet hayır. ").lower()
    if tekrar == "hayır":
        bitir = True
    elif tekrar == "evet":
        pass