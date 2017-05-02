# f = open('score.txt')
# data = f.read()
# f.close()
# print(data)

f = open('score.txt')
lines = f.readlines()
f.close()

results = []
for line in lines:
    data = line.split()
    print(data)
    sum_score = 0
    for i in data[1:]:
        sum_score+=int(i)
    result = '{0}, \t:{1}, \n'.format(data[0],sum_score)
    results.append(result)
    
f = open('result.txt','w')
f.writelines(results)
f.close()
    
    