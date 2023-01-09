from setup import *
# Controller:PIDController
# Controller.kp = Controller.ki = Controller.kd = Controller.p = Controller.i = Controller.d=0
# Controller.output_max = sys.float_info.max
# Controller.output_min = sys.float_info.min
class Controller(PIDController):
    def __init__(self):
        self.kp = self.ki = self.kd = self.p = self.i = self.d = 0
        self.output_max = sys.float_info.max
        self.output_min = sys.float_info.min
        self.prev_time = self.curr_time = clock.time()
        self.acceptable_error=0
    def setConst(self,vals:list):
        self.kp,self.ki,self.kd,self.acceptable_error = vals
        self.output=0
        
    def limit(self,output_max,output_min,value):
        if value>output_max:
            return output_max
        if value<output_min:
            return output_min
        else:
            return value
    def setCurrentValue(self,val):
        self.curr_val = val
    def setTargetValue(self,val):
        self.target_val = val
    
    
Car = Controller()
Car.setConst([1,2,3,4])
print(Car.acceptable_error,Car.kp)

