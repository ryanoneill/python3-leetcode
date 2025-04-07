from find_all_possible_recipes_from_given_supplies import Solution


def test_ex1():
    recipes = ["bread"]
    ingredients = [["yeast", "flour"]]
    supplies = ["yeast", "flour", "corn"]
    solution = Solution()
    results = solution.findAllRecipes(recipes, ingredients, supplies)
    results.sort()
    assert results == ["bread"]


def test_ex2():
    recipes = ["bread", "sandwich"]
    ingredients = [["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]
    solution = Solution()
    results = solution.findAllRecipes(recipes, ingredients, supplies)
    results.sort()
    assert results == ["bread", "sandwich"]


def test_ex3():
    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies = ["yeast", "flour", "meat"]
    solution = Solution()
    results = solution.findAllRecipes(recipes, ingredients, supplies)
    results.sort()
    assert results == ["bread", "burger", "sandwich"]


def test_ex4():
    recipes = [
        "xevvq",
        "izcad",
        "p",
        "we",
        "bxgnm",
        "vpio",
        "i",
        "hjvu",
        "igi",
        "anp",
        "tokfq",
        "z",
        "kwdmb",
        "g",
        "qb",
        "q",
        "b",
        "hthy",
    ]
    ingredients = [
        ["wbjr"],
        ["otr", "fzr", "g"],
        ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
        ["fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i", "anp"],
        ["wi", "xgp", "wbjr"],
        ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"],
        ["xgp", "otr", "wbjr"],
        ["wbjr", "otr"],
        ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
        ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"],
        ["bxgnm"],
        ["wi", "fzr", "otr", "wbjr"],
        ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"],
        ["otr", "fzr", "xgp", "wbjr"],
        ["xgp", "wbjr", "q", "vpio", "tokfq", "we"],
        ["wbjr", "wi", "xgp", "we"],
        ["wbjr"],
        ["wi"],
    ]
    supplies = ["wi", "otr", "wbjr", "fzr", "xgp"]
    solution = Solution()
    results = solution.findAllRecipes(recipes, ingredients, supplies)
    results.sort()
    expected = ["xevvq", "izcad", "bxgnm", "i", "hjvu", "tokfq", "z", "g", "b", "hthy"]
    expected.sort()
    assert results == expected


def test_ex5():
    recipes = ["burger", "bread", "sandwich"]
    ingredients = [["sandwich", "meat", "bread"], ["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]
    solution = Solution()
    results = solution.findAllRecipes(recipes, ingredients, supplies)
    results.sort()
    assert results == ["bread", "burger", "sandwich"]
