#!/usr/bin/python
from Enum import TimeFrames

class Income:
	Label = ''
	amount = 0.0
	remaining_payments = 0
	time_frame = TimeFrames.MONTH
	daily_income = 0.0

	def __init__(self, label, amount, remaining_payments, time_frame):
		self.label = label
		self.amount = amount
		self.remaining_payments = remaining_payments
		self.time_frame = time_frame
		self.daily_income = self.amount / timeFrameToDays(self.time_frame)

	def __repr__(self):
		return '(Income: ' + ', '.join([self.label, str(self.amount), str(self.remaining_payments), str(self.time_frame)]) + ')'
