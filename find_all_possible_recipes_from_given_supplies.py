from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        haves = set(supplies)
        indices = {recipe: index for index, recipe in enumerate(recipes)}
        dependencies = defaultdict(list)
        indegrees = [0] * len(recipes)

        for index, needs in enumerate(ingredients):
            for item in needs:
                if item not in haves:
                    dependencies[item].append(recipes[index])
                    indegrees[index] += 1

        results = []
        queue = deque(index for index, count in enumerate(indegrees) if count == 0)
        while queue:
            index = queue.popleft()
            recipe = recipes[index]
            results.append(recipe)

            for dependency in dependencies[recipe]:
                dep_index = indices[dependency]
                indegrees[dep_index] -= 1
                if indegrees[dep_index] == 0:
                    queue.append(dep_index)

        return results
