from matplotlib import pyplot

minimum = 0
maximum = 100
x = list()
y = list()

for i in range(minimum,maximum):
    j = i
    count = 0
    while j>1:
        x.append(count)
        y.append(j)
        if j % 2 == 0: #Is a pair number
            j = j /2
        else: #Is an odd number
            j = (3*j)+1
        count = count +1
    
    pyplot.plot(x, y, color='black')
    print(i," took ",count," steps until reaching 1")
 
pyplot.show() 
