import math


#Instructions and welcome message
print "Hi, welcome to Rocketman. This is a Python based calculator to help you find values for your rocket.\n"
print "You can find thrust, acceleration, velocity, altitude, and drag over time.\n"
print "Enter 1 to begin calculating a single aspect, or 2 to calculate them all and make a spreadsheet. You don't really have a choice though, I haven't gotten to multiple options. Enter everything."
print "---------------------------------------------------------------------------------"
#End of instructions and welcome message


        #-----------------------------------------


#Directory
file = open("C:\Users\Coles\Documents\Python Writables\csv_t.csv","w") 
#End of file directory


        #-----------------------------------------


#Header write
file.write("Time (s), Thrust (weight units), Acceleration:, Velocity:, Altitude:, Drag:\n")
#End of header 


        #-----------------------------------------


#Column labeler
print " Variables \t \t \t Units \t \t \t \t  Inputs"
print "--------------------------------------------------------------------------------"
#End of column labeler


        #-----------------------------------------


#User variable prompts
air_density = input(" Air Density \t \t \t (kilograms per cubic meter) \t: ")
wet_mass = input(" Mass of Rocket With Fuel \t (kilograms) \t \t \t: ")
dry_mass = input(" Mass of Rocket Without Fuel \t (kilograms): ")
burnout = input(" Burnout \t \t \t (in seconds): ")
avg_thrust = input(" Average Thrust \t \t (in newtons): ")
gravity = input(" Gravity \t \t \t (in meters per second): ")
drag_coef = input(" Drag Coefficient: ")
diameter = input(" Diameter \t \t \t (in centimeters): ")

#End of user varible prompts


        #-----------------------------------------


#Thrust equation
def thrust_calc(time, burnout, avg_thrust):
    if time < burnout:
        return avg_thrust
    else:
        return 0

#End of thrust equation
#-----------------------------------------------
#Area equation LOOK AT THIS FOR ISSUES
def area_calc(diameter):
    return (((diameter / 100) / 2) ** 2) * math.pi
    #return diameter
    
#End of area equation
#-----------------------------------------------
#Acceleration equation
def acceleration_calc(mass, thrust, drag):
        return ((thrust - drag) / mass) - gravity
    
#End of acceleration equation
#-----------------------------------------------
#Velocity equation
def velocity_calc(velocity, time_step, acceleration):
        return velocity + acceleration * time_step

#End of velocity equation
#-----------------------------------------------
#Altitude equation
def altitude_calc(altitude, acceleration, velocity, time_step):
        return altitude + (velocity * time_step)

#End of altitude equation
#-----------------------------------------------
#Drag equation
def drag_calc(drag_coef, area, air_density, velocity):
    if velocity > 0:
        return 0.5 * drag_coef * area * air_density * velocity ** (2)
    else:
        return abs(0.5 * drag_coef * area * air_density * velocity ** (2))   

#End of drag equation
#-----------------------------------------------
#Mass equation LOOK AT THIS FOR ISSUES
def mass_calc(wet_mass, dry_mass, burnout, time):
    if time < burnout:
        return wet_mass - (((wet_mass - dry_mass) / burnout) * time)
    if time > burnout:
        return dry_mass

    
#End of mass equation
#-----------------------------------------------


        #-----------------------------------------


#Starting values
time = 0
time_step = 0.1
area = area_calc(diameter)
velocity = 0
altitude = 0
acceleration = 0
drag = 0
#Zeros


        #-----------------------------------------


#Bug fixing tool kit
print("Time (s), Thrust (weight units), Acceleration:, Velocity:, Altitude:, Drag:\n")
#End Bug fixing tool kit


        #-----------------------------------------


#Calulations and writing
for x in range(1, 631):
    time = time + time_step
    mass = mass_calc(wet_mass, dry_mass, burnout, time)
    thrust = thrust_calc(time, burnout, avg_thrust)
    drag = drag_calc(drag_coef, area, air_density, velocity)
    acceleration = acceleration_calc(mass, thrust, drag)
    velocity = velocity_calc(velocity, time_step, acceleration)
    altitude = altitude_calc(altitude, acceleration, velocity, time_step)
    file.write("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n" % (time, thrust, acceleration, velocity, altitude, drag))
    print("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n" % (time, thrust, acceleration, velocity, altitude, drag))
    if altitude < 0:
        break
file.close()
#End of calculations and writing

