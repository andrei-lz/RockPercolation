from tkinter import *
import time
import numpy as np
import matplotlib.pyplot as plt

class Frame:

    def __init__(self, display_matrices: list):
        self.tk = Tk()

        self.height = 1366
        self.width = 1068

        self.tk.geometry("1366x1068")
        self.canvas = Canvas(self.tk, width = self.width, height = self.height)
        self.tk.title("Percolation Simulation")
        self.canvas.pack()

        self.display_matrix(display_matrices[10], 10, 10)

    def update(self):
        self.tk.update()
        time.sleep(0.1)

    def display_matrix(self, matrix, xOff, yOff):
        rowCount = 0
        for row in matrix:
            columnCount = 0
            for column in row:
                value = matrix[rowCount][columnCount]
                if value == 1:
                    color = "black"
                elif value == 2:
                    color = "blue"
                else:
                    color = "white"

                size = 10
                xPos = xOff+(size*rowCount)
                yPos = yOff+(size*columnCount)
                
                self.canvas.create_rectangle(xPos, yPos, xPos+size, yPos+size, fill=color)
                columnCount+=1
            rowCount+= 1