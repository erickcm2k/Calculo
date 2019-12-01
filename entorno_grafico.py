import PyQt5.QtWidgets as graficos
import sympy as sp
global Layout1
global Layout2
global Btn_derivar
global Btn_integrar
global Btn_Limpiar
global Btn_ayuda
global Btn_ocultar
global Qle_Funcion
global Lbl_ayuda
global Lbl_Resultado
global Ventana2

def Derivar():
    try:
        Cadena=str(Qle_Funcion.text())
        x=sp.Symbol('x')
        Res=sp.diff(Cadena,x)
        Lbl_Resultado.setText(str(Res))
    except:
        Lbl_Resultado.setText('Funcion invalida')

def Integrar():
    try:
        Cadena=str(Qle_Funcion.text())
        x=sp.Symbol('x')
        Res=sp.integrate(Cadena,x)
        Lbl_Resultado.setText(str(Res)+' +c')
    except:
        Lbl_Resultado.setText('Funcion invalida')
def Limpiar():
    Qle_Funcion.setText('Aqui va la funcion a derivar o integrar')
    Lbl_Resultado.setText('Resultado')

def Mostrar():
    Ventana2.setVisible(True)

def Ocultar():
    Ventana2.setVisible(False)

def Completar_Layouts():
    global Layout1
    global Layout2
    Layout1.addWidget(graficos.QLabel('Calculadora de derivadas e integrales'),0,1)
    Layout1.addWidget(Qle_Funcion,1,1)
    Layout1.addWidget(Btn_derivar,2,0)
    Layout1.addWidget(Btn_integrar,2,1)
    Layout1.addWidget(Btn_Limpiar,2,2)
    Layout1.addWidget(Lbl_Resultado,3,1)
    Layout1.addWidget(Btn_ayuda,0,2)
    Layout2.addWidget(Lbl_ayuda,0,0)
    Layout2.addWidget(Btn_ocultar,1,0)
    Btn_ayuda.clicked.connect(Mostrar)
    Btn_ocultar.clicked.connect(Ocultar)
    Btn_derivar.clicked.connect(Derivar)
    Btn_integrar.clicked.connect(Integrar)
    Btn_Limpiar.clicked.connect(Limpiar)



"""En esta parte aunque parezca confus estoy dadole un valor definitivo a los elementos de el entorno grafico"""
def main():
    App=graficos.QApplication([])
    Ventana1=graficos.QWidget()
    global Ventana2
    Ventana2=graficos.QWidget()
    global Layout1
    Layout1=graficos.QGridLayout()
    global Layout2
    Layout2=graficos.QGridLayout()
    global Btn_derivar
    Btn_derivar=graficos.QPushButton('Derivar funcion')
    global Btn_integrar
    Btn_integrar=graficos.QPushButton('Integrar funcion')
    global Btn_Limpiar
    Btn_Limpiar=graficos.QPushButton('Limpiar')
    global Btn_ayuda
    Btn_ayuda=graficos.QPushButton('?')
    global Btn_ocultar
    Btn_ocultar=graficos.QPushButton('Cerrar')
    global Qle_Funcion
    Qle_Funcion=graficos.QLineEdit('Aqui va la funcion')
    global Lbl_ayuda
    Lbl_ayuda=graficos.QLabel('La derivada esta dada con repecto a x'+
                                '\nLas funciones aceptadas son:'+
                                '\nfuncion\tescritura'+
                                '\ncos(x)\tcos(x)\nsen(x)\tsin(x)\ntan(x)\ttan(x)\nsec(x)\tsec(x)\ncsc(x)\tcsc(x)\nctg(x)\tcot(x)'+
                                '\ncosh(x)\tcosh(x)\nsenh(x)\tsinh(x)\ntanh(x)\ttanh(x)\nsech(x)\tsech(x)\ncsch(x)\tcsch(x)\nctgh(x)\tcoth(x)\n'+
                                'arcosen(x)\tasin(x)\narcosen(x)\tacos(x)\narcotan(x)\tatan(x)\narcosec(x)\tasec(x)\narcocsc(x)\tacsc(x)\narcoctg(x)\tacot(x)\n'+
                                'arcosenh(x)\tasinh(x)\narcosenh(x)\tacosh(x)\narcotanh(x)\tatanh(x)\narcosech(x)\tasech(x)\narcocsch(x)\tacsch(x)\narcoctgh(x)\tacoth(x)\n'+
                                'e^x\texp(x)\nlog(x)\tlog(x) ó ln(x)\n x^n\tx**n\nnx\tn*x\n √x\tsqrt(x)\n'+
                                'Un ejemplo de esto es:\texp(cos(x)**4)\n'+
                                'En caso de que obtenga como resultado Integrate(F(x))), indica que su derivada o \nintegral no puede ser computada por este software')
    global Lbl_Resultado
    Lbl_Resultado=graficos.QLabel('Funcion resultante')
    Completar_Layouts()
    Ventana2.setLayout(Layout2)
    Ventana1.setLayout(Layout1)
    Ventana1.resize(400,400)
    Ventana1.setWindowTitle('Calculadora de derivadas e integrales')
    Ventana2.setWindowTitle('Ayuda')
    Ventana1.show()
    App.exec()

if __name__ == "__main__":
    main()
