from Enum import TimeFrames
from datetime import datetime

def timeFrameToDays(time_frame):
	if time_frame == TimeFrames.DAY:
		return 1
	elif time_frame == TimeFrames.WEEK:
		return 7
	elif time_frame == TimeFrames.MONTH:
		days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		now = datetime.now()
		current_month = now.month
		return days_in_months[current_month - 1]
	elif time_frame == TimeFrames.YEAR:
		return 365

def daysRemaining(remaining_payments, time_frame):
	return (remaining_payments * timeFrameToDays(time_frame))