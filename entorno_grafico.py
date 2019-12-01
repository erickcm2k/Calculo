import subprocess, sys
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
    Qle_Funcion.setText('')
    Lbl_Resultado.setText('Resultado')

def AbrirAyuda():

    if sys.platform == 'linux':
        #Linux detectado
        subprocess.call(["xdg-open", "ayuda.pdf"])
    elif sys.platform == 'darwin':
        #MacOSx detectado
        subprocess.call(["open", "ayuda.pdf"])
    elif sys.platform.startswith('win'):
        #Windows detectado
        subprocess.call(["start", "ayuda.pdf"])

def Mostrar():
    AbrirAyuda()
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
    Lbl_ayuda=graficos.QLabel('\n\t\t¿Cómo ingresar datos a la calculadora?\n'+
                                '\n\t\tLas funciones aceptadas son:\n'+
                                '\nForma Convencional:\tForma que puede entender la calculadora:'+
                                '\ncoseno\tcos(x)\nseno\tsin(x)\ntangente\ttan(x)\nsecante\tsec(x)\ncosecante\tcsc(x)\ncotangente\tcot(x)'+
                                '\narcocoseno\tacos(x)\narcoseno\tasin(x)\narcotangente\tatan(x)\narcosecante\tasec(x)\narcocosecante\tacsc(x)\narcocotangente\tacot(x)'+
                                '\ncosh(x)\tcosh(x)\nsenh(x)\tsinh(x)\ntanh(x)\ttanh(x)\nsech(x)\tsech(x)\ncsch(x)\tcsch(x)\nctgh(x)\tcoth(x)\n'+
                                'e^x\texp(x)\nlog(x)\tlog(x) ó ln(x)\n x^n\tx**n\nnx\tn*x\n √x\tsqrt(x)\n'+
                                'En caso de que obtenga como resultado Integrate(F(x))), indica que su derivada o integral no puede ser computada por este software')
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
