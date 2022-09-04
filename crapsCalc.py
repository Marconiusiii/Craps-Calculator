import math
import os

version = "1.0"

print("Craps Calculator {}\n\tBy: Marco Salsiccia".format(version))

while True:

	while True:
		num = int(input("Which number are you Placing? >"))
		if num not in [4, 5,6, 8, 9, 10]:
			print("That's not a box number! Try again.")
			continue
		else:
			break
	while True:
		try:
			bet = int(input("What is your initial bet? >"))
			break
		except ValueError:
			print("That wasn't a number, dingus. Try again!")
			continue
		if num in [4, 5, 9, 10] and bet % 5 != 0:
			print("Your starting bet needs to be a multiple of 5 when Placing the {}! Try again...".format(num))
			continue
		elif num in [6, 8] and bet % 6 != 0:
			print("Your starting bet must be a multiple of 6 when Placing the {}! Try again...".format(num))
			continue
		else:
			break
	while True:
		try:
			rolls = int(input("How many rolls? >"))
			break
		except ValueError:
			print("I don't even know how you'd expect to roll that. Try again!")
			continue
			
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
			if addBet > 0 and roll != rolls:
				print("\tPower Pressing up ${}.".format(addBet))
				addBet = 0
			bet = nextBet
		else:
			bet *= 2

	again = input("Start over? y/n > ")
	if again in ['y', 'Y', 'yes', 'Yes']:
		continue
	else:
		raise SystemExit
