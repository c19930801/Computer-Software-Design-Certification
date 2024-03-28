from tkinter import *
from tkinter import ttk
import tkinter as tk
root=tk.Tk()
root.geometry("800x400")
root.title("身分證號碼檢查")
# 建立群組
group=tk.LabelFrame(root,text="應檢人資料")
group.pack()
# 建立表格資料
bdata=[
    ["姓名","王小美","術科測試編號","11101123"],
    ["座號","60","考 試 日 期","2023-12-18"]
       ]
# 在群組中建立表格
for rowN in range(2):#0 1
    for columnN in range(4):#0 1 2 3
        if columnN not in [1,3]: # 0.2
            t=tk.Label(group,text=bdata[rowN][columnN])
        else:#1.3
            t=tk.Entry(group,width=10)
            t.insert(0,bdata[rowN][columnN])
        t.grid(row=rowN,column=columnN)
# 讀取檔案資料並檢查身分證號碼
with open("identity.txt","r",encoding=("utf-8"))as f:
    data=f.read()
data=data.split("\n")
gd=[]
for i in data:
    errMsg=""
    idno,name1,sex=i.strip().split(",")
    #格式檢查
    Ll=idno[0] # 開頭英文
    d=[0]*10
    for i in range(1,10): # 1 2 3 4 5 6 7 8 9
        if "9">=idno[i]>="0":
            d[i]=int(idno[i])
        else:
            errMsg="格式錯誤"
    if errMsg=="":
        # 性別檢查
        if (d[1])==1 and sex=="F" or d[1]==2 and sex=="M":
            errMsg="性別代碼錯誤"
    
    if errMsg=='':
        # 安全碼檢查
        fn="ABCDEFGHJKLMNPQRSTUVXYWZIO".find(Ll)+10
        x1=fn//10
        x2=fn%10
        y=x1+9*x2
        k=8
        for j in range(1,8):#1.2.3.4.5.6.7
            y=y+k*d[j]
            k=k-1
        y=y+d[8]+d[9]
        if not(y%10==0):
            errMsg="驗證錯誤"
    t=[idno,name1,sex,errMsg]
    gd.append(t)
# 將檢查後的資料以ID NO順序排序,並建立表格
gd.sort()
hname=["ID NO","NAME","SEX","ERROR"]
tree=ttk.Treeview(root,column=hname,show="headings")
for i in hname:
    tree.column(i,anchor="w")
    tree.heading(i,text=i,anchor="w")
for i in range(len(gd)):
    tree.insert("","end",text="1",values=gd[i])
tree.pack()

root.mainloop()