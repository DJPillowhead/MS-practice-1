# Exercise 1
# Given an integer, return the integer with reversed digits. Note: The
# integer could be either positive or negative.

def IntReversed():
    num = input("Enter an integer! ")
    outNum = ""
    arrayNum = []

    try:
        isNegative = False

        if int(num) < 0:
            isNegative = True
            num = int(num) * -1

        strNum = str(num)

        for i in range(0, len(strNum)):
            arrayNum.append(strNum[i])

        for i in range(len(arrayNum)-1, -1, -1):
            outNum = outNum + arrayNum[i]

        if isNegative == True:
            outNum = int(outNum)*-1

        print(outNum)

    except:
        print("Invalid input!")

# IntReversed()

def OtherIntReversed():
    num = input("Enter an integer! ")

    try:
        num = int(num)

        isNegative = False

        if num < 0:
            isNegative = True
            num = int(num) * -1

        reversedNum = ""

        if num == 0:
            reversedNum = 0

        else:
            while num > 0:
                digit = int(num%10)
                reversedNum = reversedNum + str(digit)
                num = (num-digit)/10

        if isNegative == True:
            reversedNum = int(reversedNum)*-1

        print(reversedNum)

    except Exception as e:
        #print("Invalid input!")
        print(e)

# OtherIntReversed()

# Exercise 2
# For a given sentence, return the average word length. Note: Remember
# to remove punctuation first.

def AvgLength():

    sentence = input("Enter a sentence: ")

    punct = """".?!,;:'"()-[]{}\<>/@#$%^&*_~"""

    try:

        for i in sentence:
            for k in punct:
                if i == k:
                    sentence = sentence.replace(i, "")

        # print(sentence)

        counter = 0
        wordLengthArray = []

        for i in sentence:
            # print(i)
            counter = counter + 1
            if i == " ":
                wordLengthArray.append(counter-1)
                # print(counter-1)
                counter = 0

        wordLengthArray.append(counter)

        # print(wordLengthArray)

        sum = 0
        for i in wordLengthArray:
            sum = sum + i

        # print(sum)

        avgWordLength = sum/len(wordLengthArray)

        print(avgWordLength)

    except Exception as e:
        print(e)

# AvgLength()

# Exercise 3
# Given two non-negative integers num1 and num2 represented as string,
# return the sum of num1 and num2. You must not use any built-in
# BigInteger library or convert the inputs to integer directly.

# def StringToInt():
