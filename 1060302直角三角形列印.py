# Q2
# 載入tkinter模組
import tkinter as tk
# 建立主視窗
root=tk.Tk()
root.title("SD Q2")
root.geometry("400x300")
# 開啟檔案讀取第一行資料
with open("data.txt","r",encoding=("utf-8")) as f:
    data=f.read()
    # data=7
# 準備結果
result=""
n=int(data)
for i in range(1,n+1):
    for x in range(1,i+1):
        result=result+str(x)
    result=result+"\n"
result="第二題結果"+"\n"+result
# 在視窗中加入標籤
label1=tk.Label(root,text=result,justify="left")
label1.pack()
root.mainloop()    