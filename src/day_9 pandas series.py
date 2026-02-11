# task 1

import pandas as pd

products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(products['Laptop'])

print("\nFirst two products:")
print(products[:2])

#task 2

data = pd.Series([ 85, None, 92, 45, None, 78, 55])
print(data.isnull())
print(data.fillna(0))

passed = data[data>60]
print(passed)


#task3
import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()
print(cleaned)

# Check which names contain letter 'a'
contains_a = cleaned.str.contains('a')
print(contains_a)
