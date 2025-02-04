# Loop through numbers from 1000 to 2000, counting by 25
for i in range(1000, 2001, 25):
    # Check if the number is divisible by 25
    if i % 25 == 0:
        print(i)  # Print the number if it's divisible by 25
