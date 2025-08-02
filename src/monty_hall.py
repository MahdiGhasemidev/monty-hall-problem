import random

def monty_hall_game(switch_choice: bool) -> bool :
    """_summary_

    Args:
        switch_choice (bool): _description_

    Returns:
        bool: _description_
    """
    
    doors = ['goat'] * 2 + ['car']
    random.shuffle(doors)
    selected_door = random.choice(range(3))
    
    doors_revealed = [i for i in range(3) if i != selected_door and doors[i] == 'goat' ]
    door_revealed = random.choice(doors_revealed)
    
    if switch_choice : 
        final_choice = [i for i in range(3) if i != selected_door and  i != door_revealed][0]
    else:
        final_choice = selected_door
    
    return doors[final_choice] == 'car'

def simulate_games(num_games: int = 1000) :
    """_summary_

    Args:
        num_games (int, optional): _description_. Defaults to 1000.

    Returns:
        _type_: _description_
    """
    num_wins_without_switching = sum(monty_hall_game(switch_choice = False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall_game(switch_choice = True) for _ in range(num_games))

    return num_wins_without_switching, num_wins_with_switching


if __name__ == '__main__':
    num_games = 1000000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(f"Winning percentage without switching doors: {(num_wins_without_switching/num_games):.2%}")
    print(f"Winning percentage with    switching doors: {(num_wins_with_switching/num_games):.2%}")

