import tkinter as tk
root=tk.Tk()
root.geometry("300x400")

with open("data.txt","r")as f:
    data=f.read()
"""
1,2
3,4
5,6
7,8
"""
n=data.split("\n")
w=[]
for i in n:
    w.append(i.split(","))

# 計算出C串列的值
c=[[0,0],[0,0]]
c[0][0]=int(w[0][0])+int(w[2][0])
c[0][1]=int(w[0][1])+int(w[2][1])
c[1][0]=int(w[1][0])+int(w[3][0])
c[1][1]=int(w[1][1])+int(w[3][1])
result=[]
for i in c:
    if i[1]<10:
        result.append("["+str(i[0])+" "*15+str(i[1])+"]")
    else:
        result.append("["+str(i[0])+" "*10+str(i[1])+"]")
result="\n".join(result)
result="第五題結果:\n"+result

lambel=tk.Label(root,text=result)
lambel.pack()
root.mainloop()
