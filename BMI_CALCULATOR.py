#Welcome to the BMI Calculator 🏋️‍♀️

#Weight and Height
Weight = int(input("Whats your Weight in kg? "))
Height = float(input("Whats your Height in m? "))

#Calculate BMI 🧮
Height_Squard = Height ** 2
BMI = Weight / Height_Squard

overall_BMI = round(BMI, 1)
print(overall_BMI)