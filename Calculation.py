import math
from decimal import *
import tkinter as tk
import matplotlib.pyplot as plt

Kw = Decimal("1e-14")

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("普化小计算")
        self.create_buttons()

    #主界面
    def create_buttons(self):
        label = tk.Label(self.master, text="本程序的默认单位：")
        label.grid(row=0, column=0)
        label = tk.Label(self.master, text="浓度：mol/L；体积：L")
        label.grid(row=0, column=1)
        
        label = tk.Label(self.master, text="Kw = ")
        label.grid(row=1, column=0)
        label = tk.Label(self.master, text=Kw)
        label.grid(row=1, column=1)
        
        def change_Kw():
            global Kw
            Kw = tk.Entry.get(Kw0)
            Kw = Decimal(Kw)
            label = tk.Label(self.master, text=Kw)
            label.grid(row=1, column=1)
        
        button = tk.Button(self.master, text="修改水的自解离常数", command=change_Kw)
        button.grid(row=2, column=0)
        Kw0 = tk.Entry(self.master)
        Kw0.grid(row=2, column=1)
        
        button_names = ["一元酸碱溶液","二元酸碱溶液","一元弱酸弱碱盐溶液","两种弱酸或碱共存的水溶液","缓冲溶液","一元酸碱滴定"]
        for i in range(3):
            for j in range(2):
                button = tk.Button(self.master, text=button_names[i*2+j], command=lambda i=i, j=j: self.open_new_interface(i, j))
                button.grid(row=i+3, column=j)

    #小界面
    def open_new_interface(self, i, j):
        button_names = ["一元酸碱溶液","二元酸碱溶液","一元弱酸弱碱盐溶液","两种弱酸或碱共存的水溶液","缓冲溶液","一元酸碱滴定"]
        #"Monobasic acid base solution", "Binary acid base solution", "Monobasic weak acid weak base salt solution", 
        #"An aqueous solution in which two weak acids or bases coexist", "Buffer solution", "Monobasic acid base titration"
        
        #一元酸碱溶液
        if i == 0 and j == 0:        
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            solution_type = tk.BooleanVar()
            solution_type.set(True)
            button = tk.Radiobutton(new_window, text="酸性", variable=solution_type, value=True)
            button.grid(row=0, column=0)
            button = tk.Radiobutton(new_window, text="碱性", variable=solution_type, value=False)
            button.grid(row=0, column=1)
            
            K_label = tk.Label(new_window, text="K(电离平衡常数) = ")
            K_label.grid(row=1, column=0)
            K = tk.Entry(new_window)
            K.grid(row=1, column=1)
            
            C_label = tk.Label(new_window, text="C(溶液初始浓度) = ")            
            C_label.grid(row=2, column=0)
            C = tk.Entry(new_window) 
            C.grid(row=2, column=1)
            
            def calculate_ion_1():
                K_value = tk.Entry.get(K)
                C_value = tk.Entry.get(C)
                solution_type_bool = tk.BooleanVar.get(solution_type)               
                ion,minuslogpro,relativeerror = Define.mono_acid(Decimal(K_value), Decimal(C_value), Kw)
                
                if solution_type_bool == True:
                    label = tk.Label(new_window, text="H+离子浓度：")
                    label.grid(row=4,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=4, column=1)
                    
                    label = tk.Label(new_window, text="pH：")
                    label.grid(row=5,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=5, column=1)
                else:
                    label = tk.Label(new_window, text="OH-离子浓度：")
                    label.grid(row=4,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=4, column=1)
                    
                    label = tk.Label(new_window, text="pOH：")
                    label.grid(row=5,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=5, column=1)
                    
                label = tk.Label(new_window, text="相对误差：")
                label.grid(row=6,column=0)
                value = tk.Label(new_window, text=relativeerror)
                value.grid(row=6, column=1)
                            
            button = tk.Button(new_window, text="计算", command=calculate_ion_1)
            button.grid(row=3)                    

        #二元酸碱溶液
        elif i == 0 and j == 1:
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            solution_type = tk.BooleanVar()
            solution_type.set(True)
            button = tk.Radiobutton(new_window, text="酸性", variable=solution_type, value=True)
            button.grid(row=0, column=0)
            button = tk.Radiobutton(new_window, text="碱性", variable=solution_type, value=False)
            button.grid(row=0, column=1)
            
            K1_label = tk.Label(new_window, text="K1(一级电离平衡常数) = ")
            K1_label.grid(row=1, column=0)
            K1 = tk.Entry(new_window)
            K1.grid(row=1, column=1)
            
            K2_label = tk.Label(new_window, text="K2(一级电离平衡常数) = ")
            K2_label.grid(row=2, column=0)
            K2 = tk.Entry(new_window)
            K2.grid(row=2, column=1)
            
            C_label = tk.Label(new_window, text="C(溶液初始浓度) = ")            
            C_label.grid(row=3, column=0)
            C = tk.Entry(new_window) 
            C.grid(row=3, column=1)
            
            def calculate_ion_2():
                K1_value = tk.Entry.get(K1)
                K2_value = tk.Entry.get(K2)
                C_value = tk.Entry.get(C)
                solution_type_bool = tk.BooleanVar.get(solution_type)           
                ion,minuslogpro,relativeerror = Define.diprotic_acid(Decimal(K1_value), Decimal(K2_value), Decimal(C_value), Kw)
                
                if solution_type_bool == True:
                    label = tk.Label(new_window, text="H+离子浓度：")
                    label.grid(row=5,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=5, column=1)
                    
                    label = tk.Label(new_window, text="pH：")
                    label.grid(row=6,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=6, column=1)
                else:
                    label = tk.Label(new_window, text="OH-离子浓度：")
                    label.grid(row=5,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=5, column=1)
                    
                    label = tk.Label(new_window, text="pOH：")
                    label.grid(row=6,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=6, column=1)
                    
                label = tk.Label(new_window, text="相对误差：")
                label.grid(row=7,column=0)
                value = tk.Label(new_window, text=relativeerror)
                value.grid(row=7, column=1)
                
            button = tk.Button(new_window, text="计算", command=calculate_ion_2)
            button.grid(row=4, column=0)
            label = tk.Label(new_window, text="Attention:二元酸碱大部分时候可以直接用一元来计算")            
            label.grid(row=4, column=1) 
            

        #一元弱酸弱碱盐溶液
        elif i == 1 and j == 0:
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            Ka_label = tk.Label(new_window, text="Ka(弱酸电离平衡常数) = ")
            Ka_label.grid(row=0, column=0)
            Ka = tk.Entry(new_window)
            Ka.grid(row=0, column=1)
            
            Kb_label = tk.Label(new_window, text="Kb(弱碱电离平衡常数) = ")
            Kb_label.grid(row=1, column=0)
            Kb = tk.Entry(new_window)
            Kb.grid(row=1, column=1)
            
            C_label = tk.Label(new_window, text="C(溶液初始浓度) = ")            
            C_label.grid(row=2, column=0)
            C = tk.Entry(new_window) 
            C.grid(row=2, column=1)
            
            def calculate_ion_3():
                Ka_value = tk.Entry.get(Ka)
                Kb_value = tk.Entry.get(Kb)
                C_value = tk.Entry.get(C)
                ion,minuslogpro,relativeerror = Define.monobasic_salt(Decimal(Ka_value), Decimal(Kb_value), Decimal(C_value), Kw)
                
                label = tk.Label(new_window, text="H+离子浓度：")
                label.grid(row=4,column=0)
                value = tk.Label(new_window, text=ion)
                value.grid(row=4, column=1)
                    
                label = tk.Label(new_window, text="pH：")
                label.grid(row=5,column=0)
                value = tk.Label(new_window, text=minuslogpro)
                value.grid(row=5, column=1)
                    
                label = tk.Label(new_window, text="相对误差：")
                label.grid(row=6,column=0)
                value = tk.Label(new_window, text=relativeerror)
                value.grid(row=6, column=1)
                            
            button = tk.Button(new_window, text="计算", command=calculate_ion_3)
            button.grid(row=3)

        #两种弱酸或碱共存的水溶液
        elif i == 1 and j == 1:
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            solution_type = tk.BooleanVar()
            solution_type.set(True)
            button = tk.Radiobutton(new_window, text="酸性", variable=solution_type, value=True)
            button.grid(row=0, column=0)
            button = tk.Radiobutton(new_window, text="碱性", variable=solution_type, value=False)
            button.grid(row=0, column=1)
            
            K1_label = tk.Label(new_window, text="K1(一级电离平衡常数1) = ")
            K1_label.grid(row=1, column=0)
            K1 = tk.Entry(new_window)
            K1.grid(row=1, column=1)
            
            K2_label = tk.Label(new_window, text="K2(一级电离平衡常数2) = ")
            K2_label.grid(row=2, column=0)
            K2 = tk.Entry(new_window)
            K2.grid(row=2, column=1)
            
            C1_label = tk.Label(new_window, text="C1(溶液初始浓度1) = ")            
            C1_label.grid(row=3, column=0)
            C1 = tk.Entry(new_window) 
            C1.grid(row=3, column=1)
            
            C2_label = tk.Label(new_window, text="C2(溶液初始浓度2) = ")            
            C2_label.grid(row=4, column=0)
            C2 = tk.Entry(new_window) 
            C2.grid(row=4, column=1)
            
            def calculate_ion_4():
                K1_value = tk.Entry.get(K1)
                K2_value = tk.Entry.get(K2)
                C1_value = tk.Entry.get(C1)
                C2_value = tk.Entry.get(C2)
                solution_type_bool = tk.BooleanVar.get(solution_type)               
                ion,minuslogpro,relativeerror = Define.coexist(Decimal(K1_value), Decimal(K2_value), Decimal(C1_value), Decimal(C2_value), Kw)
                
                if solution_type_bool == True:
                    label = tk.Label(new_window, text="H+离子浓度：")
                    label.grid(row=6,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=6, column=1)
                    
                    label = tk.Label(new_window, text="pH：")
                    label.grid(row=7,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=7, column=1)
                else:
                    label = tk.Label(new_window, text="OH-离子浓度：")
                    label.grid(row=6,column=0)
                    value = tk.Label(new_window, text=ion)
                    value.grid(row=6, column=1)
                    
                    label = tk.Label(new_window, text="pOH：")
                    label.grid(row=7,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=7, column=1)
                    
                label = tk.Label(new_window, text="相对误差：")
                label.grid(row=8,column=0)
                value = tk.Label(new_window, text=relativeerror)
                value.grid(row=8, column=1)
                
            button = tk.Button(new_window, text="计算", command=calculate_ion_4)
            button.grid(row=5, column=0) 

        #缓冲溶液
        elif i == 2 and j == 0:
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            cal_type = tk.BooleanVar()
            cal_type.set(True)
            button = tk.Radiobutton(new_window, text="计算pH", variable=cal_type, value=True)
            button.grid(row=0, column=0)
            button = tk.Radiobutton(new_window, text="计算缓冲比", variable=cal_type, value=False)
            button.grid(row=0, column=1)
            
            label = tk.Label(new_window, text="计算pH时请填入K,Ca,Cb")            
            label.grid(row=1, column=0)
            label = tk.Label(new_window, text="计算缓冲比时请填入K,pH")            
            label.grid(row=1, column=1)
            
            K_label = tk.Label(new_window, text="K(电离平衡常数) = ")
            K_label.grid(row=2, column=0)
            K = tk.Entry(new_window)
            K.grid(row=2, column=1)
            
            Ca_label = tk.Label(new_window, text="Ca(共轭酸浓度) = ")            
            Ca_label.grid(row=3, column=0)
            Ca = tk.Entry(new_window) 
            Ca.grid(row=3, column=1)
            
            Cb_label = tk.Label(new_window, text="Cb(共轭碱浓度) = ")            
            Cb_label.grid(row=4, column=0)
            Cb = tk.Entry(new_window) 
            Cb.grid(row=4, column=1)
            
            pH_label = tk.Label(new_window, text="pH = ")            
            pH_label.grid(row=5, column=0)
            pH = tk.Entry(new_window) 
            pH.grid(row=5, column=1)
            
            def calculate_ion_5():
                K_value = tk.Entry.get(K)
                Ca_value = tk.Entry.get(Ca)
                Cb_value = tk.Entry.get(Cb)
                pH_value = tk.Entry.get(pH)
                cal_type_bool = tk.BooleanVar.get(cal_type)

                if cal_type_bool == True:
                    minuslogpro,relativeerror = Define.buffer_solution(Decimal(K_value), cal_type_bool, Kw, Decimal("7"), Decimal(Ca_value), Decimal(Cb_value))
                        
                    label = tk.Label(new_window, text="pH：")
                    label.grid(row=7,column=0)
                    value = tk.Label(new_window, text=minuslogpro)
                    value.grid(row=7, column=1)
                        
                    label = tk.Label(new_window, text="相对误差：")
                    label.grid(row=8,column=0)
                    value = tk.Label(new_window, text=relativeerror)
                    value.grid(row=8, column=1)
                    
                else:
                    buf_ratio = Define.buffer_solution(Decimal(K_value), cal_type_bool, Kw, Decimal(pH_value), Decimal("0"), Decimal("0"))
                        
                    label = tk.Label(new_window, text="缓冲比：")
                    label.grid(row=7,column=0)
                    value = tk.Label(new_window, text=buf_ratio)
                    value.grid(row=7, column=1)
                    
                    zero_label = tk.Label(new_window, text="")
                    zero_label.grid(row=8,column=0)
                    zero_value = tk.Label(new_window, text="")
                    zero_value.grid(row=8, column=1)
                
            button = tk.Button(new_window, text="计算", command=calculate_ion_5)
            button.grid(row=6, column=0)

        #一元酸碱滴定        
        elif i == 2 and j == 1:
            new_window = tk.Toplevel(self.master)
            new_window.title(button_names[i*2+j])
            
            C1_label = tk.Label(new_window, text="C1(弱溶液初始浓度) = ")
            C1_label.grid(row=0, column=0)
            C1 = tk.Entry(new_window)
            C1.grid(row=0, column=1)
            
            V1_label = tk.Label(new_window, text="V1(弱溶液初始体积(mL)) = ")
            V1_label.grid(row=1, column=0)
            V1 = tk.Entry(new_window)
            V1.grid(row=1, column=1)
            
            K1_label = tk.Label(new_window, text="K1(弱溶液电离平衡常数) = ")            
            K1_label.grid(row=2, column=0)
            K1 = tk.Entry(new_window) 
            K1.grid(row=2, column=1)
            
            C2_label = tk.Label(new_window, text="C2(用于滴定的强溶液浓度) = ")            
            C2_label.grid(row=3, column=0)
            C2 = tk.Entry(new_window) 
            C2.grid(row=3, column=1)
            
            V2_label = tk.Label(new_window, text="V2(滴入间隔(mL)) = ")            
            V2_label.grid(row=4, column=0)
            V2 = tk.Entry(new_window) 
            V2.grid(row=4, column=1)
            
            def calculate_ion_6():
                C1_value = tk.Entry.get(C1)
                V1_value = tk.Entry.get(V1)
                K1_value = tk.Entry.get(K1)
                C2_value = tk.Entry.get(C2)
                V2_value = tk.Entry.get(V2)
                Define.titration(Decimal(C1_value), Decimal(V1_value) / Decimal("1000"), Decimal(K1_value), Decimal(C2_value), Kw, Decimal(V2_value) / Decimal("1000"))
                               
            button = tk.Button(new_window, text="计算", command=calculate_ion_6)
            button.grid(row=5, column=0)            
            label = tk.Label(new_window, text="Attention:数据较多的时候可能会卡，请耐心等待")            
            label.grid(row=5, column=1)

class Define:
    #定义一元酸碱计算函数
    def mono_acid(Ka, Ca, Kw, Ion_0=Decimal("1e-7")):
        while True:
            Ion_1 = Kw/Ion_0 + Ka*Ca/(Ka+Ion_0)
            RelativeError = (abs(Ion_1-Ion_0))/Ion_1
            Ion_0 = Ion_1
            if RelativeError <= Decimal("0.01"):
                pH = abs(round(math.log(Ion_1, 10), 2))
                return Ion_1, pH, RelativeError
            
    #定义二元酸碱计算函数
    def diprotic_acid(K1, K2, Ca, Kw, Ion_0=Decimal("1e-7")):
        while True:
            Ion_1 = (K1*Ca*Ion_0 + Decimal("2")*K1*K2*Ca)/(Ion_0**Decimal("2") + K1*Ion_0 + K1*K2) + (Kw/Ion_0)
            RelativeError = (abs(Ion_1-Ion_0))/Ion_1
            Ion_0 = Ion_1
            if RelativeError <= Decimal("0.01"):
                pH = abs(round(math.log(Ion_1, 10), 2))
                return Ion_1, pH, RelativeError

    #定义一元弱酸弱碱盐的计算函数
    def monobasic_salt(Ka, Kb, Cab, Kw, Ion_0=Decimal("1e-7")):
        while True:
            Ion_1 = Decimal(math.sqrt((Kw*Ka*Kb + (Kw*(Ka+Kb) + Ka*Kb*Cab)*Ion_0 - (Ka*Kb - Kw)*(Ion_0**Decimal("2")))/((Ka + Kb + Cab)*Ion_0 + (Ion_0**Decimal("2")))))
            RelativeError = (abs(Ion_1-Ion_0))/Ion_1
            Ion_0 = Ion_1
            if RelativeError <= Decimal("0.01"):
                pH = abs(round(math.log(Ion_1, 10), 2))
                return Ion_1, pH, RelativeError

    #定义两种弱酸或碱共存的水溶液pH计算
    def coexist(Ka1, Ka2, Ca1, Ca2, Kw, Ion_0=Decimal("1e-7")):
        while True:
            Ion_1 = Decimal(math.sqrt((Kw*Ka1*Ka2 + (Kw*(Ka1+Ka2) + Ka1*Ka2*(Ca1+Ca2))*Ion_0 - (Ka1*Ka2 - Kw - Ka1*Ca1 - Ka2*Ca2)*(Ion_0**Decimal("2")))/((Ka1+Ka2)*Ion_0 + (Ion_0**Decimal("2")))))
            RelativeError = (abs(Ion_1-Ion_0))/Ion_1
            Ion_0 = Ion_1
            if RelativeError <= Decimal("0.01"):
                pH = abs(round(math.log(Ion_1, 10), 2))
                return Ion_1, pH, RelativeError

    #定义计算缓冲溶液相关问题
    def buffer_solution(K, task, Kw, ph=Decimal("7"), Ca=Decimal("0"), Cb=Decimal("0"), Ion_0=Decimal("1e-7")):
        if task == True:
            while True:
                Ion_1 = Decimal(math.sqrt((Ion_0*Ca*K + Kw*(K+Ion_0))/(K+Ion_0+Cb)))
                RelativeError = (abs(Ion_1-Ion_0))/Ion_1
                Ion_0 = Ion_1
                if RelativeError <= Decimal("0.01"):
                    pH = abs(round(math.log(Ion_1, 10), 2))
                    return pH, RelativeError

        else:
            buffer_ratio = round(((Decimal(10)**(Decimal("-1")*ph))/K), 3)
            return buffer_ratio

    #定义一元强碱滴定弱酸的函数
    def titration(C0, V0, K0, C1, Kw, step):
        times_int = 0
        V_list = []
        pH_list = []
        while True:
            times = str(times_int)
            N_left = Decimal(C0*V0 - C1*Decimal(times)*step)
            V_total = V0 + step*Decimal(times)
            V_titrated = Decimal(times)*step
            if N_left >= 0:
                Ca = Decimal(N_left/V_total)
                Cb = step * Decimal(times)
                pH = Define.buffer_solution(K0, True, Kw, Decimal("0"), Ca, Cb)[0]
                V_list.append(float(str(V_titrated)))
                pH_list.append(pH)
            else:
                C_add = Decimal(abs(N_left)/V_total)
                C_oh = Decimal(Define.mono_acid(Kw/K0, C0*V0 / V_total, Kw)[0]) + C_add
                pH = 14 - round(abs(math.log(C_oh, 10)), 2)
                V_list.append(float(str(V_titrated)))
                pH_list.append(pH)
            times_int += 1
            # 停止循环语句
            if Decimal(times)*step >= Decimal("2")*V0:
                # 使用matplotlib作图
                plt.rcParams["font.sans-serif"] = ["SimHei"]
                x = V_list
                y = pH_list
                plt.figure()
                plt.plot(x, y, color="#d62728", linewidth=2, marker="o", markerfacecolor="gray", markersize=8)
                plt.title("滴定曲线")
                plt.xlabel("滴定剂用量/l")
                plt.ylabel("体系pH值")
                plt.show()
                break
            
if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()
    
#部分代码借鉴自我的学长，在此对他表示感谢。
