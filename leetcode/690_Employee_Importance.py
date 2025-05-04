"""
Name: Employee Importance (#690)
URL: https://leetcode.com/problems/employee-importance/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def calculate_importance(employee):
            
            imp = employee.importance

            for subordinate_id in employee.subordinates:
                imp += calculate_importance(emp[subordinate_id])

            return imp

        emp = {employee.id: employee for employee in employees}

        return calculate_importance(emp[id])
        