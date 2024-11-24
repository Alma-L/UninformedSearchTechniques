def is_valid(schedule, week, group, player, player_pairs):
    """
    Check if adding a player to a group in a given week is valid.
    """
    # Ensure no duplicate players in the same group
    if player in schedule[week][group]:
        return False

    # Ensure player pairs do not repeat across weeks
    for teammate in schedule[week][group]:
        if (player, teammate) in player_pairs or (teammate, player) in player_pairs:
            return False

    return True

def solve_sgp(players, groups, players_per_group, weeks, max_depth ):
    """
    Solve the Social Golfers Problem using DFS and Backtracking.
    """
    schedule = [[[] for _ in range(groups)] for _ in range(weeks)]
    player_pairs = set()  # Track all player pairs to prevent repeats

    def backtrack(week, group, player_index,depth):
        if depth > max_depth:
            return False

        # Base case: all weeks scheduled
        if week == weeks:
            return True

        # Move to the next week if all groups are scheduled
        if group == groups:
            return backtrack(week + 1, 0, 0,depth)

        # If the current group is full, move to the next group
        if len(schedule[week][group]) == players_per_group:
            return backtrack(week, group + 1, 0,depth)

        # Try adding players to the current group
        for player in range(player_index, players):
            if is_valid(schedule, week, group, player, player_pairs):
                # Add the player to the group
                schedule[week][group].append(player)
                # Add player pairs to the tracking set
                for teammate in schedule[week][group]:
                    if teammate != player:
                        player_pairs.add((player, teammate))

                # Recur to the next step
                if backtrack(week, group, player + 1,depth+1):
                    return True

                # Backtrack: remove the player and their pairs
                schedule[week][group].remove(player)
                for teammate in schedule[week][group]:
                    if teammate != player:
                        player_pairs.remove((player, teammate))

        # If no valid placement is found, return False
        return False

    # Start the backtracking process
    if backtrack(0, 0, 0,0):
        return schedule
    else:
        return None

# Parameters
players = 32
groups = 8
players_per_group = 4
weeks = 8
max_depth = 300

# Solve the problem
solution = solve_sgp(players, groups, players_per_group, weeks,max_depth)

# Output the result
if solution:
    for week, groups in enumerate(solution):
        print(f"Week {week + 1}:")
        for i, group in enumerate(groups):
            print(f"  Group {i + 1}: {group}")
else:
    print("No solution found.")
