    
  
class Car(object):
  """This car class can be used to instantiate various vehicles. Each car has got different attributes:
  name: eg Toyota, Honda
  model: eg Corrola
  type: eg truck, trailer"""
  
  
  def __init__(self, name, model, car_type):
    #a function to initialize the Car class
    self.car_type = car_type
    self.model = model
    if name == None:
      self.name = "General"
    else:
      self.name = name
      
    if name == "Koenigsegg" or name == "Agera R"":
      self.num_of_doors = 4
    else:
      self.num_of_doors = 2

      
      
  