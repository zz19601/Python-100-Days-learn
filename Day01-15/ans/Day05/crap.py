##规则：玩家掷两个骰子，每个骰子点数为1-6，
# 如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，
# 则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，
# 直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。

from random import randint

def toll():
    return (randint(1,6))

def crap(): 
    toll1 = toll()
    toll2 = toll()
    if (toll1+toll2 == 7) | (toll1+toll2 == 11):
        return ('player win!')
    elif (toll1+toll2 == 2) | (toll1+toll2 == 3) | (toll1+toll2 == 12):
        return ('host win!')
    else:

        target = toll1 + toll2
        print ('the score is: %s, duel!' %(target))
        print ('target is: ' + str(target))
        while True:
            newScore = toll() + toll()
            print ('new score is: ' + str(newScore))
            if (newScore == 7): return ('host win!')
            if (newScore == target): return ('player win!')
            else: 
                print ('duel!') 
                continue

print (str(crap()))