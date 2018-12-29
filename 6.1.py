#
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

fibs
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#
num=int(input('how many doyou want?'))
fibs=[0,1]
for i in range(num-2):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)

#
def hello_1(greeting, name):
    print('{},{}!'.format(greeting, name))
    hello_1(greeting='hello', name='world')
