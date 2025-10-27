import math

def points_from_volume(volume):
    if volume < 2:
        return 0
    
    # Points formula: 1 point for $2, +1 for each doubling
    points = math.floor(math.log(volume / 2, 2)) + 1
    return max(points, 0)

# User input
volume = float(input("Enter your trading volume in $: "))
points = points_from_volume(volume)

print(f"For a volume of ${volume}, you will get approximately {points} points")
