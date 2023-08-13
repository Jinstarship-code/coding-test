def solution(answers):
    t=[]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1=0
    cnt2=0
    cnt3=0
    i=0
    j=0
    k=0
    
    for answer in answers:
        if answer == p1[i]:
            cnt1 += 1
        if answer == p2[j]:
            cnt2 += 1
        if answer == p3[k]:
            cnt3 += 1
            
        i+=1
        j+=1
        k+=1
        if i == 5 :
            i = 0
        if j == 8:
            j = 0
        if k == 10:
            k = 0
            
    print(cnt1)
    print(cnt2)
    print(cnt3)
    if cnt1 > cnt2:
        if cnt1 > cnt3:
            t.append(1)
        elif cnt1 < cnt3:
            t.append(3)
        else:
            t.append(1)
            t.append(3)
    elif cnt1 < cnt2:
        if cnt2 > cnt3:
            t.append(2)
        elif cnt2 < cnt3:
            t.append(3)
        else:
            t.append(2)
            t.append(3)
    else:
        if cnt1 > cnt3:
            t.append(1)
            t.append(2)
        elif cnt1 < cnt3:
            t.append(3)
        else:
            t.append(1)
            t.append(2)
            t.append(3)
    
    
    return t

"""
 This is Hard Coding
"""