total = int(input("enter amount : "))
out={}

if total//2000 >0:
    out[2000] = total//2000
    total = total % 2000
if total//500 >0:
    out[500] = total//500
    total = total % 500
if total//200 >0:
    out[200] = total//200
    total = total%200
if total//100 >0:
    out[100] = total//100
    total=total%100
if total//50 >0:
    out[50] = total//50
    total = total%50
if total//20 >0:
    out[20] = total//20
    total = total%20
if total//10 >0:
    out[10] = total//10
    total=total%10
if total//5 >0:
    out[5] = total//5
    total=total%5
if total//2 >0:
    out[2]=total//2
    total=total%2
if total//1 >0:
    out[1] = total//1
    total=total%1
print(out)

