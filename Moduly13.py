
result = 0
amountOfTickets = int(input("input amount of tickets "))
list_of_prices = []
for i in range(amountOfTickets):
  age = (int(input(f"input age of person for ticket number {i+1} ")))
  if (age < 18):
    list_of_prices.append(0)
  elif (17< age < 25):
    list_of_prices.append(990)
  elif (age > 25):
    list_of_prices.append(1390)
print (list_of_prices)
for j in list_of_prices:
  result += j
if (amountOfTickets > 3):
  print(f'sum to pay is {int(result - (result / 10))} (-10%)')
else:
  print (f'sum to pay is {(result)}')