day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
a,b = map(int, input().split())

a -= 1
b -= 1
answer = 0
arr=[31,28,31,30,31,30,31,31,30,31,30]
for i in range(a):
  answer += arr[i]

answer += b
print(day[answer%7])


"""
* 7,8월은 31일까지 있다!

"""