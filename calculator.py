#imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import Ui_MainWindow
import math
pi  = math.pi
e   = math.e
#initialization
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

check = True

#logicdef 
def A():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"A")
    if not check:
        ui.lineEdit.setText("A")
    check = True
def B():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"B")
    if not check:
        ui.lineEdit.setText("B")
    check = True
def C():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"C")
    if not check:
        ui.lineEdit.setText("C")
    check = True
def D():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"D")
    if not check:
        ui.lineEdit.setText("D")
    check = True
def E():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"E")
    if not check:
        ui.lineEdit.setText("E")
    check = True
def F():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"F")
    if not check:
        ui.lineEdit.setText("F")
    check = True
def zero():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"0")
    if not check:
        ui.lineEdit.setText("0")
    check = True
def one():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"1")
    if not check:
        ui.lineEdit.setText("1")
    check = True
def two():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"2")
    if not check:
        ui.lineEdit.setText("2")
    check = True
def three():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"3")
    if not check:
        ui.lineEdit.setText("3")
    check = True
def four():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"4")
    if not check:
        ui.lineEdit.setText("4")
    check = True
def five():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"5")
    if not check:
        ui.lineEdit.setText("5")
    check = True
def six():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"6")
    if not check:
        ui.lineEdit.setText("6")
    check = True
def seven():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"7")
    if not check:
        ui.lineEdit.setText("7")
    check = True
def eight():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"8")
    if not check:
        ui.lineEdit.setText("8")
    check = True
def nine():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"9")
    if not check:
        ui.lineEdit.setText("9")
    check = True
def DEL():
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])       #DELETE
def AC():
    ui.lineEdit.setText("")                             #AC
def PR():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+"(")
    if not check:
        ui.lineEdit.setText("(")
    check = True
def PL():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+")")
    if not check:
        ui.lineEdit.setText(")")
    check = True
def dev():
    global check
    ui.lineEdit.setText(ui.lineEdit.text()+"/")
    check = True
def mul():
    global check
    ui.lineEdit.setText(ui.lineEdit.text()+"*")
    check = True
def plus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text()+"+")
    check = True
def minus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text()+"-")
    check = True
def point():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text()+".")
    if not check:
        ui.lineEdit.setText(".")
    check = True
def equal():
    global check
    ui.lineEdit.setText(str(eval(ui.lineEdit.text())))       #equal
    check = False
def dec1():
    global check
    ui.lineEdit.setText("DEC= "+str(ui.lineEdit.text()) + "     HEX= " + str(format(hex(int(ui.lineEdit.text()))[2:]))
                        + "     BIN= " + str(format(bin(int(ui.lineEdit.text()))[2:])) 
                        + "     OCT= " + str(format(oct(int(ui.lineEdit.text()))[2:])))
    check = False
def hex1():
    global check
    ui.lineEdit.setText("DEC= "+str(int(ui.lineEdit.text(),base=16)) + "     HEX= " + str(ui.lineEdit.text())
                        + "     BIN= " + str(format(bin(int(ui.lineEdit.text(),base=16))[2:])) 
                        + "     OCT= " + str(format(oct(int(ui.lineEdit.text(),base=16))[2:])))
    check = False  
def bin1():
    global check
    ui.lineEdit.setText("DEC= "+str(int(ui.lineEdit.text(),base=2)) + "     HEX= " + str(format(hex(int(ui.lineEdit.text(),base=2)))[2:])
                        + "     BIN= " + str(ui.lineEdit.text()) 
                        + "     OCT= " + str(format(oct(int(ui.lineEdit.text(),base=2))[2:])))
    check = False
def oct1():
    global check
    ui.lineEdit.setText("DEC= "+str(int(ui.lineEdit.text(),base=8)) + "     HEX= " + str(format(hex(int(ui.lineEdit.text(),base=8)))[2:])
                        + "     BIN= " + str(format(bin(int(ui.lineEdit.text(),base=8))[2:]))
                        + "     OCT= " + str(ui.lineEdit.text()))
    check = False
def sin():
    global check
    ui.lineEdit.setText("sin("+ui.lineEdit.text()+") = " + str(math.sin(int(ui.lineEdit.text()))))
    check = False
def cos():
    global check
    ui.lineEdit.setText("cos("+ui.lineEdit.text()+") = " + str(math.cos(int(ui.lineEdit.text()))))
    check = False
def tan():
    global check
    ui.lineEdit.setText("tan("+ui.lineEdit.text()+") = " + str(math.tan(int(ui.lineEdit.text()))))
    check = False
def xp2():
    global check
    ui.lineEdit.setText(str(ui.lineEdit.text())+"^2"+ " = " + str(int(ui.lineEdit.text())**2))
    check = False
def log():
    global check
    ui.lineEdit.setText("log(" + str(ui.lineEdit.text()) + ") = " + str(math.log(int(ui.lineEdit.text()))))
    check = False
def oneoverx():
    global check
    ui.lineEdit.setText("1/" + str(ui.lineEdit.text()) + " = " + str(1/(int(ui.lineEdit.text()))))    
    check = False
def factorial():
    global check
    ui.lineEdit.setText(str(ui.lineEdit.text())+"!"+ " = " + str(math.factorial(int(ui.lineEdit.text()))))
    check = False
def tenpwrx():
    global check
    ui.lineEdit.setText("10^" + str(ui.lineEdit.text()) + " = " + str(10**(int(ui.lineEdit.text()))))
    check = False
def sqrt():
    global check
    ui.lineEdit.setText("sqrt("+ui.lineEdit.text()+") = " + str(math.sqrt(int(ui.lineEdit.text()))))
    check = False
def exp():
    global check
    ui.lineEdit.setText("exp(" + str(ui.lineEdit.text())+") "+ " = " + str(math.exp(int(ui.lineEdit.text()))))
    check = False
def ln():
    global check
    ui.lineEdit.setText("ln(" + str(ui.lineEdit.text())+")" + " = " + str(math.log(int(ui.lineEdit.text()),e)))
    check = False
def mod():
    global check
    ui.lineEdit.setText(ui.lineEdit.text()+"%")
    check = True
    

#Connections
ui.pushButton.clicked.connect(zero)
ui.pushButton_9.clicked.connect(one)
ui.pushButton_10.clicked.connect(two)
ui.pushButton_8.clicked.connect(three)
ui.pushButton_5.clicked.connect(four)
ui.pushButton_6.clicked.connect(five)
ui.pushButton_7.clicked.connect(six)
ui.pushButton_4.clicked.connect(seven)
ui.pushButton_3.clicked.connect(eight)
ui.pushButton_2.clicked.connect(nine)
ui.pushButton_19.clicked.connect(DEL)
ui.pushButton_11.clicked.connect(AC)
ui.pushButton_17.clicked.connect(PR)
ui.pushButton_18.clicked.connect(PL)
ui.pushButton_15.clicked.connect(dev)
ui.pushButton_14.clicked.connect(mul)
ui.pushButton_13.clicked.connect(plus)
ui.pushButton_16.clicked.connect(minus)
ui.pushButton_12.clicked.connect(point)
ui.pushButton_20.clicked.connect(equal)
ui.pushButton_21.clicked.connect(dec1)
ui.pushButton_24.clicked.connect(hex1)
ui.pushButton_23.clicked.connect(bin1)
ui.pushButton_22.clicked.connect(oct1)
ui.pushButton_25.clicked.connect(sin)
ui.pushButton_26.clicked.connect(cos)
ui.pushButton_34.clicked.connect(tan)
ui.pushButton_28.clicked.connect(xp2)
ui.pushButton_27.clicked.connect(log)
ui.pushButton_35.clicked.connect(oneoverx)
ui.pushButton_30.clicked.connect(factorial)
ui.pushButton_29.clicked.connect(tenpwrx)
ui.pushButton_36.clicked.connect(sqrt)
ui.pushButton_32.clicked.connect(exp)
ui.pushButton_31.clicked.connect(ln)
ui.pushButton_37.clicked.connect(mod)
ui.pushButton_38.clicked.connect(A)
ui.pushButton_39.clicked.connect(B)
ui.pushButton_40.clicked.connect(C)
ui.pushButton_41.clicked.connect(D)
ui.pushButton_42.clicked.connect(E)
ui.pushButton_33.clicked.connect(F)








sys.exit(app.exec_())
