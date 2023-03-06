from random import randint

print('Willkommen beim Spiel "Zahlenratenspiel"!')
play = True
while play == True:
    print('In welchem Bereich werden wir die Zahl erraten?')
    print('Geben Sie die Grenze von 1 bis an...')
    limit = int(input())
    print('Gut gemacht!!')
    rnd = randint(1, limit)
    print(f'Erraten Sie eine Zahl von 1 bis {limit}')


    def is_valid_guess_num():
        if 1 <= int(guess_num) <= limit:
            return True
        else:
            print(f'Geben Sie bitte eine ganze Zahl von 1 bis ein {limit}?')
            return False


    count = 0
    while True:
        guess_num = int(input())
        if is_valid_guess_num() == True:
            if guess_num == rnd:
                count += 1
                print(f'Großartig! Du hast es in fünf erraten {count} Versuche!')
                break
            elif guess_num < rnd and (rnd - guess_num) <= 5:
                print('Ihre Zahl ist geringer als vorhergesagt, aber schon sehr nah dran! Versuchen Sie es erneut')
                count += 1
            elif guess_num < rnd and (rnd - guess_num) > 5:
                print('Ihre Zahl ist viel höher als erwartet! Versuchen Sie es erneut')
                count += 1
            elif guess_num > rnd and (guess_num - rnd) <= 5:
                print('Ihre Zahl ist höher als die Zahl, die Sie erraten haben, aber Sie sind der Antwort nahe! Versuchen Sie es erneut')
                count += 1
            else:
                print('Deine Zahl ist mehr als vorhergesagt, du bist weit davon entfernt - es ist kalt, brrr! Versuchen Sie es erneut')
                count += 1

    print('Willst du noch einmal spielen? (drücken Sie Ja, Nein)')
    anw = input()
    if anw.lower() == 'ja':
        play = True
        print('Gehen!')
    elif anw.lower() == 'nein':
        print('Treffen Sie mich ein andermal!')
        play = False
    else:
         print("Hoppla, Sie haben etwas falsch gedrückt. Sie müssen das Spiel neu starten, wenn Sie fortfahren möchten")