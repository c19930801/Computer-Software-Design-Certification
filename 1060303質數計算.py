import tkinter as tk
root=tk.Tk()
root.title("SD Q3")
root.geometry("300x400")

with open("data.txt","r")as f:
    data=f.read()
    #data=12
n=int(data)
result=""
for i in range(2,n):
    if n%i==0:
        result="第三題結果:"+str(n)+" is not a prime number"
    else:
        result="第三題結果:"+str(n)+" is a prime number"
label=tk.Label(root,text=result)
label.pack()
root.mainloop()