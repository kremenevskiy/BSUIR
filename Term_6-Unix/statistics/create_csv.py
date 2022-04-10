import pandas as pd

ids = ['iphone', 'iphone', 'TV', 'Xbox', 'Mouse']
cnt = [10, 20, 30, 40, 40]
price = [500, 700, 900, 1000, 100]

# print(len(ids))
# print(len(cnt))
# print(len(price))
df = pd.DataFrame({'name': ids, 'count': cnt, 'price': price})
df.to_csv('data.csv', index=False)
