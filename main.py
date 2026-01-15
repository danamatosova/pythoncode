from datetime import datetime

# Get the current date and time
now = datetime.now()

# Print the raw object
print("Current Date and Time (Raw):", now)

# Format the output for better readability
# %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %S = Second
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_now)