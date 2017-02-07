def fizz_buzz(entry):
	if type(entry) != int or type(entry) != float: #eliminates non-numbers
		raise TypeError("THE ENTRIES ARE WRONG!!")

	elif entry % 3 == 0 and entry % 5 == 0: #tests for numbers that are divisible by both three and five
		return "FizzBuzz"

	elif entry % 3 == 0: #tests for numbers that are divisible by three 
		return "Fizz"

	elif entry % 5 == 0: #tests for numbers that are divisible by five
		return "Buzz"

	else: 
		return None
