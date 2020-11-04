print('How many Km\'s did you cycle today?')
kilometers = input()
miles = float(kilometers)/1.60934
miles = round(miles,2)
print(f'Your {kilometers}km ride was {miles}mil')