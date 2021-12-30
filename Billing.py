from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Biling System")
        self.root.geometry("1350x750+0+0")
        bg_color="black"
        title=Label(self.root,text="Deepak Tubewell Traders",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=======variable====================
        self.pipe1=IntVar()
        self.pipe2=IntVar()
        self.pipe3=IntVar()
        self.pipe4=IntVar()
        self.pipe5=IntVar()
        self.pipe6=IntVar()
        self.pipe7=IntVar()
        self.pipe8=IntVar()
        self.pipe9=IntVar()
        self.pipe10=IntVar()
        self.pipe11=IntVar()
        self.pipe12=IntVar()
        self.pipe13=IntVar()
        self.pipe14=IntVar()
        self.pipe15=IntVar()
        self.pipe16=IntVar()
        self.pipe17=IntVar()
        self.pipe18=IntVar()
        self.pipe19=IntVar()
        self.pipe20=IntVar()
        self.pipe21=IntVar()
        self.pipe22=IntVar()
        self.pipe23=IntVar()
        #==Tax and Price=====
        self.pipe_price=StringVar()
        self.pipe_tax=StringVar()
        #==Customer=======
        self.c_name=StringVar()
        self.c_phon=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        








        #====================Customer Detail frame

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        c_name=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        c_phone=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill=Label(F1,text="Bill No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12  bold").grid(row=0,column=6,pady=10,padx=10)

        #=========Pipes Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Pipes",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=950,height=435)

        Pipe_1=Label(F2,text=" 8* Nirmaan B.C.P(200mm)",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,pady=10,sticky="w")
        Pipe1_txt=Entry(F2,width=5,textvariable=self.pipe1,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=15,pady=10)

        Pipe_2=Label(F2,text=" 8* Nirman C.C.P(200mm)",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,pady=10,sticky="w")
        Pipe2_txt=Entry(F2,width=5,textvariable=self.pipe2,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=15,pady=10)

        Pipe_3=Label(F2,text=" 6* Nirman Supremo Agricu Y.C.P",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,pady=10,sticky="w")
        Pipe3_txt=Entry(F2,width=5,textvariable=self.pipe3,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=15,pady=10)

        Pipe_4=Label(F2,text=" 6* Nirmaan C.C.P Bhumi",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,pady=10,sticky="w")
        Pipe4_txt=Entry(F2,width=5,textvariable=self.pipe4,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=15,pady=10)

        Pipe_5=Label(F2,text=" 6* Nirman Supremo Bhumi Y.C.P",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,pady=10,sticky="w")
        Pipe5_txt=Entry(F2,width=5,textvariable=self.pipe5,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=15,pady=10)

        Pipe_6=Label(F2,text=" 5* Nirmaan C.C.P Agriculture",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,pady=10,sticky="w")
        Pipe6_txt=Entry(F2,width=5,textvariable=self.pipe6,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=15,pady=10)

        Pipe_7=Label(F2,text=" 6* Nirmaan C.C.P Agriculture",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=6,column=0,pady=10,sticky="w")
        Pipe7_txt=Entry(F2,width=5,textvariable=self.pipe7,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=15,pady=10)

        Pipe_8=Label(F2,text=" 5* Nirmaan Supremo Agricu Y.C.P",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=7,column=0,pady=10,sticky="w")
        Pipe8_txt=Entry(F2,width=5,textvariable=self.pipe8,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=15,pady=10)

        
        
        Pipe_9=Label(F2,text=" 5* Nirmaan C.C.P Bhumi ",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=2,pady=10,sticky="w")
        Pipe9_txt=Entry(F2,width=5,textvariable=self.pipe9,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=15,pady=10)

        Pipe_10=Label(F2,text=" 5* Nirmaan Supremo Bhumi Y.C.P ",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=2,pady=10,sticky="w")
        Pipe10_txt=Entry(F2,width=5,textvariable=self.pipe10,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=15,pady=10)

        Pipe_11=Label(F2,text=" 4* Nirman C.C.P Agriculture ",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=2,pady=10,sticky="w")
        Pipe11_txt=Entry(F2,width=5,textvariable=self.pipe11,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=15,pady=10)

        Pipe_12=Label(F2,text=" 4* Nirmaan C.C.P Bhumi",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=2,pady=10,sticky="w")
        Pipe12_txt=Entry(F2,width=5,textvariable=self.pipe12,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=15,pady=10)

        Pipe_13=Label(F2,text=" 4* Nirmaan C.C.P Supremo",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=2,pady=10,sticky="w")
        Pipe13_txt=Entry(F2,width=5,textvariable=self.pipe13,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=3,padx=15,pady=10)

        Pipe_14=Label(F2,text=" 3* Nirmaan T.C.P",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=2,pady=10,sticky="w")
        Pipe14_txt=Entry(F2,width=5,textvariable=self.pipe14,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=3,padx=15,pady=10)

        Pipe_15=Label(F2,text=" 3* Nirmaan W.C.P",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=6,column=2,pady=10,sticky="w")
        Pipe15_txt=Entry(F2,width=5,textvariable=self.pipe15,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=3,padx=15,pady=10)

        Pipe_16=Label(F2,text=" 4* Nirmaan Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=7,column=2,pady=10,sticky="w")
        Pipe16_txt=Entry(F2,width=5,textvariable=self.pipe16,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=3,padx=15,pady=10)
        
        Pipe_17=Label(F2,text=" 3* Nirman Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=4,pady=10,sticky="w")
        Pipe17_txt=Entry(F2,width=5,textvariable=self.pipe17,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=5,padx=15,pady=10)

        Pipe_18=Label(F2,text=" 2 1/2* Nirman Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=4,pady=10,sticky="w")
        Pipe18_txt=Entry(F2,width=5,textvariable=self.pipe18,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=5,padx=15,pady=10)

        Pipe_19=Label(F2,text=" 2* Nirman Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=4,pady=10,sticky="w")
        Pipe19_txt=Entry(F2,width=5,textvariable=self.pipe19,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=5,padx=15,pady=10)

        Pipe_20=Label(F2,text=" 1 1/4* Nirmaan Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=4,pady=10,sticky="w")
        Pipe20_txt=Entry(F2,width=5,textvariable=self.pipe20,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=5,padx=15,pady=10)

        Pipe_21=Label(F2,text=" 1* Nirman Column",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=4,pady=10,sticky="w")
        Pipe21_txt=Entry(F2,width=5,textvariable=self.pipe21,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=5,padx=15,pady=10)

        Pipe_22=Label(F2,text=" 1* T.C.P Nirmaan",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=4,pady=10,sticky="w")
        Pipe22_txt=Entry(F2,width=5,textvariable=self.pipe22,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=5,padx=15,pady=10)

        Pipe_23=Label(F2,text=" 1* Sch-80",font=("times new roman",12,"bold"),bg=bg_color,fg="yellow").grid(row=6,column=4,pady=10,sticky="w")
        Pipe23_txt=Entry(F2,width=5,textvariable=self.pipe23,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=5,padx=15,pady=10)

        #====================Bill area
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=950,y=180,width=410,height=435)

        bill_title=Label(F5,text="Biling Status",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill="both",expand=1)
        #button frame=======================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=610,relwidth=1,height=90)

        m1_lbl=Label(F6,text="Total Pipes Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,pady=10,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.pipe_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Pipe tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,pady=10,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.pipe_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=700,width=540,height=60)

        total_btn=Button(btn_F,command=self.total,text="Total",bd=3,bg="cadetblue",fg="white",pady=15,width=15,font="arial 7 bold").grid(row=0,column=0,padx=5,pady=0)

        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bd=3,bg="cadetblue",fg="white",pady=15,width=15,font="arial 7 bold").grid(row=0,column=4,padx=20,pady=0)

        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bd=3,bg="cadetblue",fg="white",pady=15,width=15,font="arial 7 bold").grid(row=0,column=8,padx=20,pady=0)

        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bd=3,bg="cadetblue",fg="white",pady=15,width=15,font="arial 7 bold").grid(row=0,column=12,padx=20,pady=0)
        self.welcome_bill()


    def total(self):
        self.pipe_1_p=self.pipe1.get()*210
        self.pipe_2_p=self.pipe2.get()*240
        self.pipe_3_p=self.pipe3.get()*165
        self.pipe_4_p=self.pipe4.get()*156
        self.pipe_5_p=self.pipe5.get()*145
        self.pipe_6_p=self.pipe6.get()*136
        self.pipe_7_p=self.pipe7.get()*185
        self.pipe_8_p=self.pipe8.get()*122
        self.pipe_9_p=self.pipe9.get()*125
        self.pipe_10_p=self.pipe10.get()*115
        self.pipe_11_p=self.pipe11.get()*96
        self.pipe_12_p=self.pipe12.get()*66
        self.pipe_13_p=self.pipe13.get()*56
        self.pipe_14_p=self.pipe14.get()*37
        self.pipe_15_p=self.pipe15.get()*26
        self.pipe_16_p=self.pipe16.get()*180
        self.pipe_17_p=self.pipe17.get()*105
        self.pipe_18_p=self.pipe18.get()*72.5
        self.pipe_19_p=self.pipe19.get()*52.5
        self.pipe_20_p=self.pipe20.get()*32.5
        self.pipe_21_p=self.pipe21.get()*22.5
        self.pipe_22_p=self.pipe22.get()*12.5
        self.pipe_23_p=self.pipe23.get()*22.5
        
        self.total_pipe_price=float(
                                  self.pipe_1_p+
                                  self.pipe_2_p+
                                  self.pipe_3_p+
                                  self.pipe_4_p+
                                  self.pipe_5_p+
                                  self.pipe_6_p+
                                  self.pipe_7_p+
                                  self.pipe_8_p+
                                  self.pipe_9_p+
                                  self.pipe_10_p+
                                  self.pipe_11_p+
                                  self.pipe_12_p+
                                  self.pipe_13_p+
                                  self.pipe_14_p+
                                  self.pipe_15_p+
                                  self.pipe_16_p+
                                  self.pipe_17_p+
                                  self.pipe_18_p+
                                  self.pipe_19_p+
                                  self.pipe_20_p+
                                  self.pipe_21_p+
                                  self.pipe_22_p+
                                  self.pipe_23_p
                                  )
                                  
                                  
                                  
                                  
        self.pipe_price.set("Rs. "+str(self.total_pipe_price))
        self.p_tax=round((self.total_pipe_price*0.18),2)

        self.pipe_tax.set("Rs. "+str(self.p_tax))

        self.Total_bill=float(
                              self.total_pipe_price +
                              self.p_tax
                              )


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to Deepak Tubewell Traders\n")
        
        self.textarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n==============================================")
        self.textarea.insert(END,f"\n Produts\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n==============================================")
         
        










    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer detail are must")
        elif self.pipe_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
            
            

        else:
            self.welcome_bill()
        #========pipes==========
            if self.pipe1.get()!=0:
                self.textarea.insert(END,f"\n 8* Nirmaan B.C.P(200MM)\t\t{self.pipe1.get()}\t\t{self.pipe_1_p}")
            
            if self.pipe2.get()!=0:
                self.textarea.insert(END,f"\n 8* Nirmaan C.C.P Agri\t\t{self.pipe2.get()}\t\t{self.pipe_2_p}")
            if self.pipe3.get()!=0:
                self.textarea.insert(END,f"\n 6* Nirmaan Supremo Agri\t\t{self.pipe3.get()}\t\t{self.pipe_3_p}")
       
            if self.pipe4.get()!=0:
                self.textarea.insert(END,f"\n 6* Nirmaan C.C.P Bhumi\t\t{self.pipe4.get()}\t\t{self.pipe_4_p}")
      
            if self.pipe5.get()!=0:
                self.textarea.insert(END,f"\n 6* Nirmaan Sup Bhumi Y.C.P\t\t{self.pipe5.get()}\t\t{self.pipe_5_p}")
            
            if self.pipe6.get()!=0:
                self.textarea.insert(END,f"\n 5* Nirmaan C.C.P Agri\t\t{self.pipe6.get()}\t\t{self.pipe_6_p}")
            
            if self.pipe7.get()!=0:
                self.textarea.insert(END,f"\n 6* Nirmaan C.C.P Agri\t\t{self.pipe7.get()}\t\t{self.pipe_7_p}")
            
            if self.pipe8.get()!=0:
                self.textarea.insert(END,f"\n 5* Nirmaan Sup Agri Y.C.P\t\t{self.pipe8.get()}\t\t{self.pipe_8_p}")
            
            if self.pipe9.get()!=0:
                self.textarea.insert(END,f"\n 5* Nirmaan C.C.P Bhumi\t\t{self.pipe9.get()}\t\t{self.pipe_9_p}")
            
            if self.pipe10.get()!=0:
                self.textarea.insert(END,f"\n 5* Nirmaan Sup Bhum Y.C.P\t\t{self.pipe10.get()}\t\t{self.pipe_10_p}")
            if self.pipe11.get()!=0:
                self.textarea.insert(END,f"\n 4* Nirmaan C.C.P Agri\t\t{self.pipe11.get()}\t\t{self.pipe_11_p}")
            if self.pipe12.get()!=0:
                self.textarea.insert(END,f"\n 4* Nirmaan C.C.P Bhumi\t\t{self.pipe12.get()}\t\t{self.pipe_12_p}")
            if self.pipe13.get()!=0:
                self.textarea.insert(END,f"\n 4* Nirmaan C.C.P Super\t\t{self.pipe13.get()}\t\t{self.pipe_13_p}")
            if self.pipe14.get()!=0:
                self.textarea.insert(END,f"\n 3* Nirmaan T.C.P(200MM)\t\t{self.pipe14.get()}\t\t{self.pipe_14_p}")
            if self.pipe15.get()!=0:
                self.textarea.insert(END,f"\n 3* Nirmaan W.C.P\t\t{self.pipe15.get()}\t\t{self.pipe_15_p}")
            if self.pipe16.get()!=0:
                self.textarea.insert(END,f"\n 4* Nirmaan Column\t\t{self.pipe16.get()}\t\t{self.pipe_16_p}")
            if self.pipe17.get()!=0:
                self.textarea.insert(END,f"\n 3* Nirmaan Column\t\t{self.pipe17.get()}\t\t{self.pipe_17_p}")
            if self.pipe18.get()!=0:
                self.textarea.insert(END,f"\n 2 1/2* Nirmaan Column\t\t{self.pipe18.get()}\t\t{self.pipe_18_p}")
            if self.pipe19.get()!=0:
                self.textarea.insert(END,f"\n 2* Nirmaan Column\t\t{self.pipe19.get()}\t\t{self.pipe_19_p}")
            if self.pipe20.get()!=0:
                self.textarea.insert(END,f"\n 1 1/2* Nirmaan Column\t\t{self.pipe20.get()}\t\t{self.pipe_20_p}")
            if self.pipe21.get()!=0:
                self.textarea.insert(END,f"\n 1* Nirmaan Column\t\t{self.pipe21.get()}\t\t{self.pipe_21_p}")
            if self.pipe22.get()!=0:
                self.textarea.insert(END,f"\n 1* T.C.P Nirmaan\t\t{self.pipe22.get()}\t\t{self.pipe_22_p}")
            if self.pipe23.get()!=0:
                self.textarea.insert(END,f"\n 1* Sch-80)\t\t{self.pipe23.get()}\t\t{self.pipe_23_p}")
        
        
            self.textarea.insert(END,f"\n----------------------------------------------")
            if self.pipe_tax.get()!="Rs. 0.0":
                
                self.textarea.insert(END,f"\n Pipe Tax\t\t{self.pipe_tax.get()}")
            self.textarea.insert(END,f"\n Total Bill: \t\t Rs. {self.Total_bill}")
        
             

            self.textarea.insert(END,f"\n----------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved bill",f"Bill no. :{self.bill_no.get()}  Saved Successfuly")
        else:
            return
        
        

    def find_bill(self):
        present="no"
        
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                
                for d in f1:
                    self.textarea.insert(END,d)
                    
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear")
        if op>0:
            
            self.pipe1.set(0)  
            self.pipe2.set(0)
            self.pipe3.set(0)
            self.pipe4.set(0)
            self.pipe5.set(0)
            self.pipe6.set(0)
            self.pipe7.set(0)
            self.pipe8.set(0)
            self.pipe9.set(0)
            self.pipe10.set(0)
            self.pipe11.set(0)
            self.pipe12.set(0)
            self.pipe13.set(0)
            self.pipe14.set(0)
            self.pipe15.set(0)
            self.pipe16.set(0)
            self.pipe17.set(0)
            self.pipe18.set(0)
            self.pipe19.set(0)
            self.pipe20.set(0)
            self.pipe21.set(0)
            self.pipe22.set(0)
            self.pipe23.set(0)
            #==Tax and Price=====
            self.pipe_price.set("")
            self.pipe_tax.set("")
            #==Customer=======
            self.c_name.set("")
            self.c_phon.set("")
        
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
            


        
        
        
        

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
            
            
                    
         
         
                
            
        
    

        



        
 
 


        

    

        








        
root=Tk()
obj=Bill_App(root)
root.mainloop()

