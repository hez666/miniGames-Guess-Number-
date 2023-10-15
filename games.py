import random

print ("Guess the number !")

number = random.randint(1, 10)

guess = None
 
while guess != number:
    guess = int(input("Masukan Tebakan anda: "))

    if guess < number:
        print("Rendah!")
    elif guess > number:
        print("Ketinggian!")
    else: 
        print("Anda benar! tebakan anda adalah", number)
    
print("Game Over!")


