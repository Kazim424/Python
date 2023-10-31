# WAP program to convert days in to years, weeks and days

days=int(input("Enter days: "))

# Conversion 

years = (days // 365)   # Ignoring leap year
weeks = (days % 365) / 7
days  = days - ((years * 365) + (weeks * 7))

# Print all resultant values 

print("YEARS: ", years)
print("WEEKS: ", weeks)
print("DAYS: ", days)