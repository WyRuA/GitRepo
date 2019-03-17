a=input('请输入x=')
b=input('请输入y=')
c=input('请输入z=')
d=input('请输入w=')
e=[int(a),int(b),int(c),int(d)]
for i in range(len(e)):
    for j in range(i+1):
        if e[i]>e[j]:
            e[i],e[j]=e[j],e[i]
print('结果：',e)
