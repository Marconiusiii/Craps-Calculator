# Craps Calculator v.1.0
A bet progression calculator for the game of Craps.

## Purpose

This is a small script that will generate a betting progression for a Place number in Craps. The script will ask you for your starting bet amount, the number you are simulating, how many rolls you want to simulate, and whether or not you want to show the Power Press progression or amounts.

A standard press in Craps just means that the initial bet is doubled with every hit on that number. A power press is adding money to the winnings to press the bet up to the next closest unit.

### Place 4 and 10

The 4 and 10 are set to an auto-buy progression, meaning that each win will pay true odds of 2:1 minus the 5% commission/vig. This will reflect in the winnings shown in the calculator output. Normally, the 4 and 10 pay out 9:5, but most casinos now have an auto-buy set in place for bets of $10 or more.

### Place 5 and 9

The 5 and 9 pay out 7:5, and all bets must be made in a multiple of 5. The exception is a $36 bet which will pay out $50 when rounded by the dealers.

### Place 6 and 8

The 6 and 8 pay out 7:6, so all bets must be made in multiples of 6. There are some extra exceptions with a $25 bet, but those are not reflected in the calculator.