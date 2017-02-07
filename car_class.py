
class Car(object):
  """This car class can be used to instantiate various vehicles. Each car has got different attributes:
  name: eg Toyota, Honda
  model: eg Corrola
  type: eg truck, trailer"""
  
  
  def __init__(self, name, model, car_type):
    #a function to initialize the Car class
    
    self.model = model
    
    #estblish a saloon car as the default non-trailer car
    if car_type== "Trailer":
      self.car_type = car_type
    else:
      self.car_type = "Saloon"
    
   
   #establishing the default name "General" 
    if name == None:
      self.name = "General"
    else:
      self.name = name
    
    #establishing conditions for the number of doors  
    if name == "Koenigsegg" or name == "Agera R"":
      self.num_of_doors = 4
    else:
      self.num_of_doors = 2
      
    #establishing conditions for the number of wheels  
    if car_type == "Trailer":
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


      
      
  