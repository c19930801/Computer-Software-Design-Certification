# Q1
#載入 tkinter 模組
import tkinter as tk
# 建立視窗
window=tk.Tk()
window.title("SD Q1")
window.geometry("400x300") #設定視窗大小
#開啟檔案,讀取第一行資料
with open("data.txt","r")as f:
    data=f.read()
    #讀取資料到變數data中
result=""
if data==data[::-1]:# [::-1] 把順序全倒過來
    result=data+"是回文"
else:
    result=data+"不是回文"
result="第一題結果是:"+result
#在視窗上新增一個標籤,顯示結果
result_label=tk.Label(window,text=result)
result_label.pack()
#開始執行視窗的主迴圈
window.mainloop()
