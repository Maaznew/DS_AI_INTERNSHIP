import matplotlib.pyplot as plt

x=[1,2,3,4,5,]
y=[2,4,6,8,12]
plt.plot(x,y)
plt.show()

# topic2 scatter plot
x=[1,2,3,4,5,6]
y=[12,10,8,6,4,2]
plt.scatter(x,y)
plt.show()

#topic3 bar plots
categories=['two wheelers','three wheelers','four wheelers']
values=[90000,150000,400000]
plt.bar(categories,values)
plt.show()

#topic4 customizing plots & subplots

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot([1,2,3],[1,4,9])
plt.title("line plot")
plt.subplot(1,2,2)
plt.bar(['A','B','C'],[3,7,5])
plt.title("bar chart")
plt.show()

# task1


import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months, revenue)
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD") 
plt.show()
