a=input('请输入x=')
b=input('请输入y=')
c=input('请输入z=')
w=[int(a),int(b),int(c)]
for i in range(len(w)):
    for j in range(i+1):
        if w[i]<w[j]:
            w[i],w[j]=w[j],w[i]
print('结果：',w)

