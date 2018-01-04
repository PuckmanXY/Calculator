from tkinter import *

class CalButton(Button):
  def __init__(self, container, comandClick, height, width, text):
    super().__init__(container,command=comandClick)
    self.configure(height=height,width=width,text=text, background="#FF9933")
    self.pack(side=LEFT)
     
class Display(Label):
  def __init__(self,container,height,width,text):
    super().__init__(container)
    self.configure(background="#FFFFFF",height=height,width=width,text=text)
    self.pack(side=LEFT)
  
class Calculator:
    def __init__(self, parent):
  
        #Valores
        self.n1 = ''
        self.operation = ''
        self.n2 = ''
        self.pointClicked = False
  
  
        #Janela
        self.myParent = parent
        self.myParent.title('Calculadora')
        self.myParent.geometry('303x480')
        self.myParent.resizable(1,1)

        self.myContainer = []

        for i in range(6):
            self.myContainer.append(Frame(parent))
            self.myContainer[i].pack()
  
  
  
        #Visores
        self.visorValue1 = Display(self.myContainer[0], 5, 6, self.n1)
  
        self.visorOperation = Display(self.myContainer[0], 5, 5, self.operation)
  
        self.visorValue2 = Display(self.myContainer[0], 5, 6, self.n2)
  
        self.visorEquals = Display(self.myContainer[0], 5, 5, '')
  
        self.visorResult = Display(self.myContainer[0], 5, 15, '')
  
  
  
        #Botões de valor
        self.button1 = CalButton(self.myContainer[1],lambda:self.buttonClick('1'),5,6,"1")

        self.button2 = CalButton(self.myContainer[1],lambda:self.buttonClick('2'),5,6,"2")

        self.button3 = CalButton(self.myContainer[1],lambda:self.buttonClick('3'),5,6,"3")

        self.button4 = CalButton(self.myContainer[2],lambda:self.buttonClick('4'),5,6,"4")

        self.button5 = CalButton(self.myContainer[2],lambda:self.buttonClick('5'),5,6,"5")

        self.button6 = CalButton(self.myContainer[2],lambda:self.buttonClick('6'),5,6,"6")

        self.button7 = CalButton(self.myContainer[3],lambda:self.buttonClick('7'),5,6,"7")

        self.button8 = CalButton(self.myContainer[3],lambda:self.buttonClick('8'),5,6,"8")

        self.button9 = CalButton(self.myContainer[3],lambda:self.buttonClick('9'),5,6,"9")

        self.button0 = CalButton(self.myContainer[4],lambda:self.buttonClick('0'),5,6,"0")

        self.pointButton = CalButton(self.myContainer[4], self.buttonPointClick, 5, 6, ".")
         
         
  
        ##Botões de operacão
        self.buttonReset = CalButton(self.myContainer[5],self.ResetClick,3,35,"RESET")
  
        self.buttonAddition = CalButton(self.myContainer[1],lambda:self.OperationClick('+'),5,6,"+")
  
        self.buttonSubtraction = CalButton(self.myContainer[2],lambda:self.OperationClick('-'),5,6,"-")
  
        self.buttonMultiplication = CalButton(self.myContainer[3],lambda:self.OperationClick('*'),5,6,"*")
  
        self.buttonEquals = CalButton(self.myContainer[4],self.Equals,5,6,"=")
  
        self.buttonDivision = CalButton(self.myContainer[4],lambda:self.OperationClick('/'),5,6,"/")
  
  
  
 
    ##Funções
    def buttonClick(self,number):
        if self.operation == '':
            self.n1 = self.n1 + number
            self.visorValue1.configure(text=self.n1)
        else:
            self.n2 = self.n2 + number
            self.visorValue2.configure(text=self.n2)
 
  
    def buttonPointClick(self):
        if self.operation == '' and self.pointClicked == False:
            self.n1 = self.n1 + '.'
            self.pointClicked = True
            self.visorValue1.configure(text=self.n1)
        elif self.pointClicked == True: pass
        else:
            self.n2 = self.n2 + '.'
            self.visorValue2.configure(text=self.n2)
  
    def OperationClick(self,operation):
        self.pointClicked = False
        self.operation= operation
        self.visorOperation.configure(text=self.operation)
  
    def Equals(self):
        if self.operation=='':
            pass
        if self.operation=='+':
            self.visorResult.configure(text="%.2f"%(float(self.n1) + float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='-':
            self.visorResult.configure(text="%.2f"%(float(self.n1) - float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='*':
            self.visorResult.configure(text="%.2f"%(float(self.n1) * float(self.n2)))
            self.visorEquals.configure(text="=")
        if self.operation=='/':
            if float(self.n2)==0:
                self.visorValue1.configure(text='Math')
                self.visorValue2.configure(text='Error')
                self.visorResult.configure(text='Try Again')
                self.n1=''
                self.operation=''
                self.n2=''
            else:
                self.visorResult.configure(text="%.2f"%(float(self.n1) / float(self.n2)))
                self.visorEquals.configure(text="=")
  
    def ResetClick(self):
        self.n1=''
        self.n2=''
        self.operation=''
        self.pointClicked = False
        self.visorValue1.configure(text=self.n1)
        self.visorValue2.configure(text=self.n2)
        self.visorOperation.configure(text=self.operation)
        self.visorResult.configure(text='')
  
  
root = Tk()
myapp = Calculator(root)
root.mainloop()
