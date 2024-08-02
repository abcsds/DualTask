outlet.push_sample([f"begin_routine_{{trials.thisN+1}}"])
for i in range(5): # Marks start of experiment
    arduino.write(b"p")
    outlet.push_sample([f"sync_{i+1}"])
    time.sleep(0.5)

routine_start_time = core.getTime()
next_flash_time = routine_start_time + stimulus_duration + random.normal(loc=between_stimuli, scale=1) + 1 # Initial flash time

stimulus = "X"
all_letters = ["M", "N", "Y", "A", "U", "H"]

all_letters = all_letters + (["X"] * n_x)

last_flash_time = None 
offset_time = core.getTime() + stimulus_duration

# Set the mouse and target at the center of the screen
mouse.setPos([0,0])
circle_pos = [0,0]
circle.setPos([0,0])
circle_direction = random.uniform(0, 2 * math.pi)  # Initial direction (random)

# Log the trial number
log.exp(f"Trial begin: {trials.thisN+1}")
