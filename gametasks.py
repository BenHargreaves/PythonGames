def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        file = open("userScores.txt", "r")
        for line in file:
            content = line.strip().split(', ')
            if content[0] == userName:
                file.close()
                return content[1]
        file.close()
        return -1
    except IOError:
        print("File doesn't exist. Creating new userScores.txt file")
        file = open("userScores.txt", "w")
        file.close()
        return -1


def updateUserScore(newUser, userName, score):
    from os import remove, rename

    if newUser == True:
        file = open("userScores.txt", "a")
        file.write(userName + ", " + score + "\n")
        file.close()
    else:
        tempFile = open("userScores.tmp", "w")
        userFile = open("userScores.txt", "r")

        for line in userFile:
            content = line.split(', ')
            if content[0] == userName:
                tempFile.write(userName + ', ' + score + "\n")
            else:
                tempFile.write(line)

        tempFile.close()
        userFile.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")
