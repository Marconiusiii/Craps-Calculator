import math

print("Marco's Craps Bet Progression Calculator\n")

bet = int(input("What is your initial bet? >"))

num = int(input("And rolling which number? >"))

for roll in range(8):
	vig = bet * 0.05
	if vig <= 1:
		vigPay = 1
	else:
		vigPay = math.floor(vig)

	if num in [4, 10]:
		win = bet * 2 - vigPay
	elif num in [5, 9]:
		win = bet//5 * 7
	elif num in [6, 8]:
		win = bet//6 * 7
	print("{bet} wins {win}.".format(bet=bet, win=win))
	nextBet = bet + win
	addBet = 0
	if num not in [6, 8]:
		while nextBet % 5 != 0:
			nextBet += 1
			addBet += 1
	else:
		while nextBet % 6 != 0:
			nextBet += 1
			addBet += 1
	if addBet > 0:
		print("\tPower Pressing up ${}.".format(addBet))
		addBet = 0
	bet = nextBet