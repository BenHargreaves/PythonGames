from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, MathGame, BinaryGame

try:
    mathInstructions = "In this game, you will be given a simple arithmetic question.\n\nEach correct answer gives you one point.\nNo points are deducted for incorrect answers."
    binaryInstructions = "In this game, you will be given a number in base 10,\nYour task is to convert this number to base 2 (binary)\n\nEach correct answer gives you one point\nNo points are deducted for incorrect answers."
    userChoice = 0

    bg = BinaryGame()
    mg = MathGame()

    userName = input("Enter your User Name (Will be created if user doesnt exist): ")
    score = int(getUserScore(userName))
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print(f"\n\nWelcome {userName} - Your Current score is {score}")

    while userChoice != 'exit':
        game = input('Math Game(1) or Binary Game(2) ? ')
        while game != '1' and game != '2':
            print('Please only enter either \'1\' for Math Game, or \'2\' for the Binary Game\n')
            game = input('Math Game(1) or Binary Game(2) ? ')

        numPrompt = input("How many questions do you want per game (1 to 10)? ")
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("Please enter a valid integer number")
                numPrompt = input("How many questions do you want per game (1 to 10)? ")

        if game == '1':
            mg.noOfQuestions = num
            printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()

        print(f'\n\nYour current score after the last round of questions is {score}')
        userChoice = input("\nPlease press enter to continue, or type 'exit' to stop playing\n")

    updateUserScore(newUser, userName, str(score))

except Exception as e:
    print("Unknown error occurred. Program will now exit.")
    print("Error: ", e)
