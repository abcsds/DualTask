from pylsl import StreamInfo, StreamOutlet

# Setup LSL outlet
info = StreamInfo("Psychopy", "Markers", 1, 0, "string", "PsychopyUUID0001")
outlet = StreamOutlet(info)
outlet.push_sample(["begin_experiment"])
