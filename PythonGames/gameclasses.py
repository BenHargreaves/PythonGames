class Game:
    def __init__(self, noOfQuestions = 0):
        _noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            print("\nMininum Number of Questions = 1\nHence, number of questions will be set to 1")
            self._noOfQuestions = 1
        elif value > 10:
            print("\nMaximum Number of Questions = 10\nHence, number of questions will be set to 10")
            self._noOfQuestions = 10
        else:
            self._noOfQuestions = value


class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint

        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input(f'Conver the number {base10} to binary: ')
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print("Correct!!")
                        score = score + 1
                        break
                    else:
                        print("Incorrect :(")
                        print("The correct answer is: {:b}".format(base10))
                        break
                except:
                    print("\nYou have entered an invalid binary number. Please try again\n")
                    userResult = input(f"Please convert {base10} to binary: ")

        return score


class MathGame(Game):
    def generateQuestions(self):
        from random import randint

        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}

        for i in range(self.noOfQuestions):
            for index in range(0, 5):
                numberList[index] = randint(1, 9)

            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == "**":
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1,4)]

            questionString = str(numberList[0])
            for index in range(0, 4):
                questionString = questionString + symbolList[index] + str(numberList[index+1])

            result = eval(questionString)
            questionString.replace("**", "^")

            userResult = input(f"\nWhat is the answer to the following Equation:\n{questionString} = ")

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Correct!!")
                        score = score + 1
                        break
                    else:
                        print("\nIncorrect :( ")
                        print(f"The Correct answer was {result}")
                        break
                except:
                    print("You've entered an answer in an invalid format. Please try again")
                    userResult = input(f"What is the answer to the following Equation:\n{questionString} = ")

        return score
