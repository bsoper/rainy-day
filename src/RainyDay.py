#!/usr/bin/python
from Application import Application
from Expenditure import Expenditure
from Enum import TimeFrames
from Income import Income

def main():
	app = Application()

	app.run()


	# app.expenditures.append(Expenditure('rent', 1000.0, 0, TimeFrames.MONTH))
	# app.expenditures.append(Expenditure('car', 200.0, 700, TimeFrames.MONTH))

	# app.incomes.append(Income('work', 3000.0, 0, TimeFrames.MONTH))

	# app.printInformation()


if __name__ == "__main__":
    main()