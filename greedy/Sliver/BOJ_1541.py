import re

n = input()

# codeline 6 ~ 15 ==> 앞의 0000이 있는 수를 제거 하는 과정
# -----------------------------------------------------
operatorlist = []
    # split()을 할것이기 때문에 연산자를 미리 저장해둔다.
for i in range(len(n)):
  if n[i] == '+' or n[i] == '-':
    operatorlist.append(n[i])    
    # re module을 이용해 +,-을 제외한 수를 tmp에 list로 저장시켜둔다.
tmp = re.split(r'[+-]',n)

    # lstrip으로 앞의 0이 있는 수를 제거 한다.
for i in range(len(tmp)):
  tmp[i]  = tmp[i].lstrip('0')
# --------------------------------------------
# 이제는 앞에 0이 있는 수를 제거 했으니 편하게 계산하는 작업.
n=''
for i,x in enumerate(tmp):
  n += ''.join(x)
  if i == len(tmp)-1:
    break
  n += ''.join(operatorlist[i])
    # -를 -(로 변경해주고 pcheck이란 bool값을 이용해 )을 닫을 타이밍을 체크함
    # 결론적으로, 다음 -연산자 앞에 )를 닫으면 된다.
n= n.replace('-','-(')
answer =''
pcheck = False

for i in range(len(n)):
  if n[i] == '(':
    pcheck = True
  if pcheck and n[i] == '-':
    answer +=''.join(')-')
    pcheck = False
    continue
  if pcheck and i == len(n)-1:
    answer+= ''.join(n[i]+')')
    break
  answer += ''.join(n[i])

print(answer)


"""
    0~9,+,-    ()을 이용해 최소값으로 만들어라.

    마지막 조건 000009-0000009를 제거하는게 젤 어려웠다.
    조금 돌아가는 코드 인것 같은데.. 좋은 방법이 지금은 생각나지 않는다.

"""