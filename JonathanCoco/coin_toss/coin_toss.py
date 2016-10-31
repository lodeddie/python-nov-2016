import random


def PerformCoinToss(numTimes):
    numHeads = 0
    numTails = 0
    numAttempts = 0
    Message = ""

    for i in range(0, numTimes):
        #coinToss = CoinToss()
        coinToss = round(random.random())
        numAttempts = numAttempts + 1

        Message = ("Attempt #{}: Thorwing a coin..").format(numAttempts)

        # heads
        if coinToss == 0:
            numHeads = numHeads + 1
            Message = Message + "Its a head!... "
        else:
            numTails = numTails + 1
            Message = Message + "Its a tail!... "

        Message = Message + ("Got {} head(s) so far and {} tail(s) so far").format(numHeads, numTails)
        printnumAttempts = numAttempts + 1
        print Message


#main cannonball
PerformCoinToss(10)
