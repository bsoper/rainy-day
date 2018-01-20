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

