# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
#
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
#
# Return a list of all the recipes that you can create. You may return the answer in any order.
#
# Note that two recipes may contain each other in their ingredients.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)

        recipe_to_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}

        visited = {}
        result = []

        def can_make(recipe):
            if recipe in visited and visited[recipe] == 0:
                return False

            if recipe in visited and visited[recipe] == 1:
                return True

            if recipe in available_supplies:
                return True

            if recipe not in recipe_to_ingredients:
                return False

            visited[recipe] = 0

            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make(ingredient):
                    visited[recipe] = -1
                    return False

            visited[recipe] = 1
            result.append(recipe)
            return True

        for recipe in recipes:
            can_make(recipe)

        return [recipe for recipe in recipes if recipe in visited and visited[recipe] == 1]
