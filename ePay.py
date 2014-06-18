
#EXERCISE1
#rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes 2 parameter (hours and rate)

def computePay():
   '''
   The program take hours and rate, and calculate the ordinary payment and extra payment if apply.
   Extraordinary payment applies only if hours per week exceed 40 hours, otherwise ordinary payment is applying.
   The program does not recognize the numbers as string, please enter only numbers 
   >>>computePay(40,8)
   >>>320.0
   >>>ComputePay(45,10)
   >>>475.0
   '''
   extra_pay = 0
   while True:
      try:
         hours = int(input("Please enter a number for hours: \n"))
         break
      except ValueError:
         print("Oops!  That was no valid number. Please enter a valid value for hours...")

   while True:
      try:
         rate = int(input("Please enter a number for rate: \n"))
         break
      except ValueError:
         print("Oops!  That was no valid number. Please enter a valid value for rare...")
   if hours <= 40:
      ordinary_pay = 40 * rate
      
   else:
      ordinary_pay = 40 * rate
      extra_pay = (hours - 40) * rate * 1.5
   
   total_pay = ordinary_pay + extra_pay
   return float(total_pay)


print(computePay())
