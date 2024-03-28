from tkinter import *
from tkinter import ttk
import tkinter as tk
# 建立視窗
root=tk.Tk()
root.geometry("800x400")
root.title("樸克牌比大小")
# 建立應檢人資料框架
group=tk.LabelFrame(root,text="應檢人資料")
group.pack()
# 建立應檢人資料
bdata=[
["姓名","王小美","術科測試編號","11101123"],
["座號","60","考試日期","2023-12-20"] ]
for i in range(2):
    for x in range(4):
        if x not in[1,3]:
            t=tk.Label(group,text=bdata[i][x])
        else:
            t=tk.Entry(group,width=10)
            t.insert(0,bdata[i][x])
        t.grid(column=x,row=i)
# 讀取資料
with open("data.txt","r") as f:
    data=f.read()
data=data.split("\n")
n=int(data[0])
rd=[]
for i in range(1,len(data)):
    t=int(float(data[i])*52)
    rd.append(t)
# rd [42, 42, 6, 35, 46, 26, 0, 6, 14, 42, 24, 46, 22, 5, 47, 1]
#　去重復，計算比大小
gd=[]
rd1=[]
for i in rd:
    if i not in rd1:
        rd1.append(i)
#rd1 [42, 6, 35, 46, 26, 0, 14, 24, 22, 5, 47, 1] 無重復
j=1
for i in range(0,n*2,2): #0 2 4 6 8
    p=rd1[i]   #p:玩家 42
    pn=p%13+1  #pn:玩家牌數字 5
    pf=p//13  #pf:玩家牌花色 3
    b=rd1[i+1] #b:莊家 6
    bn=b%13+1  #bn:莊家牌數字 7
    bf=b//13   #bf:莊家牌花色 0
    msg=""
    if pn>bn:
        msg="玩家贏"
    if pn==bn:
        msg="平手"
    if pn<bn:
        msg="莊家贏"
    rn=["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    rf=["\u2660","\u2665","\u2666","\u2663"] # 牌花色utf-8碼
    t=[j,rf[pf]+rn[pn],rf[bf]+rn[bn],msg]
    gd.append(t)
    j=j+1
# 建立結果表格
hname=["序號","玩家","莊家","結果"]
tree=ttk.Treeview(root,column=hname,show="headings")

for i in hname:
    tree.column(i)
    tree.heading(i,text=i)

for i in range(len(gd)):
    tree.insert("","end",text="1",values=gd[i])
tree.pack()

root.mainloop()
