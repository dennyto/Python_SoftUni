work_days = int(input())
daily_wage = float(input())
dollar_rate = float(input())

rate_in_lv = daily_wage * dollar_rate
monthly_salary = rate_in_lv * work_days
yearly_salary = monthly_salary * (12 + 2.5)
yearly_salary = yearly_salary * 0.75
average_daily = yearly_salary / 365

print('{:.2f}'.format(average_daily))
