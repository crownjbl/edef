from edef import EventDefinition
import time

my_edef = EventDefinition("Matt's EDEF", user="mgibbs") #Will raise an exception if no EDEFs available.

# You can set inclusion/exclusion masks with a list of modifier bits.
# Use the name for each bit.  The names are case sensitive, so watch out!
my_edef.inclusion_masks = ["pockcel_perm", "BKRCUS"]
my_edef.exclusion_maks = ["TS2", "TS3", "TS5", "TS6"]

# Set number of measurements to acquire.  Your value will be clipped to the
# limits of the BSA system (currenly -1 to 2800).
# -1 means acquire "forever", constantly filling the 2800-point buffer.
my_edef.n_measurements = 500
caput("EDEF:SYS0:{edef_num}:BEAMCODE".format(edef_num=my_edef.edef_num), 2)
# Now, start the acquisition.
my_edef.start()

# Wait for the edef to collect all 500 points.  Alternatively, you can 
# set a callback function to run when acquisition is complete instead.
while not my_edef.is_acquisition_complete():
    time.sleep(0.1)
 
def my_done_callback():
    print(my_edef.get_data_buffer("BPMS:LTUH:250:X"))
    
my_edef.done_callback = my_callback
my_edef.start()

#You can use the edef object to get the acquired data for your edef.
dl2_bpm_data = my_edef.get_data_buffer("BPMS:LTUH:250:X")
print(dl2_bpm_data)


#Please release your edef when you are done!
my_edef.release()