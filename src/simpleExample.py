from psychopy import visual, event, core
import random
import math

# Function to calculate distance between two points
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

# Create a window
win = visual.Window([800, 600], color="black", units="pix")

# Circle parameters
circle_radius = 20
circle_speed = 5  # Initial speed
circle_direction = random.uniform(0, 2 * math.pi)  # Initial direction (random)

# Create a figure
figure = visual.Circle(win, radius=circle_radius, pos=[0, 0], fillColor="white")

# Create a mouse object to track mouse position
mouse = event.Mouse()

# Initialize variables
initial_mouse_pos = [0, 0]
clock = core.Clock()
cross_color = "white"

# Define boundaries
boundary_x_min = -win.size[0] / 2 + circle_radius
boundary_x_max = win.size[0] / 2 - circle_radius
boundary_y_min = -win.size[1] / 2 + circle_radius
boundary_y_max = win.size[1] / 2 - circle_radius

# Fixation cross parameters
fixation_cross = visual.TextStim(win, text="+", color="white", height=40, pos=(0, 0))
next_flash_time = core.getTime() + random.uniform(2, 4)  # Initial flash time

# Response variables
response_times = []
distances = []

try:
    # Start the experiment loop
    while True:
        # Check for quit event
        if event.getKeys(keyList=["escape"]):
            break

        # Check for fixation cross flash
        if core.getTime() >= next_flash_time:
            print(cross_color)
            last_flash_time = next_flash_time  # Store last flashing time
            fixation_cross.fillColor = "#888888"  # Asign the color gray (written in Hexadecimal)
            fixation_cross.draw()
            win.flip()
            response = event.waitKeys(keyList=["left"], maxWait=1)  # Wait for a left mouse button click
            if response:
                response_time = response[0]
                response_times.append(response_time)
                mouse_pos = mouse.getPos()
                dist = distance(mouse_pos, figure.pos)
                distances.append(dist)
            next_flash_time = core.getTime() + random.uniform(2, 4)  # Schedule the next flash
        
        if core.getTime() >= last_flash_time + 0.2:  # last flash time + 200 ms
            fixation_cross.fillColor = "White"  # Change back to white
            fixation_cross.draw()
            win.flip()

        # Get the current mouse position
        mouse_pos = mouse.getPos()

        # Calculate distance between mouse and figure
        dist = distance(mouse_pos, figure.pos)

        # Update figure color based on distance (adjust the values)
        if dist < 100:
            figure.fillColor = "red"
        elif dist < 200:
            figure.fillColor = "green"
        else:
            figure.fillColor = "blue"

        # Calculate the new position based on speed and direction
        figure.pos[0] += circle_speed * math.cos(circle_direction)
        figure.pos[1] += circle_speed * math.sin(circle_direction)

        # Check for collisions with boundaries
        if figure.pos[0] <= boundary_x_min or figure.pos[0] >= boundary_x_max:
            circle_direction = math.pi - circle_direction
        if figure.pos[1] <= boundary_y_min or figure.pos[1] >= boundary_y_max:
            circle_direction = -circle_direction

        # Randomly adjust speed and direction
        if random.random() < 0.02:  # 2% chance
            circle_speed = random.uniform(1, 5)
            circle_direction = random.uniform(0, 2 * math.pi)

        # Update initial mouse position at the beginning of the experiment
        if clock.getTime() == 0:
            initial_mouse_pos = mouse_pos

        # Draw the figure
        figure.draw()

        # Flip the window
        win.flip()

except KeyboardInterrupt:
    pass

# Close the window
win.close()
core.quit()

# Print response times and distances
print("Response Times (seconds):", response_times)
print("Distances from Figure (pixels):", distances)
