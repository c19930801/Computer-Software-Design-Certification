import tkinter as tk
root=tk.Tk()
root.title("SD Q4")
root.geometry("300x400")
root.title("體質指數BMI")

with open("data.txt","r")as f:
    data=f.read()
n=data.split("\n")
# ['176,45', '165,50', '170,55', '']
# BMI=體重/身高*身高
BMI=[]
for i in range(3):
    w=n[i].split(",")
    h=int(w[0])/100
    m=int(w[1])
    bmi=((m/(h*h)+0.5)*100)//100
    BMI.append(int(bmi))
result=''
if 20<=min(BMI)<=25:
    result="最小 BMI值="+str(min(BMI))+",正常"
else:
    result="最小 BMI值="+str(min(BMI))+",不正常"
result="第四題結果:\n"+result
label=tk.Label(root,text=result)
label.pack()
root.mainloop()
    
