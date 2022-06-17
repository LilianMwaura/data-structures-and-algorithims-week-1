#https://www.hackerrank.com/challenges/simple-array-sum/problem

# input - ar[1 2 3 4 10 11]
# output- 31
# loop through ar and find the sum


def simpleArraySum(ar):
    sum = 0 
    for i in ar:
        sum+= i
    return sum
    

