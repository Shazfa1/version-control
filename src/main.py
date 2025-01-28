import datetime
import os

# Get the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write the current time to version.md
with open('output/version.md', 'w') as f:
    f.write(current_time)
# date and time written to version.md
