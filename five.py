def calculate_interest(principal , rate , time = 1):
  interest = (principal * rate * time) / 100
  return interest


principal = 100
rate = 5
time = 1

total_interest = calculate_interest(principal, rate , time)

print("Total interest is : " , total_interest)

