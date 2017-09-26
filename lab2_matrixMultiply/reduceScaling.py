import matplotlib.pyplot as plt
reduceScale = [1,2,4,8,16,32,64,128]
mapTime, = plt.plot(reduceScale, [17,16,16,16,21,16,16,15], 'ro')
reduceTime, = plt.plot(reduceScale,[30,18,12,9,8,7,11,12],'g^')
plt.xlabel('Number of reducers')
plt.ylabel('Runtime')
plt.title('Reduce Scaling')
plt.legend(["mapTime", "reduceTime"])

plt.show()