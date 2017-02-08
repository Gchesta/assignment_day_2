
class Car(object):
  
  def __init__(self, name="General", model="GM", car_type="saloon"):
    #The car should be called `General` if no name was passed as an argument
    #The car's model should be called `GM` if no model was passed as an argument
    #The car type should be saloon if it is not a trailer
    self.name = name
    self.model = model
    self.car_type = car_type
    self.speed = 0 
    
    #The car shoud have four (4) doors except its a Porshe or Koenigsegg
    if self.name == "Porshe" or self.name == "Koenigsegg":
      self.num_of_doors = 2
    
    else:
      self.num_of_doors = 4
    
    #The car shoud have four (4) wheels except its a type of trailer
    if self.car_type == "trailer":
      self.num_of_wheels = 8
  
    else:
      self.num_of_wheels = 4
  
  #The car type should be saloon if it is not a trailer
  def is_saloon(self):
    if self.car_type == "saloon":
      return True
    return False
    
  def drive(self, factor):
    #The Trailer should have speed 0 km/h until you put `the pedal to the metal
    if self.name == "Mercedes":
      self.speed = 10 ** factor
    
    #The Mercedes should have speed 0 km/h until you put `the pedal to the metal  
    elif self.car_type == "trailer":
      self.speed = 11 * factor
      
    return self
