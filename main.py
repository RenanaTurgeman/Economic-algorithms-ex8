add_budget = 1


def selected_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    """
    Returns the first item that can be purchased based on the provided votes and balances.

    Args:
    : param: votes (list[set[str]]): A list of sets of strings representing the votes for each voter.
    : param: (list[float]): A list of floats representing the balances of each voter.
    : param: (dict[str, float]): A dictionary where keys are the items and values are their respective costs.

    Returns:
    - str or -1: The name of the first item that can be purchased, or -1 if no item can be purchased.

    Examples:
    >>> selected_item([{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}], [1.5, 2.4, 3.3, 4.2, 5.1], {"Park": 9.9, "Trees": 2000, "Lights": 3000})
    'Park'
    >>> selected_item([{"Trees"}, {"Lights"}, {"Park"}], [1.5, 2.4, 3.3], {"Park": 1000, "Trees": 2000, "Lights": 3000})
    -1
    """
    # Iterate over each item and its cost
    for item, item_cost in costs.items():
        # Calculate the total balance for the current item
        total_balance = sum(balances[i] for i in range(len(votes)) if item in votes[i])
        if round(total_balance) >= item_cost:
            return item  # Return the item if it can be purchased
    return -1  # Return -1 if no item can be purchased


def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    """
    Elects the next budget item that can be purchased based on the provided votes, balances, and costs.

    Args:
    : param: votes (list[set[str]]): A list of sets of strings representing the votes for each voter.
    : param: balances (list[float]): A list of floats representing the balances of each voter.
    : param: costs (dict[str, float]): A dictionary where keys are the items and values are their respective costs.

    Returns:
    - None , it prints the result

    Examples:
    >>> elect_next_budget_item([{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}], [1.5, 2.4, 3.3, 4.2, 5.1],
    ... {"Park": 9.9, "Trees": 2000, "Lights": 3000})
    After adding 0 to each citizen, Park is chosen.
    Citizen 1 has 0 remaining balance.
    Citizen 2 has 2.4 remaining balance.
    Citizen 3 has 0 remaining balance.
    Citizen 4 has 4.2 remaining balance.
    Citizen 5 has 0 remaining balance.

    >>> elect_next_budget_item([{"Park"}, {"Park"}, {"Park"}, {"Park"}], [1000, 2000, 3000, 4000], {"Park": 500})
    After adding 0 to each citizen, Park is chosen.
    Citizen 1 has 0 remaining balance.
    Citizen 2 has 0 remaining balance.
    Citizen 3 has 0 remaining balance.
    Citizen 4 has 0 remaining balance.

    >>> elect_next_budget_item([{"Park", "Lights"}, {"Lights"}, {"Park"}], [25, 200, 20], {"Park": 50, "Lights": 100})
    After adding 0 to each citizen, Lights is chosen.
    Citizen 1 has 0 remaining balance.
    Citizen 2 has 0 remaining balance.
    Citizen 3 has 20 remaining balance.

    >>> elect_next_budget_item([{"Park", "Lights"}, {"Lights"}, {"Park"}], [25, 0, 20], {"Park": 50, "Lights": 100})
    After adding 3 to each citizen, Park is chosen.
    Citizen 1 has 0 remaining balance.
    Citizen 2 has 3 remaining balance.
    Citizen 3 has 0 remaining balance.
    """
    item = selected_item(votes, balances, costs)

    money = 0  # for printing the money each citizen get
    while item == -1:
        # If there is still no product that can be bought, Update balances with the additional budget
        balances = [curr_balance + add_budget for curr_balance in balances]
        item = selected_item(votes, balances, costs)
        money += add_budget

    # when we select item:
    # 1) Lower the balance of all supporters of the selected item to 0
    balances = [0 if item in votes[i] else curr_balance for i, curr_balance in enumerate(balances)]
    # 2) print the result
    print(f"After adding {money} to each citizen, {item} is chosen.")
    for i, balance in enumerate(balances):
        print(f"Citizen {i + 1} has {balance} remaining balance.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # 3 items, 5 voters
    votes = [{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}]
    balances = [1.5, 2.4, 3.3, 4.2, 5.1]
    costs = {"Park": 1000, "Trees": 2000, "Lights": 3000}

    # print(selected_item([{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}],
    #                     [1.5, 2.4, 3.3, 4.2, 5.1],
    #                     {"Park": 9.9, "Trees": 2000, "Lights": 3000}))
    # elect_next_budget_item(votes, balances, costs)
    # elect_next_budget_item([{"Park", "Lights"}, {"Lights"}, {"Park"}], [25, 200, 20], {"Park": 50, "Lights": 100})
    # elect_next_budget_item([{"Park", "Lights"}, {"Lights"}, {"Park"}], [25, 0, 20], {"Park": 50, "Lights": 100})
