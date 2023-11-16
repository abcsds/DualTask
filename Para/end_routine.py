outlet.push_sample([f"end_routine_{{trials.thisN+1}}"])
for i in range(4): # Marks start of experiment
    arduino.write(b"p")
    outlet.push_sample([f"sync_{i+1}"])
    time.sleep(0.5)