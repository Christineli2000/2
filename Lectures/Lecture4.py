
watch_list = ['QAN.AX', 'CBA.AX', 'BHP.AX']

active_list = ['CBA.AX', 'BHP.AX', 'NAB.AX', 'WBC.AX', 'RIO.AX']

buy_stocks_list = []
for stock in active_list:
    if stock in watch_list:
        buy_stocks_list.append(stock)

print('Task 1A:')
print(buy_stocks_list)
print()

# TASK 1B:
# Use a list comprehension to create a list called buy_stocks that contain stocks
# that are in present in both watch_list and active_list

buy_stocks_list = [stock for stock in active_list if stock in watch_list]

print('Task 1B:')
print(buy_stocks_list)
print()

def buy_how_many(ticker):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_shares = 0
    for i in ticker[:3]:
        num_shares += alphabet.index(i) + 1
    return num_shares


print('Task 2:')
for stock in buy_stocks_list:
    print(f'Buy {buy_how_many(stock)} shares of {stock}')
print()

buy_stock_dict = {}
for stock in buy_stocks_list:
    buy_stock_dict[stock] = buy_how_many(stock)

print('Task 3A:')
print(buy_stock_dict)
print()

buy_stock_dict = {stock: buy_how_many(stock) for stock in buy_stocks_list}

print('Task 3B:')
print(buy_stock_dict)
print()
