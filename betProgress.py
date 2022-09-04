import math

version = "1.0"

print("Craps Calculator {}\n\tBy: Marco Salsiccia".format(version))

bet = int(input("What is your initial bet? >"))
num = int(input("And rolling which number? >"))
rolls = int(input("How many rolls? >"))
power = input("Do you want to Power Press? y/n ")

if power in ['y', 'Y', 'yes', 'Yes']:
	print("Placing ${bet} on the {num} and hitting it {rolls} times; Power Press!".format(bet=bet, num=num, rolls=rolls))
else:
	print("Placing ${bet} on the {num} and hitting it {rolls} times; standard press.".format(bet=bet, num=num, rolls=rolls))

for roll in range(rolls+1):
	if num in [4, 10]:
		vig = bet * 0.05
		if vig <= 1:
			vigPay = 1
		else:
			vigPay = math.floor(vig)
	else:
		vigPay = 0

	if num in [4, 10]:
		win = bet * 2 - vigPay
	elif num in [5, 9]:
		win = bet//5 * 7
	elif num in [6, 8]:
		win = bet//6 * 7

	if vigPay == 0:
		print("{bet} wins {win}.".format(bet=bet, win=win))
	else:
		print("{bet} minus the ${vig} vig wins {win}.".format(bet=bet, vig=vigPay, win=win))

	if power in ['y', 'Y', 'yes', 'Yes']:
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
	else:
		bet *= 2