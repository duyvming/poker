str = input("please begin your game:")
a = str.split('\t')[0]
b = str.split('\t')[1]

a = a.split(':')[1]
b = b.split(':')[1]

a_num = []
a_let = []
b_num = []
b_let = []
tag = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for i in range(5):
    a_num.append(a[3*i+1])
    a_let.append(a[3*i+2])
    b_num.append(b[3*i+1])
    b_let.append(b[3*i+2])

# print(a_num)
# print(a_let)
# print(b_num)
# print(b_let)

def switch(a):
    for i in range(5):
        if(a[i]=='T'):
            a[i]=10
        elif(a[i]=='J'):
            a[i]=11
        elif(a[i]=='Q'):
            a[i]=12
        elif(a[i]=='K'):
            a[i]=13
        elif(a[i]=='A'):
            a[i]=14
        else:
            a[i]=int(a[i])

switch(a_num)
switch(b_num)

a_num.sort()
b_num.sort()

# print(a_num)
# print(b_num)




def judge(a,b):
    #判断同花顺
    if(b[0]==b[1] and b[1]==b[2] and b[2]==b[3] and b[3]==b[4] and a[0]<a[1] and a[1]<a[2] and a[2]<a[3] and a[3]<a[4] and a[4]-a[0]==4):
        return tag[8]
    #判断铁支
    elif((a[0]==a[3] and a[3]!=a[4]) or (a[1]==a[4] and a[0]!=a[1])):
        return tag[7]
    #判断葫芦
    elif((a[0]==a[2]and a[3]==a[4])or(a[0]==a[1]and a[2]==a[4])):
        return tag[6]
    #判断同花
    elif(b[0]==b[1]and b[1]==b[2] and b[2]==b[3] and b[3]==b[4]):
        return tag[5]
    #判断顺子
    elif(a[0]<a[1] and a[1]<a[2] and a[2]<a[3] and a[3]<a[4] and a[4]-a[0]==4):
        return tag[4]
    #判断三条
    elif(a[0]==a[2] or a[1]==a[3] or a[2]==a[4]):
        return tag[3]
    #判断两对
    elif((a[0]==a[1] and (a[2]==a[3] or a[3]==a[4]))or (a[1]==a[2]and a[3]==a[4])):
        return tag[2]
    #判断对子
    elif(a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4]):
        return tag[1]
    #判断散牌
    else:
        return tag[0]

#寻找铁支最大的数
def tiezhi(a):
    if(a[0]==a[1]):
        return a[0]
    else:
        return a[1]

def hulu(a):
    if(a[0]==a[1] and a[1]==a[2]):
        return a[0]
    elif(a[1]==a[2] and a[2]==a[3]):
        return a[1]
    else:
        return a[2]

def santiao(a):
    if(a[0]==a[1] and a[1]==a[2]):
        return a[0]
    elif(a[1]==a[2] and a[2]==a[3]):
        return a[1]
    else:
        return a[2]

def liangdui(a):
    if(a[0]==a[1] and a[2]==a[3]):
        return a[0],a[2],a[4]
    elif(a[0]==a[1] and a[3]==a[4]):
        return a[0],a[3],a[2]
    else:
        return a[1],a[3],a[0]

def duizi(a):
    if(a[0]==a[1]):
        return a[0],a[4],a[3],a[2]
    elif(a[1]==a[2]):
        return a[1],a[4],a[3],a[0]
    elif(a[2]==a[3]):
        return a[2],a[4],a[1],a[0]
    else:
        return a[3],a[2],a[1],a[0]


black = judge(a_num, a_let)
print(black)
white = judge(b_num, b_let)
print(white)

if(black > white):
    print("black wins")
elif(black==white):
    if(black==8):
        if(a_num[4]>b_num[4]):
            print("black wins")
        elif(a_num[4]==b_num[4]):
            print("draw")
        else:
            print("white wins")
    elif(black==7):
        tiezhi_a = tiezhi(a_num)
        tiezhi_b = tiezhi(b_num)
        if(tiezhi_a > tiezhi_b):
            print("black wins")
        elif(tiezhi_a < tiezhi_b):
            print("white wins")
        else:
            print("draw")

    elif(black==6):
        hulu_a = hulu(a_num)
        hulu_b = hulu(b_num)
        if(hulu_a > hulu_b):
            print("black wins")
        elif(hulu_a < hulu_b):
            print("white wins")
        else:
            print("draw")
    elif(black==5):
        if (a_num[4] > b_num[4]):
            print("black wins")
        elif (a_num[4] == b_num[4]):
            if (a_num[3] > b_num[3]):
                print("black wins")
            elif (a_num[3] == b_num[3]):
                if (a_num[2] > b_num[2]):
                    print("black wins")
                elif (a_num[2] == b_num[2]):
                    if (a_num[1] > b_num[1]):
                        print("black wins")
                    elif (a_num[1] == b_num[1]):
                        if (a_num[0] > b_num[0]):
                            print("black wins")
                        elif (a_num[0] == b_num[0]):
                            print("draw")
                        else:
                            print("white wins")
                    else:
                        print("white wins")
                else:
                    print("white wins")
            else:
                print("white wins")
        else:
            print("white wins")
    elif(black==4):
        if (a_num[4] > b_num[4]):
            print("black wins")
        elif (a_num[4] < b_num[4]):
            print("white wins")
        else:
            print("draw")
    elif(black==3):
        santiao_a = santiao(a_num)
        santiao_b = santiao(b_num)
        if(santiao_a > santiao_b):
            print("black wins")
        elif(santiao_a < santiao_b):
            print("white wins")
        else:
            print("draw")
    elif(black==2):
        small_a, big_a, single_a = liangdui(a_num)
        small_b, big_b, single_b = liangdui(b_num)
        if(big_a > big_b):
            print("black wins")
        elif(big_a==big_b):
            if(small_a>small_b):
                print("black wins")
            elif(small_a==small_b):
                if(single_a>single_b):
                    print("black wins")
                elif(single_a==single_b):
                    print("draw")
                else:
                    print("white wins")
            else:
                print("white wins")
        else:
            print("white wins")

    elif(black==1):
        da,da_1,da_2,da_3 = duizi(a_num)
        db,db_1,db_2,db_3 = duizi(b_num)
        if(da>db):
            print("black wins")
        elif(da==db):
            if(da_1>db_1):
                print("black wins")
            elif(da_1==db_1):
                if(da_2>db_2):
                    print("black wins")
                elif(da_2==db_2):
                    if(da_3>db_3):
                        print("black wins")
                    elif(da_3==db_3):
                        print("draw")
                    else:
                        print("white wins")
                else:
                    print("white wins")
            else:
                print("white wins")
        else:
            print("white wins")
    elif(black==0):
        if (a_num[4] > b_num[4]):
            print("black wins")
        elif (a_num[4] == b_num[4]):
            if (a_num[3] > b_num[3]):
                print("black wins")
            elif (a_num[3] == b_num[3]):
                if (a_num[2] > b_num[2]):
                    print("black wins")
                elif (a_num[2] == b_num[2]):
                    if (a_num[1] > b_num[1]):
                        print("black wins")
                    elif (a_num[1] == b_num[1]):
                        if (a_num[0] > b_num[0]):
                            print("black wins")
                        elif (a_num[0] == b_num[0]):
                            print("draw")
                        else:
                            print("white wins")
                    else:
                        print("white wins")
                else:
                    print("white wins")
            else:
                print("white wins")
        else:
            print("white wins")
else:
    print("white wins")




