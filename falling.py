# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fall_time(altitude,mass=100,c2=0,vi=0):
   

    timestep=0.001
    time=0
   
    new_pos=altitude
    new_vel=vi
    new_acc=-9.8
   
    pos_array=[new_pos]
    vel_array=[new_vel]
    time_array=[time]
    
  
    
    while new_pos > 0:
        old_pos=new_pos
        old_vel=new_vel
        old_acc=new_acc
        
        new_pos= old_pos + old_vel*timestep+0.5*old_acc*timestep*timestep
        new_vel= old_vel + old_acc*timestep
        
        new_acc= -9.8 -  (c2/float(mass))*new_vel*abs(new_vel)
        
        time=time+timestep
        
        pos_array.append(new_pos)
        vel_array.append(new_vel)
        time_array.append(time)
        
    
    print(time)
    
    return pos_array,vel_array,time_array
   



#example code
"""
results1=fall_time(100,c2=0)
results2=fall_time(100,c2=0.5)
results3=fall_time(1000,80,c2=0.25,vi=40)
import matplotlib.pyplot as plt
plt.plot(results3[0],results[2])
"""