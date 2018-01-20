from Expenditure import Expenditure
from Income import Income
import Helper

class Application:
	expenditures = []

	incomes = []

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



app = Application()

app.expenditures.append(Expenditure('rent', 1000.0, 0, TimeFrame.MONTH))
app.expenditures.append(Expenditure('car', 200.0, 700, TimeFrame.MONTH))

app.incomes.append(Income('work', 3000.0, 0, TimeFrame.MONTH))

app.printInformation()