import math

def required_volume_for_points(points):
    if points < 1:
        return 0
    
    # Formula: each doubling adds 1 point starting from $2 = 1 point
    volume = 2 * (2 ** (points - 1))  # Inverse of doubling-based points
    return volume

# User input
points = int(input("Enter the number of points you want: "))
volume = required_volume_for_points(points)

print(f"To get {points} points, you need approximately ${volume}")
