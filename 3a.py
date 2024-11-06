def minimax(depth, nodeIndex, maximizingPlayer, values):
    # Base case: return the value if at leaf node
    if depth == 0:
        return values[nodeIndex]

    if maximizingPlayer:
        bestValue = -float('inf')
        for i in range(2):  # Assuming each node has 2 children
            value = minimax(depth - 1, nodeIndex * 2 + i, False, values)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float('inf')
        for i in range(2):  # Assuming each node has 2 children
            value = minimax(depth - 1, nodeIndex * 2 + i, True, values)
            bestValue = min(bestValue, value)
        return bestValue


# Example usage
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Possible outcomes
optimal_value = minimax(3, 0, True, values)  # Start at depth 3
print(f"The optimal value for the current player is: {optimal_value}")
