import random
actual_num = random.randint(1,100)

guessed_wrong = True

while guessed_wrong:
    guessed_num = input("Enter a number between 1-100: ")

    if int(guessed_num)>actual_num:
        print("Too High")
    elif int(guessed_num)<actual_num:
        print("Too Low")
    elif int(guessed_num)==actual_num:
        guessed_wrong=False
        print("Perfect!")






