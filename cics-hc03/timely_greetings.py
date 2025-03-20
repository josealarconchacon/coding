# Get the hour of the day from the user
hour = int(input("Enter hour (in 24 hour time): "))

morning_hours = range(0, 12) # hold morning hours
afternoon_hours = range(12, 17) # hold afternoon hours

# Validate the input
if hour < 0 or hour > 23:
    print("Invalid hour. Please enter a value between 0 and 23.")
else:
    # Determine the greeting based on the hour
    if hour in morning_hours:
        print("Good Morning")
    elif hour in afternoon_hours:
        print("Good Afternoon")
    else:
        print("Good Evening")