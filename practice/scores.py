score1 = input("what is your score?")
score2 = input("what is your score?")
score3 = input("what is your score?")
score4 = input("what is your score?")
score5 = input("what is your score?")
score6 = input("what is your score?")
score7 = input("what is your score?")
score8 = input("what is your score?")
score9 = input("what is your score?")
score10 = input("what is your score?")

def scoregrades(number):
    for score in range(60,100):
        if score >= 60 & score <= 69:
            print "Your grade is D"
        elif score >= 70 & score <= 79:
            print "Your grade is C"
        elif score >= 80 & score <= 89:
            print "Your grade is B"
        elif score >= 90 & score <= 100:
            print "Your grade is A"
scoregrades(scores)
