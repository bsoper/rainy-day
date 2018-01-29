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

	def addExpenditure(self, label, amount, remaining_payments, time_frame):
		expenditure = Expenditure(label, amount, remaining_payments, time_frame)
		self.expenditures.append(expenditure)
		return

	def getTotalMonthlyExpenditure(self):
		total_monthly_expenditure = 0.0
		for expenditure in self.expenditures:
			total_monthly_expenditure += expenditure.daily_expenditure * min(Helper.timeFrameToDays(TimeFrame.MONTH), 
				Helper.daysRemaining(expenditure.remaining_payments, expenditure.time_frame))

	def addIncome(self, label, amount, remaining_payments, time_frame):
		income = Income(label, amount, remaining_payments, time_frame)
		self.incomes.append(income)
		return

	def calculateDailyAllowance():
		return

