#!/usr/bin/python
# _*_ coding: utf-8 _*_
import tkinter as tk # STANDARD
from tkinter import messagebox # STANDARD
import tkinter.font as tkFont # STANDARD
import tkinter.scrolledtext as ts # STANDARD
from PIL import Image, ImageTk # NON-STANDARD Allows the use of different image formats
import os # STANDARD
import vlc 
import time 
import subprocess
import Sorteador

import simpleaudio as sa
import time


# V-I-E-W
# Dynamically renders the GUI

######## TO DO
##### 1. DYNAMICALLY RENDER GUI, using lambdas probably?
##### 2. SENDING BACK TO CONTROLLER DATABASE ACTIONS

# 1. ROOT -> 2. CANVAS (adds Widgets and Bkg)

''' View Object of Universidad'''


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        # Declarar protocolos (links entre ventana events y script) parte de Tk()
        self.PATH_ICON = os.path.relpath("assets\\icon.ico")
        self.title("1000 Esferas con Causa - Pioneros del Cambio AC")
        self.iconbitmap(self.PATH_ICON)

        self.lift()
        self.attributes("-topmost", True)

        
        # Centrar ventana en la pantalla
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))


        # Protocolos de ventana
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Crear Frame dentro de Tk
        HomePage(self, "assets\\home-bkg.png")
        

    def on_closing(self):
        if messagebox.askokcancel(message="¿Está seguro que desea salir?", title="1000 Esferas con Causa"):
            self.destroy()
        

class HomePage(tk.Canvas):
    def __init__(self, ROOT, BKG_PATH):
        # Atributos CONSTANTES
        self.ROOT = ROOT
        self.BORDER_WIDTH=0
        self.HIGHLIGHT_THICKNESS=0
        self.HIGHLIGHT_COLOR = '#E4E4E4'
        self.WIDTH = 1920
        self.HEIGHT = 1080
        
        # Atributos VARIABLES
        self.BKG_PATH = BKG_PATH

        # FONST
        self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
        self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=12)
        self.fontStyle3 = tkFont.Font(family="Montserrat ExtraBold", size=9)

        # CANVAS constructor!
        super().__init__(ROOT, width = self.WIDTH, height = self.HEIGHT, 
                        highlightthickness = self.HIGHLIGHT_THICKNESS, highlightbackground = self.HIGHLIGHT_COLOR)

        # BKG setup!
        # bUG MYSTERIOUS PADDING WHEN THICKNESS != 0 CHECK TEMP

        self.pil_img = Image.open(self.BKG_PATH)
        self.r_img = self.pil_img.resize((self.WIDTH, self.HEIGHT))
        self.img = ImageTk.PhotoImage(self.r_img)
        self.bg = self.create_image(0, 0, anchor = tk.NW, image=self.img)
        
        
         # Entrar Button
        self.addWidget(tk.Button(self, 
                                    text="Entrar", 
                                    anchor = tk.CENTER,
                                    bg = "#FE9C33",
                                    foreground = "#B4302A",
                                    width = "100",
                                    height = "1",
                                    bd = "4",
                                     font = self.fontStyle,
                                    command = self.go_next_page), 980, 1000)

        # Author text  
        self.create_text(1760,900, fill="black",
                                        text="Desarrollado por Jorge Flores",
                                        justify = tk.RIGHT,
                                        font = self.fontStyle3)


        # CANVAS Geometry Manager
        self.place(x = 0, y = 0)
    
    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def go_next_page(self):
        
        SuertePage(self.ROOT, "assets\\suerte-bkg.png")
        self.destroy()
        
class SuertePage(tk.Canvas):
   
    def __init__(self, ROOT, BKG_PATH):
        # FONST
        sa.stop_all()
        self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
        self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=15)
        self.fontStyle3 = tkFont.Font(family="Montserrat ExtraBold", size=9)

        # Atributos CONSTANTES
        self.ROOT = ROOT
        self.BORDER_WIDTH=0
        self.HIGHLIGHT_THICKNESS=0
        self.HIGHLIGHT_COLOR = '#E4E4E4'
        self.WIDTH = 1920
        self.HEIGHT = 1080

        # Atributos VARIABLES
        self.BKG_PATH = BKG_PATH

        

        # CANVAS constructor!
        super().__init__(ROOT, width = self.WIDTH, height = self.HEIGHT, 
                        highlightthickness = self.HIGHLIGHT_THICKNESS, highlightbackground = self.HIGHLIGHT_COLOR)

        # BKG setup!
        # bUG MYSTERIOUS PADDING WHEN THICKNESS != 0 CHECK TEMP

        self.pil_img = Image.open(self.BKG_PATH)
        self.r_img = self.pil_img.resize((self.WIDTH, self.HEIGHT))
        self.img = ImageTk.PhotoImage(self.r_img)
        self.bg = self.create_image(0, 0, anchor = tk.NW, image=self.img)
        
        
         # WIDGETS
        self.plt = self.create_text(3000,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)
        self.slt = self.create_text(3500,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)
        self.tlt = self.create_text(3500,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)
       # Revisar Alumnos Button



        # Entrar Button
        self.siguiente = self.addWidget(tk.Button(self, 
                                    text="Continuar", 
                                    anchor = tk.CENTER,
                                    bg = "#FE9C33",
                                    foreground = "#B4302A",
                                    width = "100",
                                    height = "1",
                                    bd = "4",
                                    font = self.fontStyle,
                                    command = self.go_next_page), 980, 1000)

        # Atrás button
        self.addWidget(tk.Button(self, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#FE9C33",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "0",
                                font = self.fontStyle3,
                                command = self.go_frame_back), 100, 50)

        # CANVAS Geometry Manager
        self.place(x = 0, y = 0)
        

    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def go_frame_back(self):
        HomePage(self.ROOT, "assets\\home-bkg.png")
        self.destroy()
        #self.forget()
    
    def go_next_page(self):
        SorteoPage(self.ROOT, "assets\\lottery-bkg.png")
        #INTERESITING IMPORT
       

class SorteoPage(tk.Canvas):
    def __init__(self, ROOT, BKG_PATH):
        
        # FONST
        self.fontStyle = tkFont.Font(family="Montserrat ExtraBold", size=30)
        self.fontStyle2 = tkFont.Font(family="Montserrat ExtraBold", size=15)
        self.fontStyle3 = tkFont.Font(family="Montserrat ExtraBold", size=9)
        self.fontStyle4 = tkFont.Font(family="Montserrat ExtraBold", size=15)

        # Atributos CONSTANTES
        self.ROOT = ROOT
        self.BORDER_WIDTH=0
        self.HIGHLIGHT_THICKNESS=0
        self.HIGHLIGHT_COLOR = '#E4E4E4'
        self.WIDTH = 1920
        self.HEIGHT = 1080

        # Atributos VARIABLES
        self.BKG_PATH = BKG_PATH

        

        # CANVAS constructor!
        super().__init__(ROOT, width = self.WIDTH, height = self.HEIGHT, 
                        highlightthickness = self.HIGHLIGHT_THICKNESS, highlightbackground = self.HIGHLIGHT_COLOR)

        # BKG setup!
        # bUG MYSTERIOUS PADDING WHEN THICKNESS != 0 CHECK TEMP

        self.pil_img = Image.open(self.BKG_PATH)
        self.r_img = self.pil_img.resize((self.WIDTH, self.HEIGHT))
        self.img = ImageTk.PhotoImage(self.r_img)
        self.bg = self.create_image(0, 0, anchor = tk.NW, image=self.img)
        
        
         # WIDGETS
        self.plt = self.create_text(3000,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)
        self.slt = self.create_text(3500,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)
        self.tlt = self.create_text(3500,900, fill="black",
                                        text="pl",
                                        font = self.fontStyle2)


        #self.textBox = self.addWidget(ts.ScrolledText(self, width = 80, height = 10), 400, 850)
        
       # Revisar Alumnos Button



        # Entrar Button
        self.empezar = self.addWidget(tk.Button(self, 
                                    text="Empezar!", 
                                    anchor = tk.CENTER,
                                    bg = "#FE9C33",
                                    foreground = "#B4302A",
                                    width = "100",
                                    height = "1",
                                    bd = "4",
                                    font = self.fontStyle,
                                    command = self.girar), 980, 1000)

        # Atrás button
        self.addWidget(tk.Button(self, 
                                text="Atrás", 
                                anchor = tk.CENTER,
                                bg = "#FE9C33",
                                foreground = "white",
                                width = "18",
                                height = "1",
                                bd = "0",
                                font = self.fontStyle3,
                                command = self.go_frame_back), 100, 50)


        # CANVAS Geometry Manager
        self.x = 0
        self.place(x = 0, y = 0)

        

    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def go_frame_back(self):
        SuertePage(self.ROOT, "assets\\suerte-bkg.png")
        self.destroy()
        #self.forget()

    def girar(self):
        #INTERESITING IMPOR
        
        if self.x > -1 and self.x < 300:
            #if self.x == 0:
             #   self.drumsSound = sa.WaveObject.from_wave_file("assets/drum.wav")
             #   self.drumsSound.play()
            Instancia = Sorteador.Sorteador("assets/participantes.csv")
            Instancia.start()
            
            self.pl = Instancia.primerLugar
            self.sl = Instancia.segundoLugar
            self.tl = Instancia.tercerLugar

            # Selects a random guy for display
            self.random = Instancia.df.sample(1)
            self.random_guy = str(self.random.iloc[0, 0])


            # Borra el random guy
            self.delete(self.tlt)

            self.tlt = self.create_text(1580,850, fill="black",
                                            text=self.random_guy,
                                            justify = tk.RIGHT,
                                            font = self.fontStyle2)

            self.x = self.x + 1
            self.ROOT.after(100, self.girar)
        
        elif self.x >= 600 and self.x <= 900:
            #if self.x == 201:
            #    winnerSound = sa.WaveObject.from_wave_file("assets/winner.wav")
            #    winnerSound.play()

            Instancia = Sorteador.Sorteador("assets/participantes.csv")
            Instancia.start()


            if self.x == 601:
                # GANADOR SEGUNDO LUGAR
                self.delete(self.slt)
                self.slt = self.create_text(1000,850, fill="black",
                                            text=self.sl,
                                            justify = tk.RIGHT,
                                            font = self.fontStyle2)




            
            # Selects a random guy for display
            self.random = Instancia.df.sample(1)
            self.random_guy = str(self.random.iloc[0, 0])


            # Borra el random guy
            self.delete(self.plt)


            self.plt = self.create_text(400,850, fill="black",
                                            text=self.random_guy,
                                            justify = tk.RIGHT,
                                            font = self.fontStyle2)
            

            self.x = self.x + 1
            self.ROOT.after(100, self.girar)
            
        elif self.x >= 300 and self.x < 600:
            Instancia = Sorteador.Sorteador("assets/participantes.csv")
            Instancia.start()

            if self.x == 301:
                # GANADOR TERCER LUGAR
                self.delete(self.tlt)
                self.tlt = self.create_text(1580,850, fill="black",
                                                text=self.tl,
                                                justify = tk.RIGHT,
                                                font = self.fontStyle2)

            #if self.x == 101:
            #    winnerSound = sa.WaveObject.from_wave_file("assets/winner.wav")
            #    winnerSound.play()
            
            # Selects a random guy for display
            self.random = Instancia.df.sample(1)
            self.random_guy = str(self.random.iloc[0, 0])


            # Borra el random guy
            self.delete(self.slt)


            

            
            self.slt = self.create_text(1000,850, fill="black",
                                            text=self.random_guy,
                                            justify = tk.RIGHT,
                                            font = self.fontStyle2)

            self.x = self.x + 1
            self.ROOT.after(100, self.girar)

        else:
            # GANADOR PRIMER LUGAR
            self.delete(self.plt)
            self.plt = self.create_text(400,850, fill="black",
                                            text=self.pl,
                                            justify = tk.RIGHT,
                                            font = self.fontStyle2)
            self.x = 0
            
            # REGISTRA LOS GANADORES
            with open('assets/registro.txt', 'w') as writer:
                writer.write("TERCER LUGAR ")
                writer.write(self.tl)
                writer.write("\n")
                writer.write("SEGUNDO LUGAR ")
                writer.write(self.sl)
                writer.write("\n")
                writer.write("PRIMER LUGAR ")
                writer.write(self.pl)

            return
        
    def preparar(self):
        self.x = 0
       

# creating vlc media player object
subprocess.run("Python Intro.py", cwd="bin\\")

Root().mainloop()