<!-- TITLE -->

# Leets

This repository contains my solutions to various LeetCode problems.

<div align="center">
    <img src="./readme/leetcodeMeme.png" alt="leetcode meme" />
</div>

<!-- TITLE ENDS -->

<!-- STRUCTURE -->

## Structure

Every file must be named in an underscore-separated format as shown below.

```txt
3_Longest_Substring_Without_Repeating_Characters.py
```

Each problem is stored as a separate `.py` file with the following format:

```python
"""
Name: [Problem Name] (#Problem Number)
URL: https://leetcode.com/problems/[problem-name]/

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def function(self, *args):
        pass
```

<!-- STRUCTURE ENDS -->

<!-- SCRIPT -->

## File Creation Script

Users can leverage `./utils/templateFileCreator.py` to create a template file.

Run the script and use the `-n` or `--name` flag to pass the question name (copied directly from LeetCode)

> [!IMPORTANT]
> In order for the script to work as expected, users must run this script in `leets/` folder

```bash
$ python3 utils/templateFileCreator.py -n "36. Valid Sudoku"
```

<!-- SCRIPT ENDS -->
