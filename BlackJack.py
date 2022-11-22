import random
import os
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
a=input("Dp you wamt to play BlackJack? Type 'y' or 'n':\n")
def blackjack():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    card1=[]
    card2=[]
    a=0
    csum=0
    for card in range(0,2):
        card=random.choice(cards)
        card1.append(card)
        a+=card
    for cds in range(0,2):
        cds=random.choice(cards)
        card2.append(cds)
        csum+=cds
    print(f"Your cards: {card1}, current score: {a}")    
    b=card2[0]
    print(f"Computer's First Card: {b}") 
    hitting=True 
    while hitting:
        hit=input("Type 'y' to get another card, type 'n' to pass:\n")    
        if hit=="n":
            break
        for c in range(0,1):
            c=random.choice(cards)
            a+=c
            if a>21:
                if c==11:
                    card=1
                    c=1
                    a-=10
            card1.append(c)
        print(f"Your Cards: {card1}, total score: {a}")
        print(f"Computer's first card: {b}")
        if a>21:
            print(f"Your score is {a}\nYou Lose..😭")
            break
        
        
    if hit=="n":
        print(f"Your final hand: {card1}, final score:  {a}")
        while csum<17:
            for c2 in range(0,1):
                c2=random.choice(cards)
                card2.append(c2)
                csum+=c2
            if csum>21:
                print(f"Computer's score is: {csum}.. Your score is {a}.\nYou win..🙌😎")
                break
        if csum<21:
            print(f"Computer's final hand: {card2}, final score: {csum}")          
    
    if hit=="n":
        if a<21 and csum<21:
            if a>csum:
                print("You Win..🙌😎")
            else:
                print("You lose..😭")
        elif a==csum:
            print("Match is draw..✌️")
        exit
    again=input("Do you want to play BlackJack? Type 'y' or 'n'.\n")
    if again=="y":
        os.system('cls')
        blackjack()
    else:
        exit
    
            
            
            
        
        
if a == "y":
    os.system('cls')
    blackjack()
else:
    exit