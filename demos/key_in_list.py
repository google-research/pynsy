d = range(10000)
e = range(50)
queries = [-1, 9, 100000, -100000]
for query in queries:
  if query in d:  # Slow
    print(f'Found {query}')
  if query in e:
    print(f'Found {query}')
