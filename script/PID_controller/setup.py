import time as clock
import sys
class PIDController():
    kp:float
    ki:float
    kd:float
    curr_val:float
    target_val:float
    output_max:float
    output_min:float
    error:float
    acceptable_error:float
    time_diff:float
    output:float
    p:float
    i:float
    d:float
    