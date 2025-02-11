# Ask the user for the number of cents as an integer (e.g. 99, not 0.99).
number_of_cents = int(input("Enter the number of cents: "))

# Calculate the number of quarters
quarters = number_of_cents // 25
# Calculate the remaining change
remaining_change = number_of_cents % 25
# Calculate the number of dimes
dimes = remaining_change // 10
# Calculate the remaining change
remaining_change = remaining_change % 10
# Calculate the number of nickels
nickels = remaining_change // 5
# Calculate the remaining cents 
remaining_cents = remaining_change % 5

# Print out the result
print(f"Quarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {remaining_cents}")

