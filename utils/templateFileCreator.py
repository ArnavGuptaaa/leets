import argparse

# Configure parameters
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, required=True)

# Parse arguments
args = parser.parse_args()

# Basic Validation
fileName = args.name.strip()
if fileName == "":
    raise Exception("invalid file name")

# Extract question number and question name
questionNumber = fileName.split('.')[0].strip()
questionName = fileName.split('.')[1].strip()

# Form header template
fileName = "_".join(fileName.replace(".", "").split(" "))
fileName += ".py"

headerTemplate = f"""\"\"\"
Name: {questionName} (#{questionNumber})
URL: <Add question link here>

Time Complexity: O(?)
Space Complexity: O(?)
\"\"\"
"""

# Create and write to file
with open(f'./{fileName}', 'w') as file:
    file.write(headerTemplate)
    file.close()