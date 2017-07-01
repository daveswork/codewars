def friend(x):
    friends = []
    for item in x:
        if len(item)==4:
            friends.append(item)
    return friends

print friend(["Ryan", "Kieran", "Jason", "Yous"])