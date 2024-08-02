from numpy import random
import math
import psychopy.logging as log
import serial
import time

# Function to calculate distance between two points
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
    
def rad2grad(rad):
    return rad*180/math.pi
    
def grad2rad(grad):
    return grad*math.pi/180
    
def angle2origin(pos):
    if pos[0] >= 0: 
        angle = math.atan(pos[1] / pos[0]) + math.pi 
    else:
        angle = math.atan(pos[1] / pos[0])
    return angle

# Setup serial connection to arduino
# Used for ttl triggers to EEG amp
arduino = serial.Serial("COM5", 9600)
for i in range(10): # Marks start of experiment
    arduino.write(b"p")
    outlet.push_sample([f"sync_{i+1}"])
    time.sleep(0.5)

# Define size of the circle
circle_radius = 10
circle_speed = 15
angle_uncertainty = math.pi/2

cross_color = "white"

# Define boundaries
boundary_x_min = -win.size[0] / 2 + circle_radius
boundary_x_max = win.size[0] / 2 - circle_radius
boundary_y_min = -win.size[1] / 2 + circle_radius
boundary_y_max = win.size[1] / 2 - circle_radius

# Define maximum tolerable distance from screen center
x_min = -win.size[0] / 2
x_max = win.size[1] / 2
y_min = -win.size[0] / 2
y_max = win.size[1] / 2

# Define la duración del estímulo 
stimulus_duration = 0.5 

# promedio de las duraciones entre estimulos
between_stimuli = 2.0

# proportion of x in list of all letters 
n_x = 2