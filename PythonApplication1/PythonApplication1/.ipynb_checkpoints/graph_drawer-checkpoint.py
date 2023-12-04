# graph_drawer.py

import tkinter as tk

def draw_graph(canvas, vertices, edges):
    for edge in edges:
        canvas.create_line(vertices[edge[0]][0], vertices[edge[0]][1],
                           vertices[edge[1]][0], vertices[edge[1]][1],
                           width=2)

    for vertex in vertices:
        canvas.create_oval(vertex[0] - 10, vertex[1] - 10, 
                           vertex[0] + 10, vertex[1] + 10, 
                           fill='blue')

