'''读入txt文件'''
import codecs
f = codecs.open('yq_in.txt',"r") # 打开txt文件，以"utf-8'编码读取
line = f.readline() # 以行的形式进行读取文件
list1 = []
list2 = []
tup_data=(())
tup_data1=(())
while line:
    a = line.split()
    b = a[0:3] # 这是选取需要读取的位数
    c = a[0:1]
    list2.append(c)
    list1.append(b) # 将其添加在列表之中
    line = f.readline()
f.close()
for i in list2:
        tup2 = tuple(i)
        tup_data1 += ((tup2))
for i in list1:
    tup1=tuple(i)
    tup_data+= ((tup1),)
    '''实现功能函数'''
def merger(tup):
    sta = set()#set方法排列是无序的，利用集合的特性去重
    str_lis = []
    ok = []
    for x,y,z in tup:#将每列第一个元素提取
        sta.add(x)
   #将无序set排列按原来顺序重新排列
    addr_to = list(set(tup_data1))
    addr_to.sort(key=tup_data1.index)
    for m in addr_to:
        for n,p,q in tup:
            if m == n:
                str_lis.append('\n'+p+' '+q)
                str = ' '.join(str_lis)
                str = m+str
        ok.append(str)
        str_lis=[]
    return '\n'.join(ok)
tup = tup_data
#print(merger(tup))
'''将文件写入ty_out.txt文件中'''
with open("yq_out.txt","w") as o:
    for i in merger(tup):
        o.write(i)
