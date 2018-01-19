from Expenditure import Expenditure
from Income import Income
from Enum import TimeFrames

class Application:
	expenditures = []
	total_expenditure = 0.0

	incomes = []
	total_monthly_income = 0.0

	current_savings = 0.0
	daily_allowance = 0.0

	def printExpenditures(self):
		print self.expenditures

	def printIncomes(self):
		print self.incomes

	def printInformation(self):
		self.printExpenditures()
		self.printIncomes()


	def __init__(self):
		return

	def addExpenditure(exp):
		return

	def addIncome(inc):
		return

	def calculateDailyAllowance():
		return



app = Application()

app.expenditures.append(Expenditure('rent', 1000.0, 0, TimeFrames.MONTH))
app.expenditures.append(Expenditure('car', 200.0, 700, TimeFrames.MONTH))

app.incomes.append(Income('work', 3000.0, 0, TimeFrames.MONTH))

app.printInformation()