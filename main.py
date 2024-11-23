#小向计算器源代码，使用Python3.9 64位编写
import tkinter as tk #导入tkinter GUI 库

#定义父窗口root
root = tk.Tk()
root.title("小向计算器")

#其他变量定义
b = 0
num = tk.StringVar()
num2 = tk.StringVar()
num.set("0")
num2.set("="+"0")
ans = 0
c = 0

#函数定义
def c():#按键“=”的功能
    try:
        re = eval(num.get())
        global ans
        ans = re
        num2.set("="+str(re))
        global c
        c = 1
    
        if len(num2.get()) > 25:
            num.set("得数最多显示24位，请按AC")
            num2.set("=0")
            
    except:
        num.set("出错了，请按AC")
        num2.set("=0")

def cc(a):#判断输入的是符号还是数字
    try:
        b = int(a)
        num.set(a)
    except:
        num.set("ans"+a)
            
    

def clear():#按键“AC”的功能
    num.set("0")
    num2.set("=0")

def backspace():#按键“DEL”的功能
    num.set(str(num.get())[:-1])
    if num.get() == "":
        num.set("0")
        num2.set("=0")

def show(a):#更新算式显示区
    b = 1
    number = num.get()
    if len(number) < 24:
        if number == "0":
            if a == "+" or a == "-" or a == "*" or a == "/":
                num.set("0"+a)
            else:
                number = ""
        num.set(number+a)
        global c
        if ("ans" not in num.get()) and (num.get() != "0")and (c == 1):
            c = 0
            cc(a)
    else:
        num.set("最多显示25位，请按AC")
    
def ifu():#菜单“使用说明”功能
    root1 = tk.Tk()
    root1.title("使用说明")
    lab11 = tk.Label(root1,text = "使用说明",font = "Helvetic 20 bold")
    lab11.pack(padx = 10,pady = 10)
    lab12 = tk.Label(root1,text = """软件名称：小向计算器
版本号：V2.0
使用方法：不要告诉我你连计算器都不会用......
注意事项：请不要犯一些常识性错误
          请不要输入得数太大的算式，否则程序会直接卡掉
开发者: 稗田阿柔
联系方式：hiedanoajuu@outlook.com""",justify =  'left')
    lab12.pack(padx = 10,pady = 10)
    root1.mainloop()

def ad():#菜单“版权信息”功能
    root2 = tk.Tk()
    root2.title("版权信息")
    lab21 = tk.Label(root2,text = "版权信息",font = "Helvetic 20 bold")
    lab21.pack(padx = 10,pady = 10)
    lab22 = tk.Label(root2,text = """小向计算器
版本:2.0
©2021 稗田阿柔 保留所有权利。""",justify =  'left')
    lab22.pack(padx = 10,pady = 10)
    root2.mainloop()

def utl():#菜单“更新日志”功能
    root3 = tk.Tk()
    root3.title("更新日志")
    lab31 = tk.Label(root3,text = "更新日志",font = "Helvetic 20 bold")
    lab31.pack(padx = 10,pady = 10)
    lab32 = tk.Label(root3,text = """2021.3.12 V1.0
更新主要功能，以及“说明”下拉菜单
2021.3.12 V1.1
修复BUG,新增地板除法和次幂
2021.3.12 V2.0
修复BUG，添加换行结果显示""",justify =  'left')
    lab32.pack(padx = 10,pady = 10)
    root3.mainloop()

#主程序
#“说明”菜单
menu = tk.Menu(root)
a_menu = tk.Menu(menu)
menu.add_cascade(label = "说明",menu = a_menu)
a_menu.add_command(label = "使用说明",command = ifu)
a_menu.add_command(label = "版权信息",command = ad)
a_menu.add_command(label = "更新日志",command = utl)
root.config(menu = menu)

#按键定义
label = tk.Label(root,width = 25,height = 2,textvariable = num,bg = "lightyellow",justify =  'right')
label.grid(row = 0,column = 0,columnspan = 5,padx = 5)
label2 = tk.Label(root,width = 25,height = 2,textvariable = num2,bg = "lightyellow",justify =  'right')
label2.grid(row = 1,column = 0,columnspan = 5,padx = 5)
tk.Button(root,text = "7",width = 5,command = lambda:show("7")).grid(row = 2,column = 0,padx = 2,pady = 2)
tk.Button(root,text = "8",width = 5,command = lambda:show("8")).grid(row = 2,column = 1,padx = 2,pady = 2)
tk.Button(root,text = "9",width = 5,command = lambda:show("9")).grid(row = 2,column = 2,padx = 2,pady = 2)
tk.Button(root,text = "DEL",width = 5,command = backspace,bg = "red").grid(row = 2,column = 3,padx = 2,pady = 2)
tk.Button(root,text = "AC",width = 5,command = clear,bg = "red").grid(row = 2,column = 4,padx = 2,pady = 2)
tk.Button(root,text = "4",width = 5,command = lambda:show("4")).grid(row = 3,column = 0,padx = 2,pady = 2)
tk.Button(root,text = "5",width = 5,command = lambda:show("5")).grid(row = 3,column = 1,padx = 2,pady = 2)
tk.Button(root,text = "6",width = 5,command = lambda:show("6")).grid(row = 3,column = 2,padx = 2,pady = 2)
tk.Button(root,text = "*",width = 5,command = lambda:show("*")).grid(row = 3,column = 3,padx = 2,pady = 2)
tk.Button(root,text = "/",width = 5,command = lambda:show("/")).grid(row = 3,column = 4,padx = 2,pady = 2)
tk.Button(root,text = "1",width = 5,command = lambda:show("1")).grid(row = 4,column = 0,padx = 2,pady = 2)
tk.Button(root,text = "2",width = 5,command = lambda:show("2")).grid(row = 4,column = 1,padx = 2,pady = 2)
tk.Button(root,text = "3",width = 5,command = lambda:show("3")).grid(row = 4,column = 2,padx = 2,pady = 2)
tk.Button(root,text = "+",width = 5,command = lambda:show("+")).grid(row = 4,column = 3,padx = 2,pady = 2)
tk.Button(root,text = "-",width = 5,command = lambda:show("-")).grid(row = 4,column = 4,padx = 2,pady = 2)
tk.Button(root,text = "0",width = 5,command = lambda:show("0")).grid(row = 5,column = 0,padx = 2,pady = 2)
tk.Button(root,text = ".",width = 5,command = lambda:show(".")).grid(row = 5,column = 1,padx = 2,pady = 2)
tk.Button(root,text = "//",width = 5,command = lambda:show("//")).grid(row = 5,column = 2,padx = 2,pady = 2)
tk.Button(root,text = "**",width = 5,command = lambda:show("**")).grid(row = 5,column = 3,padx = 2,pady = 2)
tk.Button(root,text = "=",width=5,command = c,bg = "yellow").grid(row = 5,column = 4,padx = 2,pady = 2)

root.mainloop()

    
