def data_type(some_data):
  try:
    if isinstance(some_data, str):
      return len(some_data)
  
    elif isinstance(some_data, bool):
      return some_data
    
    elif isinstance(some_data, int):
      
      if some_data < 100:
        return "less than 100"
    
      elif some_data == 100:
        return "equal to 100"
    
      else:
        return "more than 100"
      
    elif isinstance(some_data, list):
      if len(some_data) >= 3:
        return some_data[2]
    
    else:
      return None
    
  except TypeError: #raises an exception when no value is submitted
    return "No Value"
  
  
  
      
