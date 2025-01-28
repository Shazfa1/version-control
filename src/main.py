import datetime
import os

# Get the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the path for version.md
# This assumes the script is run from the root of the repository
file_path = os.path.join('version-control', '..', 'version.md')

# Write the current time to version.md
with open(file_pathh, 'w') as f:
    f.write(current_time)
# date and time written to version.md
