input = [100,200,300,400,500]
compared_num = [500,200,400]

for i in range(len(input)):
    if input[i] in compared_num:
        input[i] = 0

print(input)
 
 