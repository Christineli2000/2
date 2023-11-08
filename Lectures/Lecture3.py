# Use the following data for Questions 1 - 3

stk_data = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
]

# Question 1
# Write a simple for-loop to determine the amount traded
# i.e. the sum of price * volume across all dicts in stk_data
amount = 0

for i in stk_data:
    amount += i['price'] * i['volume']

print('Question 1')
print(f'The amount traded is ${amount}')
print()

# Question 2
# We are only interested in finding out whether the amount traded is more than $1000
# In reality, we might be working with a list that contains hundreds or even thousands of items
# Iterating all items in such a list might take a long time
#
# Write a for-loop that contains a break statement that can
# efficiently tell us whether the amount traded is more than $1000

amount = 0

for i in stk_data:
    amount += i['price'] * i['volume']
    if amount > 1000:
        break

print('Question 2')
print(f'The amount traded is above the threshold: {amount > 1000}')
print()

# Question 3
# We are only interested in insider trades that are large enough
# E.g. We are not interested in Lucy's trade because
# we consider the amount traded = $5.4 * 150 = $810 to be too small
# We only want to consider trades that are >= $1000
# Write a for-loop that sums up the amount traded for trades that are >= $1000

# Method 1
amount = 0

for i in stk_data:
    indiv_amount = i['price'] * i['volume']

    if indiv_amount >= 1000:
        amount += indiv_amount

print('Question 3')
print(f'Amount calculated: ${amount}')

# Method 2
amount = 0

for i in stk_data:
    indiv_amount = i['price'] * i['volume']

    if indiv_amount < 1000:
        continue

    amount += indiv_amount

print(f'Amount calculated: ${amount}')
print()


# Question 4
aapl = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
]

amzn = [
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11,
        'volume': 950,
        'ownerName': 'John',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11.2,
        'volume': 650,
        'ownerName': 'Micheal',
     },
]

ibm = [
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6,
        'volume': 300,
        'ownerName': 'John',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6.4,
        'volume': 1100,
        'ownerName': 'Micheal',
     },
]

stk_list = [aapl, amzn, ibm]

def get_insider_amount(stock_data):
    insider_amount = 0

    for stock in stock_data:
        insider_amount += stock['price'] * stock['volume']

    return insider_amount


insider_amounts = {}

for i in stk_list:
    insider_amounts[i[0]['ticker']] = get_insider_amount(i)

print('Question 4')
print(insider_amounts)
print()


# Question 5 - Challenge
stk_data = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11,
        'volume': 950,
        'ownerName': 'John',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11.2,
        'volume': 650,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6,
        'volume': 300,
        'ownerName': 'John',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6.4,
        'volume': 1100,
        'ownerName': 'Micheal',
     },
]

insider_amounts = {}

for i in stk_data:
    ticker = i['ticker']

    if ticker not in insider_amounts:
        insider_amounts[ticker] = 0

    insider_amounts[ticker] += i['price'] * i['volume']

print('Question 5')
print(insider_amounts)
print()
