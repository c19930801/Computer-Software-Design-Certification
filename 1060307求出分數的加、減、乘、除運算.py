from tkinter import *
from tkinter import ttk
import tkinter as tk

root=tk.Tk()
root.geometry("800x400")
root.title("求出分數的加、減、乘、除運算")
# 建立 應檢人資料欄位
group=tk.LabelFrame(root,text="應檢人資料")
group.pack()
bdata=[
    ["姓名","陳自強","術科測試編號","106010203"],
    ["座號","01","考 試 日 期","2017/01/06"] ]
for i in range(2):#0 1 
    for x in range(4):# 0 1 2 3
        if x not in[1,3]:
            t=tk.Label(group,text=bdata[i][x])
        else:
            t=tk.Entry(group,width=10)
            t.insert(0,bdata[i][x])
        t.grid(row=i,column=x)
# 讀取檔案資料
with open("data.txt","r")as f:
    data=f.read()
data=data.split("\n")
# 計算結果並儲存
gd=[]
for i in data:
    b,a,op,y,x=i.split(",")
    b,a,y,x=int(b),int(a),int(y),int(x)
    if op=="+":
        top=b*x+a*y
        down=a*x
    elif op=="-":
        top=b*x-a*y
        down=a*x
    elif op=="*":
        top=(b*x)*(a*y)
        down=(a*x)**2
    elif op=="/":
        top=b*x
        down=a*y
    # 約分
    gcd=1
    for i in range(1,top):
        if top % i==0 and down % i==0:
            gcd=i
    top=top//gcd
    down=down//gcd
    # 輸出格式
    a1=str(b)+"/"+str(a)
    a2=str(y)+"/"+str(x)
    ans = str(int(top))+"/"+str(int(down))
    if top==down:
        ans=1
    elif top==0:
        ans==0
    t=[a1,op,a2,ans]
    gd.append(t)
# 結果表格區
hname=["數字1","運算","數字2","結果"]
tree=ttk.Treeview(root,column=hname,show="headings")
for i in hname:
    tree.column(i,anchor=CENTER)
    tree.heading(i,text=i)
for i in range(len(gd)):
    tree.insert("","end",text="1",values=gd[i])
tree.pack()
root.mainloop()