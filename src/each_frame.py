# Only start moving after one second (fixation cross)
if core.getTime() >= routine_start_time + 1:
    # Calculate the new position based on speed and direction
    circle_pos[0] += circle_speed * math.cos(circle_direction)
    circle_pos[1] += circle_speed * math.sin(circle_direction)

# Check square new position bassed of mouse direction 
square_pos = mouse.getPos()
win.flip()

# Randomly adjust direction
if random.random() < 0.2:  # 20% chance of direction change on every frame
    circle_direction += random.uniform(-angle_uncertainty/2, angle_uncertainty/2)

# Check for collisions with boundaries
# if circle_pos[0] <= boundary_x_min or circle_pos[0] >= boundary_x_max:
#     circle_direction = math.pi - circle_direction
# if circle_pos[1] <= boundary_y_min or circle_pos[1] >= boundary_y_max:
#     circle_direction = -circle_direction

# Check for out of bounds conditions
#out_of_bounds = circle_pos[0] <= x_min or circle_pos[0] >= x_max
#out_of_bounds = out_of_bounds or circle_pos[1] <= y_min or circle_pos[1] >= y_max
out_of_bounds = circle_pos[0] <= boundary_x_min or circle_pos[0] >= boundary_x_max
out_of_bounds = out_of_bounds or circle_pos[1] <= boundary_y_min or circle_pos[1] >= boundary_y_max
if out_of_bounds:
    circle_direction = angle2origin(circle.pos)

mouse_pos = mouse.getPos()
dist = distance(mouse_pos, circle.pos)
log.exp(f"Distance = {dist}")

# Update figure color based on distance (adjust the values)
if dist < 100:
    square.borderColor = "limegreen"
elif dist < 200:
    square.borderColor = "yellow"
else:
    square.borderColor = "red"

# Check for fixation cross flash
if core.getTime() >= next_flash_time:
    last_flash_time = next_flash_time
    stimulus = random.choice(all_letters)
    win.flip()
    log.exp(f"New stimulus letter: {stimulus}")
    next_flash_time = core.getTime() + stimulus_duration + random.normal(loc=between_stimuli, scale=1)  # Schedule the next flash
    offset_time = last_flash_time + stimulus_duration
    
if core.getTime() >= offset_time:
   stimulus = ""
   win.flip()
   # log.exp(f"Removed stimulus letter")



  
