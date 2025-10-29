import random 

memory = { 
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
while True:
    input("Press Enter to roll the dice: ")
    random_number = random.randint(1, 6)
    print("You rolled a", random_number)
    print("Rolling history:")
    memory[random_number] += 1
    print(memory)
    play_again = input("Do you want to roll again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
