
data = []

while True:
    target = input()
    if target =='#':
        break
    
    target,guess = target.split(" ")

    black=0
    grey=0
    white=0

    tmp = guess
    for i in range(0,len(target)):
        if target[i] == guess[i]:
            black +=1
            string_tmp1 = list(target)
            string_tmp1[i] = '0'
            string_tmp2 = list(guess)
            string_tmp2[i] ='0'
            target = "".join(string_tmp1)
            guess = "".join(string_tmp2)
            continue

    
        if i-1>=0 and target[i]==guess[i-1]:
            grey +=1
            string_tmp1 = list(target)
            string_tmp1[i] = '0'
            target="".join(string_tmp1)

            string_tmp2 = list(guess)
            string_tmp2[i-1] = '0'
            guess="".join(string_tmp2)
            continue
        elif i+1<len(target) and target[i]==guess[i+1] and target[i+1] != guess[i+1]:
            grey +=1
            string_tmp1 = list(target)
            string_tmp1[i] = '0'
            target="".join(string_tmp1)

            string_tmp2 = list(guess)
            string_tmp2[i+1] = '0'
            guess="".join(string_tmp2)
            continue

    for i in range(0,len(target)):
        for j in range(0,len(target)):
            if target[i] == guess[j] and target[i] !='0':
                white +=1
                string_tmp1 = list(target)
                string_tmp1[i] = '0'
                string_tmp2 = list(guess)
                string_tmp2[j] ='0'
                target = "".join(string_tmp1)
                guess = "".join(string_tmp2)

    data.append((tmp,black,grey,white))

for i in range(0,len(data)):
    print(f"{data[i][0]}: {data[i][1]} black, {data[i][2]} grey, {data[i][3]} white")
 
"""
        if i-1>=0 and i+1 < len(target) and target[i]==guess[i-1] and target[i]==guess[i+1] and target[i+1] != guess[i+1]:
            grey +=1
            string_tmp1 = list(target)
            string_tmp1[i] = '0'
            target = "".join(string_tmp1)

            string_tmp2 = list(guess)
            string_tmp2[i-1] = '0'
            string_tmp2[i+1] = '0'
            guess = "".join(string_tmp2)
            continue
"""