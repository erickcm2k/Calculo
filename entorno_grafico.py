import PyQt5.QtWidgets as graficos
import sympy as sp
global Layout1
global Layout2
global Btn_derivar
global Btn_integrar
global Btn_Graficar
global Btn_ayuda
global Btn_ocultar
global Qle_Funcion
global Lbl_Grafica
global Lbl_ayuda
global Lbl_Resultado
global Ventana2

def Derivar():
    Cadena=str(Qle_Funcion.text())
    x=sp.Symbol('x')
    Res=sp.diff(Cadena,x)
    Lbl_Resultado.setText(str(Res))

def Integrar():
    Cadena=str(Qle_Funcion.text())
    x=sp.Symbol('x')
    Res=sp.integrate(Cadena,x)
    Lbl_Resultado.setText(str(Res)+'c')


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
    Layout1.addWidget(Btn_Graficar,2,2)
    Layout1.addWidget(Lbl_Resultado,3,1)
    Layout1.addWidget(Lbl_Grafica,4,1)
    Layout1.addWidget(Btn_ayuda,0,2)
    Layout2.addWidget(Lbl_ayuda,0,0)
    Layout2.addWidget(Btn_ocultar,1,0)
    Btn_ayuda.clicked.connect(Mostrar)
    Btn_ocultar.clicked.connect(Ocultar)
    Btn_derivar.clicked.connect(Derivar)
    Btn_integrar.clicked.connect(Integrar)



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
    global Btn_Graficar
    Btn_Graficar=graficos.QPushButton('Graficar')
    global Btn_ayuda
    Btn_ayuda=graficos.QPushButton('?')
    global Btn_ocultar
    Btn_ocultar=graficos.QPushButton('Cerrar')
    global Qle_Funcion
    Qle_Funcion=graficos.QLineEdit('Aqui va la funcion')
    global Lbl_Grafica
    Lbl_Grafica=graficos.QLabel('Grafica de la funcion')
    global Lbl_ayuda
    Lbl_ayuda=graficos.QLabel('Aqui van las indicaciones de com colocar datos')
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
