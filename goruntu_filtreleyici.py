import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import cv2
import numpy as np

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  
        self.init_ui()
        

    def init_ui(self):
        
        self.setStyleSheet("background-color : #55ddfc ;font-family : Times New Roman")
        self.setWindowTitle("GÖRÜNTÜ FİLTRELEYİCİ")
        
        
        # ILK RESIM ICIN
        global dosya
        self.yazi_alani1 = QtWidgets.QLabel("İLK RESİM İÇİN DOSYA YOLU GİRİNİZ:")
        self.yazi_alani1.setFixedSize(300,30)
        dosya = QtWidgets.QLineEdit()
        dosya.setFixedSize(300,30)
        
        # IKINCI RESIM ICIN
        global dosya2
        self.yazi_alani2 = QtWidgets.QLabel("İKİNCİ RESİM İÇİN DOSYA YOLU GİRİNİZ:")
        self.yazi_alani2.setFixedSize(300,30)
        dosya2 = QtWidgets.QLineEdit()
        dosya2.setFixedSize(300,30)
        
        #empty_label = QLabel(self)
        
        #BUTON TANIMLAMALARI
        self.buton = QtWidgets.QPushButton("RESİM GOSTER")
        self.buton.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman; text-type : italic')
        self.buton.setFixedSize(300,50)
        
        self.buton1 = QtWidgets.QPushButton("TRESHOLDING UYGULA")
        self.buton1.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton1.setFixedSize(300,50)
        
        self.buton2 = QtWidgets.QPushButton("HİSTOGRAM EŞİTLEME UYGULA")
        self.buton2.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton2.setFixedSize(300,50)
        
        self.buton3 = QtWidgets.QPushButton("MEDIAN BLURLAMA UYGULA")
        self.buton3.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton3.setFixedSize(300,50)
        
        self.buton4 = QtWidgets.QPushButton("MEAN BLURLAMA UYGULA")
        self.buton4.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton4.setFixedSize(300,50)
        
        self.buton5 = QtWidgets.QPushButton("GAUSS UYGULA")
        self.buton5.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton5.setFixedSize(300,50)
        
        self.buton6 = QtWidgets.QPushButton("LAPLACIAN UYGULA")
        self.buton6.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton6.setFixedSize(300,50)
        
        self.buton7 = QtWidgets.QPushButton("UNSHARP UYGULA")
        self.buton7.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton7.setFixedSize(300,50)
        
        self.buton8 = QtWidgets.QPushButton("EMBOSSING UYGULA")
        self.buton8.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton8.setFixedSize(300,50)
        
        self.buton9 = QtWidgets.QPushButton("HIGH PASS UYGULA")
        self.buton9.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton9.setFixedSize(300,50)
        
        self.buton10 = QtWidgets.QPushButton("RENK UYUMLAMASI UYGULA")
        self.buton10.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton10.setFixedSize(300,50)
    
        self.buton11 = QtWidgets.QPushButton("İKİ RESMİ KARIŞTIRMA UYGULA")
        self.buton11.setStyleSheet('background-color : #f4b67c ; font-family : Times New Roman')
        self.buton11.setFixedSize(300,50)
        
        global resim
        resim = QtWidgets.QLabel() 
        
        global resim2
        resim2 = QtWidgets.QLabel()
        
        global resim_cikti
        resim_cikti = QtWidgets.QLabel()

        v_box = QGridLayout()
        v_box.addWidget(self.yazi_alani1,0,0)
        v_box.addWidget(dosya,1,0)
        
        v_box.addWidget(self.yazi_alani2,2,0)
        v_box.addWidget(dosya2,3,0)
        
        v_box.addWidget(self.buton,4,0)
        v_box.addWidget(self.buton1,4,1)
        v_box.addWidget(self.buton2,4,2)
        v_box.addWidget(self.buton3,4,3)
        v_box.addWidget(self.buton4,5,0)
        v_box.addWidget(self.buton5,5,1)
        v_box.addWidget(self.buton6,5,2)
        v_box.addWidget(self.buton7,5,3)
        v_box.addWidget(self.buton8,6,0)
        v_box.addWidget(self.buton9,6,1)
        v_box.addWidget(self.buton10,6,2)
        v_box.addWidget(self.buton11,6,3)
        
        v_box.addWidget(resim,7,0)
        v_box.addWidget(resim2,8,0)
        v_box.addWidget(resim_cikti,9,0)
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addLayout(v_box)
        
        self.setLayout(h_box) 
        
        self.buton.clicked.connect(self.resim_goster)  
        self.buton1.clicked.connect(self.tresholding)
        self.buton2.clicked.connect(self.histogram_esitleme)
        self.buton3.clicked.connect(self.median_blur)
        self.buton4.clicked.connect(self.mean_blur)
        self.buton5.clicked.connect(self.gauss)
        self.buton6.clicked.connect(self.laplacian)
        self.buton7.clicked.connect(self.unsharp)
        self.buton8.clicked.connect(self.embossing)
        self.buton9.clicked.connect(self.high_pass)
        self.buton10.clicked.connect(self.renk_uyumlamasi)
        self.buton11.clicked.connect(self.goruntu_karistirma)
        
        
        resim.setPixmap(QtGui.QPixmap("moon.jpg")) #bu şekilde etikete resim ekleyebilirsiniz. Burada PyQt5 in yukarıda da import ettiğimiz QtGui fonksiyonunu kullanıyoruz.
        resim.move(40,60)
        
        resim2.setPixmap(QtGui.QPixmap("moon.jpg"))
        
        self.show()
        


    def resim_goster(self):
        resim.setPixmap(QtGui.QPixmap(dosya.text()))  
        resim.move(40,60)
        resim2.setPixmap(QtGui.QPixmap(dosya2.text()))  
        resim2.move(40,60)
    
    
    def tresholding(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        _, thresh_img = cv2.threshold(gray_img, thresh= 45, maxval=255,
                              type=cv2.THRESH_BINARY)
        cv2.imwrite("tresh_resim.jpg",thresh_img)
        resim_cikti.setPixmap(QtGui.QPixmap("tresh_resim.jpg"))
        resim_cikti.move(40,60)
        
        
    def histogram_esitleme(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        filtered_img = cv2.equalizeHist(gray_img)
        cv2.imwrite("histogram_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("histogram_resim.jpg"))
        resim_cikti.move(40,60)
       
    # blurlama
    def median_blur(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        filtered_img = cv2.medianBlur(gray_img, 3)
        cv2.imwrite("median_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("median_resim.jpg"))
        resim_cikti.move(40,60)

    # blurlama
    def mean_blur(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        filtered_img = cv2.blur(gray_img,(3,3))
        cv2.imwrite("mean_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("mean_resim.jpg"))
        resim_cikti.move(40,60)
    
    # blurlama
    def gauss(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        filtered_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
        cv2.imwrite("gauss_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("gauss_resim.jpg"))
        resim_cikti.move(40,60)
        
        
    # kenar bulma
    def laplacian(self):
        img = cv2.imread(dosya.text(), cv2.IMREAD_COLOR)
        gauss_img = cv2.GaussianBlur(img, (3, 3), 0)
        gray_img = cv2.cvtColor(gauss_img, cv2.COLOR_BGR2GRAY)
        filtered_img = cv2.Laplacian(gray_img, cv2.CV_16S, ksize=3)
        cv2.imwrite("laplacian_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("laplacian_resim.jpg"))
        resim_cikti.move(40,60)
        
    
    # keskinleştirme
    def unsharp(self):
        img = cv2.imread(dosya.text())
        blur_img = cv2.GaussianBlur(img, (5, 5), 0)
        filtered_img = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
        cv2.imwrite("unsharp_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("unsharp_resim.jpg"))
        resim_cikti.move(40,60)
        
        
    # kabartma
    def embossing(self):
        gray_img = cv2.imread(dosya.text(), cv2.IMREAD_GRAYSCALE)
        kernel = np.array([[0, -1, -1],
                   [1, 0, -1],
                   [1, 1, 0]])
        filtered_img = cv2.filter2D(gray_img, -1, kernel)
        cv2.imwrite("embossing_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("embossing_resim.jpg"))
        resim_cikti.move(40,60)
        


    # yüksek geçiren
    def high_pass(self):
        img = cv2.imread(dosya.text())
        img = cv2.resize(img, (255, 255), 
                 interpolation=cv2.INTER_CUBIC)
        filtered_img = img - cv2.GaussianBlur(img, (21, 21), 3)+127
        cv2.imwrite("high_pass_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("high_pass_resim.jpg"))
        resim_cikti.move(40,60)
        
    
    # renk uyumlaması
    def renk_uyumlamasi(self):
        img1 = cv2.imread(dosya.text())
        img2 = cv2.imread(dosya2.text())
        source_lab = cv2.cvtColor(img1, cv2.COLOR_BGR2Lab)
        target_lab = cv2.cvtColor(img2, cv2.COLOR_BGR2Lab)
        source_mean, source_std = cv2.meanStdDev(source_lab)
        target_mean, target_std = cv2.meanStdDev(target_lab)
        result_lab = np.zeros_like(target_lab)
        result_lab[..., 0] = target_lab[..., 0]
        result_lab[..., 1] = ((target_lab[..., 1] - target_mean[1]) * (source_std[1] / target_std[1])) + source_mean[1]
        result_lab[..., 2] = ((target_lab[..., 2] - target_mean[2]) * (source_std[2] / target_std[2])) + source_mean[2]
        filtered_img = cv2.cvtColor(result_lab, cv2.COLOR_Lab2BGR)
        cv2.imwrite("renk_uyumlu_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("renk_uyumlu_resim.jpg"))
        resim_cikti.move(40,60)
        
    
    # goruntu karistirma
    def goruntu_karistirma(self):
        img1 = cv2.imread(dosya.text())
        img2 = cv2.imread(dosya2.text())
        mix2 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0) #img1x0.3 + img2x0.7 = mixed image
        mix1 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
        filtered_img =  cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
        cv2.imwrite("karistirilmis_resim.jpg",filtered_img)
        resim_cikti.setPixmap(QtGui.QPixmap("karistirilmis_resim.jpg"))
        resim_cikti.move(40,60)
        
        
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())