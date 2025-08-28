"""
Name: Find All Possible Recipes from Given Supplies (#2115)
URL: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

Time Complexity: O(N + I) [N : Number of Recipes; I : Number of Ingredients]
Space Complexity: O(N + I) [N : Number of Recipes; I : Number of Ingredients]
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def can_make_recipe(recipe):
            if recipe in visited and visited[recipe] == 1:
                return False

            if recipe in visited and visited[recipe] == 2:
                return True

            if recipe in available_supplies:
                return True

            if recipe not in recipes:
                return False

            visited[recipe] = 1
            
            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make_recipe(ingredient):
                    return False

            visited[recipe] = 2
            result.append(recipe)
            return True

        
        available_supplies = set(supplies)
        recipe_to_ingredients = { recipes[i]: ingredients[i] for i in range( len(recipes) ) }
        visited = {}
        result = []

        for recipe in recipes:
            can_make_recipe(recipe)

        return result