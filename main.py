from rhp_defs import *

#raceform = "raceform.pdf"

data = scrambledText(raceform)

text = cleanUp(data)

data1 = cleanTimes(text)

nextStep(data1)

print(data1)

