#https://www.hackerrank.com/challenges/no-idea/problem

'''
3 2
1 5 3
3 1
5 7
'''

sizes = input().split(" ")
inputMain = [int(numStr) for numStr in input().split(" ")]

likes = set([int(numStr) for numStr in input().split(" ")])
dislikes = set([int(numStr) for numStr in input().split(" ")])

happines = 0

for i in inputMain:
    if i in likes:
        happines += 1
    elif i in dislikes:
        happines -= 1

print(happines)
