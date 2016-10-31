heads = 0
tails = 0
import random
for x in range (1, 5001):
    random_num = random.random()
    round1 = round(random_num)
    if round1 == 0:
        heads = heads + 1
        print "Attempt # " + str(x) + ":" + "Throwing a coin... It's a head!... Got " + str(heads) + " head(s) so far and " + str(tails) + " so far"
    if round1 == 1:
        tails = tails + 1
        print "Attempt # " + str(x) + ":" + "Throwing a coin... It's a tails!... Got " + str(heads) + " head(s) so far and " + str(tails) + " so far"
print "Ending the program, thank you!"
