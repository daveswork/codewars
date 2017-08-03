def balance(left, right):
    total_left = left.count("!")*2 + left.count("?")*3
    total_right = right.count("!")*2 + right.count("?")*3
    if total_left > total_right:
        state = "Left"
    elif total_left < total_right:
        state = "Right"
    else:
        state = "Balance"
    return state