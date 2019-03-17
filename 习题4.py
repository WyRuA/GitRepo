number=float(raw_input().strip())

t=5
while  abs(t*t*t-number)>0.01:
    t=t-(t*t*t*0.1-number*0.1)/(3.0*t*t)
print('%.1f',t)
