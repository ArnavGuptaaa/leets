import argparse
import os

# Configure parameters
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, required=True, help="Name of the problem (e.g., '123. Two Sum' or 'Topological Sort')")

# Mutually exclusive flags
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-lc", action="store_true", help="Flag for LeetCode problems")
group.add_argument("-gfg", action="store_true", help="Flag for GeeksforGeeks problems")

# Parse arguments
args = parser.parse_args()

# Validate file name
fileName = args.name.strip()
if fileName == "":
    raise Exception("Invalid file name")

# Handle input formats
if args.lc:
    parts = fileName.split(".")
    if len(parts) < 2:
        raise Exception("For LeetCode problems, name must be in the format '123. Problem Name'")
    questionNumber = parts[0].strip()
    questionName = ".".join(parts[1:]).strip()
    fileNameFormatted = "_".join(fileName.replace(".", "").split(" "))
    url = "<Add LeetCode link here>"
    targetDirectory = "./leetcode"

elif args.gfg:
    questionName = fileName
    fileNameFormatted = "_".join(fileName.split(" "))
    url = "<Add GeeksforGeeks link here>"
    targetDirectory = "./geeksforgeeks"

# Ensure target directory exists
os.makedirs(targetDirectory, exist_ok=True)

# Final file name
fileNameFormatted += ".py"
filePath = os.path.join(targetDirectory, fileNameFormatted)

# Check for file existence
if os.path.exists(filePath):
    raise Exception(f"'{filePath}' already exists")

# Header template
if args.lc:
    headerTemplate = f"""\"\"\"
Name: {questionName} (#{questionNumber})
URL: {url}

Time Complexity: O(?)
Space Complexity: O(?)
\"\"\"
"""
else:  # args.gfg
    headerTemplate = f"""\"\"\"
Name: {questionName}
URL: {url}

Time Complexity: O(?)
Space Complexity: O(?)
\"\"\"
"""

# Create and write to file
with open(filePath, 'w') as file:
    file.write(headerTemplate)