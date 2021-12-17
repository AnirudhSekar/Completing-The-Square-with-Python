import math


def completethesquare():
    doThis = True
    try:
        while doThis:
            a = int(input("What is the A value? "))
            b = int(input("What is the B value? "))
            c = int(input("What is the C value? "))
            if a == 1:
                trueb = b / a
                truebsquared = trueb / 2
                truebvalue = truebsquared ** 2
                truec = c * -1 + truebvalue  # Adds the Square of half of the b value to the c value and also changes the sign
                if trueb > 0:
                    solution1 = -1 * math.sqrt(truec) - truebsquared
                    solution2 = math.sqrt(truec) - truebsquared
                    print("Solution #1:" + " " + str(solution1))
                    print("Solution #2:" + " " + str(solution2))
                else:
                    solution1 = -1 * math.sqrt(truec) + truebsquared * -1
                    solution2 = math.sqrt(truec) + truebsquared * -1
                    print("Solution #1: 3 " + " " + str(solution1))
                    print("Solution #2: 4 " + " " + str(solution2))
            else:
                trueb = b / a
                truebsquared = trueb / 2
                truebvalue = truebsquared ** 2
                truec = c / a * -1 + truebvalue
                if trueb > 0:
                    solution1 = -1 * math.sqrt(truec) - truebsquared
                    solution2 = math.sqrt(truec) - truebsquared
                    print("Solution #1:" + " " + str(solution1))
                    print("Solution #2:" + " " + str(solution2))
                else:
                    solution1 = -1 * math.sqrt(truec) + truebsquared * -1
                    solution2 = math.sqrt(truec) + truebsquared * -1
                    print("Solution #1:" + " " + str(solution1))
                    print("Solution #2:" + " " + str(solution2))
            doYouWantToDoItAgain = input("Do you want to do it again? ")
            if doYouWantToDoItAgain == "Yes" or doYouWantToDoItAgain == "yes":
                doThis = True
            else:
                doThis = False
                print("Thank you for trying!")
    except:
        print("There is no solution to this Quadratic Equation")


completethesquare()
