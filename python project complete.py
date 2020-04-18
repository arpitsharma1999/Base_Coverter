from tkinter import *
class convertor:
    def __init__(self):
        window= Tk()
        window.title("KR Convertor")
        self.frame1= Frame(window)
        self.label1= Label(self.frame1, text= "******* Welcome To KR convertor ******* \n", font= "Times 15 italic underline")
        self.label1.pack()
        self.btbns=Button(self.frame1, text= "Binary Number System" , font= "Times 15 italic", command= self.Binaryconvertor)
        self.btdns=Button(self.frame1, text= "Decimal Number System" , font= "Times 15 italic", command= self.Decimalconvertor)
        self.btons=Button(self.frame1, text= "Octal Number System" , font= "Times 15 italic", command= self.octalconvertor)
        self.bthns=Button(self.frame1, text= "Hexa - decimal Number System" , font= "Times 15 italic", command= self.hexaconvertor)
        self.btbns.pack(side=LEFT)
        self.btdns.pack(side=LEFT)
        self.btons.pack(side=LEFT)
        self.bthns.pack(side=LEFT)
        
        self.frame1.pack()
        
        self.frame2= Frame(window)
        self.label2=Label(self.frame2,text= "\n")
        self.label2.pack()
        self.text = Text(self.frame2)
        self.text.insert(END, "If\ni\ndie\ntrying\natleast\ni\ntried\n")
        self.text.pack()
        self.frame2.pack()
        window.mainloop()
    def Binaryconvertor(self):
        window1=Tk()
        window1.title("Binary Convertor")
        framebin1=Frame(window1)
        labelbin1=Label(framebin1,text="******* Wecome To Binary Convertor *******", font="Times 20 italic bold underline")
        labelbin1.pack()
        framebin1.pack()
        
        labelbin2=Label(window1,text="Enter the Binary number : ", font="Times 15 italic")
        labelbin2.place(x='100',y='100')
        self.bintext= IntVar()
        self.entrybin1=Entry(window1,textvariable = self.bintext)
        
        
        self.entrybin1.place(x='330',y='105')
        
        convertbuttonbin=Button(window1,text="  > Convert <",bg="white",command=self.convertbintoall)
        convertbuttonbin.place(x='600', y='200')
        
        labelbin3=Label(window1,text="Value in Decimal : ", font="Times 15 italic")
        labelbin3.place(x='800',y='105')
        
        labelbin4=Label(window1,text="Value in Octal : ", font="Times 15 italic")
        labelbin4.place(x='800',y='205')
        
        labelbin5=Label(window1,text="Value in Hexa-Decimal : ", font="Times 15 italic")
        labelbin5.place(x='800',y='305')
        
        self.labelbin6=Label(window1, text="UNKNOWN DECIMAL ", font="Times 15 bold underline")
        self.labelbin6.place(x='1100',y='105')
       
        buttonbin2=Button(window1,text=" Explanation",font="Times 10 bold",command = self.explanationbintodecimal)
        buttonbin2.place(x='1130',y='155')
        
        self.labelbin7=Label(window1, text="UNKNOWN OCTAL ", font="Times 15 bold underline")
        self.labelbin7.place(x='1100',y='205')
        
        buttonbin3=Button(window1,text=" Explanation",font="Times 10 bold",command=self.explanationbintooctal)
        buttonbin3.place(x='1130',y='255')
        
        self.labelbin8=Label(window1, text="UNKNOWN HEXA-DECIMAL ", font="Times 15 bold underline")
        self.labelbin8.place(x='1100',y='305')
        
        buttonbin4=Button(window1,text=" Explanation",font="Times 10 bold",command=self.explanationbintohexa)
        buttonbin4.place(x='1130',y='355')
        
        window1.mainloop()
        
    def Decimalconvertor(self):
        window2=Tk()
        window2.title("Decimal Convertor")
        framedec1=Frame(window2)
        labeldec1=Label(framedec1,text="******* Wecome To Decimal Convertor *******", font="Times 20 italic bold underline")
        labeldec1.pack()
        framedec1.pack()
        
        labeldec2=Label(window2,text="Enter the Decimal number : ", font="Times 15 italic")
        labeldec2.place(x='100',y='100')
        self.dectext=IntVar()
        self.entrydec1=Entry(window2,textvariable=self.dectext)
        
        
        self.entrydec1.place(x='330',y='105')
        
        convertbuttondec=Button(window2,text="  > Convert <",bg="white",command=self.convertdectoall)
        convertbuttondec.place(x='600', y='200')
        
        labeldec3=Label(window2,text="Value in Binary : ", font="Times 15 italic")
        labeldec3.place(x='800',y='105')
        
        labeldec4=Label(window2,text="Value in Octal : ", font="Times 15 italic")
        labeldec4.place(x='800',y='205')
        
        labeldec5=Label(window2,text="Value in Hexa-Decimal : ", font="Times 15 italic")
        labeldec5.place(x='800',y='305')
        
        self.labeldec6=Label(window2, text="UNKNOWN BINARY ", font="Times 15 bold underline")
        self.labeldec6.place(x='1100',y='105')
        
        buttondec2=Button(window2,text=" Explanation",font="Times 10 bold",command=self.explanationdectobin)
        buttondec2.place(x='1130',y='155')
        
        self.labeldec7=Label(window2, text="UNKNOWN OCTAL ", font="Times 15 bold underline")
        self.labeldec7.place(x='1100',y='205')
        
        buttondec3=Button(window2,text=" Explanation",font="Times 10 bold",command=self.explanationdectooct)
        buttondec3.place(x='1130',y='255')
        
        self.labeldec8=Label(window2, text="UNKNOWN HEXA-DECIMAL ", font="Times 15 bold underline")
        self.labeldec8.place(x='1100',y='305')
        
        buttondec4=Button(window2,text=" Explanation",font="Times 10 bold",command=self.explanationdectohex)
        buttondec4.place(x='1130',y='355')
        
        window2.mainloop()
        
    def octalconvertor(self):
        window3=Tk()
        window3.title("Octal Convertor")
        
        frameoct1=Frame(window3)
        labeloct1=Label(frameoct1,text="******* Wecome To Octal Convertor *******", font="Times 20 italic bold underline")
        labeloct1.pack()
        frameoct1.pack()
        
        labeloct2=Label(window3,text="Enter the Octal number : ", font="Times 15 italic")
        labeloct2.place(x='100',y='100')
        self.octtext=IntVar()
        self.entryoct1=Entry(window3,textvariable=self.octtext)
        
        
        self.entryoct1.place(x='330',y='105')
        
        convertbuttonoct=Button(window3,text="  > Convert <",bg="white",command=self.convertocttoall)
        convertbuttonoct.place(x='600', y='200')
        
        labeloct3=Label(window3,text="Value in Binary : ", font="Times 15 italic")
        labeloct3.place(x='800',y='105')
        
        labeloct4=Label(window3,text="Value in Decimal : ", font="Times 15 italic")
        labeloct4.place(x='800',y='205')
        
        labeloct5=Label(window3,text="Value in Hexa-Decimal : ", font="Times 15 italic")
        labeloct5.place(x='800',y='305')
        
        self.labeloct6=Label(window3, text="UNKNOWN BINARY ", font="Times 15 bold underline")
        self.labeloct6.place(x='1100',y='105')
        
        buttonoct2=Button(window3,text=" Explanation",font="Times 10 bold",command=self.explanationocttobin)
        buttonoct2.place(x='1130',y='155')
        
        self.labeloct7=Label(window3, text="UNKNOWN DECIMAL ", font="Times 15 bold underline")
        self.labeloct7.place(x='1100',y='205')
        
        buttonoct3=Button(window3,text=" Explanation",font="Times 10 bold",command=self.explanationocttodec)
        buttonoct3.place(x='1130',y='255')
        
        self.labeloct8=Label(window3, text="UNKNOWN HEXA-DECIMAL ", font="Times 15 bold underline")
        self.labeloct8.place(x='1100',y='305')
        
        buttonoct4=Button(window3,text=" Explanation",font="Times 10 bold",command=self.explanationocttohex)
        buttonoct4.place(x='1130',y='355')
        
        window3.mainloop()
        
    def hexaconvertor(self):
        window4=Tk()
        window4.title("Hexa-decimal Convertor")
        
        
        framehex1=Frame(window4)
        labelhex1=Label(framehex1,text="******* Wecome To Hexa-Decimal Convertor *******", font="Times 20 italic bold underline")
        labelhex1.pack()
        framehex1.pack()
        
        labelhex2=Label(window4,text="Enter the Hexa-Decimal number : ", font="Times 15 italic")
        labelhex2.place(x='100',y='100')
        self.hextext=StringVar()
        self.entryhex1=Entry(window4,textvariable=self.hextext)
        
        
        self.entryhex1.place(x='390',y='105')
        
        convertbuttonhex=Button(window4,text="  > Convert <",bg="white",command=self.converthextoall)
        convertbuttonhex.place(x='600', y='200')
        
        labelhex3=Label(window4,text="Value in Binary : ", font="Times 15 italic")
        labelhex3.place(x='800',y='105')
        
        labelhex4=Label(window4,text="Value in Decimal : ", font="Times 15 italic")
        labelhex4.place(x='800',y='205')
        
        labelhex5=Label(window4,text="Value in Octal : ", font="Times 15 italic")
        labelhex5.place(x='800',y='305')
        
        self.labelhex6=Label(window4, text="UNKNOWN BINARY ", font="Times 15 bold underline")
        self.labelhex6.place(x='1100',y='105')
        
        buttonhex2=Button(window4,text=" Explanation",font="Times 10 bold",command=self.explanationhextobin)
        buttonhex2.place(x='1130',y='155')
        
        self.labelhex7=Label(window4, text="UNKNOWN DECIMAL ", font="Times 15 bold underline")
        self.labelhex7.place(x='1100',y='205')
        
        buttonhex3=Button(window4,text=" Explanation",font="Times 10 bold",command=self.explanationhextodec)
        buttonhex3.place(x='1130',y='255')
        
        self.labelhex8=Label(window4, text="UNKNOWN OCTAL ", font="Times 15 bold underline")
        self.labelhex8.place(x='1100',y='305')
        
        buttonhex4=Button(window4,text=" Explanation",font="Times 10 bold",command=self.explanationhextooct)
        buttonhex4.place(x='1130',y='355')
        
        
        window4.mainloop()
        
        
    def explanationbintodecimal(self):
        window5=Tk()
        window5.title("Explanation for binary to decimal")
        textbd=Text(window5)
        textbd.insert(END,"""This explanation is for binary to decimal conversion.\n
                            For binary number with n digits:

                            dn-1 ... d3 d2 d1 d0

                            The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):

                            decimal = d0×20 + d1×21 + d2×22 + ...""")
        textbd.pack()
        window5.mainloop()
        
    def explanationbintooctal(self):
        windows6=Tk()
        windows6.title("Explanation for binary to octal")
        textbo=Text(windows6)
        textbo.insert(END,"""This explanation is for binary to octal conversion.\n
        Octal number system provides convenient way of converting large binary \nnumbers into more compact and smaller groups. There are various ways to convert a binary number into octal number. You can convert using direct methods or \nindirect methods. First, you need to convert a binary into other base system \n(e.g., into decimal, or into hexadecimal). Then you need to convert it octal number.

        Most Significant Bit (MSB)			Octal Point			Least Significant Bit (LSB)
        82	81	80		8-1	8-2	8-3
        64	8	1		1/8	1/64	1/512
        Since number numbers are type of positional number system. That means weight of the positions from right to left are as 80, 81, 82, 83 and so onfor the integer part and weight of the positions from left to right are as 8-1, 8-2, 8-3and so on.for the fractional part.""")
        textbo.pack()
        windows6.mainloop()
        
    def explanationbintohexa(self):
        windows7=Tk()
        windows7.title("Explanation for binary to hexa-decimal")
        textbh=Text(windows7)
        textbh.insert(END,"""This explanation is for binary to hexa-decimal conversion.\n
                            To convert the given binary number into its equivalent hexadecimal number rewrite the binary number of the sets of four digits and then place the hexadecimal digit in front of each four digit set of a binary number as explained by the following number.

                            hexadecimal-to-binary-conversion-example-2Thus the equivalent hexadecimal number is E8D6.""")
        textbh.pack()
        windows7.mainloop()
        
    def explanationdectobin(self):
        windows8=Tk()
        windows8.title("Explanation for decimal to binary")
        textdb=Text(windows8)
        textdb.insert(END,"This\nexplanatio \nis\nfor\ndecimal\nto\nbinary\nconversion.")
        textdb.pack()
        windows8.mainloop()
        
    def explanationdectooct(self):
        windows9=Tk()
        windows9.title("Explanation for decimal to octal")
        textdo=Text(windows9)
        textdo.insert(END,"This\nexplanation \nis\nfor\ndecimal\nto\noctal\nconversion.")
        textdo.pack()
        windows9.mainloop()
        
    def explanationdectohex(self):
        windows10=Tk()
        windows10.title("Explanation for decimal to hexa-decimal")
        textdh=Text(windows10)
        textdh.insert(END,"This\nexplanation \nis\nfor\ndecimal\nto\nhexa-decimal\nconversion.")
        textdh.pack()
        windows10.mainloop()
    
    def explanationocttobin(self):
        windows11=Tk()
        windows11.title("Explanation for octal to binary")
        textob=Text(windows11)
        textob.insert(END,"This\nexplanation \nis\nfor\noctal\nto\nbinary\nconversion.")
        textob.pack()
        windows11.mainloop()
        
    def explanationocttodec(self):
        windows12=Tk()
        windows12.title("Explanation for octal to decimal")
        textod=Text(windows12)
        textod.insert(END,"This\nexplanation \nis\nfor\noctal\nto\ndecimal\nconversion.")
        textod.pack()
        windows12.mainloop()
        
    def explanationocttohex(self):
        windows13=Tk()
        windows13.title("Explanation for octal to hexa-decimal")
        textoh=Text(windows13)
        textoh.insert(END,"This\nexplanation \nis\nfor\noctal\nto\nhexa-decimal\nconversion.")
        textoh.pack()
        windows13.mainloop()
        
    def explanationhextobin(self):
        windows14=Tk()
        windows14.title("Explanation for hexa-decimal to binary")
        texthb=Text(windows14)
        texthb.insert(END,"This\nexplanation \nis\nfor\nhexa-decimal \n\to\nbinary\nconversion.")
        texthb.pack()
        windows14.mainloop()
        
    def explanationhextodec(self):
        windows15=Tk()
        windows15.title("Explanation for hexa-decimal to decimal")
        texthd=Text(windows15)
        texthd.insert(END,"This\nexplanation \nis\nfor\nhexa-decimal \n\to\ndecimal\nconversion.")
        texthd.pack()
        windows15.mainloop()
        
    def explanationhextooct(self):
        windows16=Tk()
        windows16.title("Explanation for hexa-decimal to octal")
        textho=Text(windows16)
        textho.insert(END,"This\nexplanation \nis\nfor\nhexa-decimal \n\to\noctal\nconversion.")
        textho.pack()
        windows16.mainloop()
    
    def convertbintoall(self):
        y=(self.entrybin1.get())
        x=int(y,base=2)
        print(x)
        self.labelbin6["text"]=x
        self.labelbin7["text"]=oct(x)
        self.labelbin8["text"]=hex(x)
        
        
    def convertdectoall(self):
        y=self.entrydec1.get()
        x=int(y)
        self.labeldec6["text"]=bin(x)
        self.labeldec7["text"]=oct(x)
        self.labeldec8["text"]=hex(x)
    def convertocttoall(self):
        y=self.entryoct1.get()
        x=int(y,base=8)
        print(x)
        self.labeloct6["text"]=bin(x)
        self.labeloct7["text"]=x
        self.labeloct8["text"]=hex(x)
        
    def converthextoall(self):
        y=self.entryhex1.get()
        x=int(y,base=16)
        print(x)
        self.labelhex6["text"]=bin(x)
        self.labelhex7["text"]=x
        self.labelhex8["text"]=oct(x)
        
convertor()
