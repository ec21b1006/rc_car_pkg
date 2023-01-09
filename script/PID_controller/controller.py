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
    def UpdateOutput(self):
        self.curr_time = clock.time()
        self.time_diff = max(self.curr_time-self.prev_time,0.01)
        self.prev_time = self.curr_time
        self.error = self.target_val - self.curr_val
        if abs(self.error)>=0 and abs(self.error)<=self.acceptable_error:
            self.error=0
        self.p = self.kp*self.error
        self.i = self.ki*self.error*self.time_diff
        #Limit to range
        self.d = self.kd*self.error/self.time_diff
        self.output = self.p+self.i+self.d
        return self.output
    


