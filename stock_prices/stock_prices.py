
import argparse


def find_max_profit(prices):
  low = prices[0]
  profit = prices[1] - low

  for price in prices[1:]:
    profit = max(price - low, profit)
    low = min(price, low)

  return profit

#if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  #parser = argparse.ArgumentParser(description='Find max profit from prices.')
  #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  #args = parser.parse_args()

  #print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

print(find_max_profit([1050, 270, 1540, 3800, 2]))