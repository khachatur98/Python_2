market = {'dairy': ['yogurt','cheese'],
          'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana','banana']}
print(market)

market['candies'] =  ['mars', 'kinder', 'twix']

market['fruits'] = sorted(list(set(market['fruits'])))

print(market)