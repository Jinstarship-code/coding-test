n,l = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

start = arr[0]-0.5
end = start+l
cnt =1

for i in range(0,len(arr)):
  if start<arr[i]<end:
    continue
  else:
    cnt +=1
    start = arr[i]-0.5
    end = start+l

print(cnt)
    