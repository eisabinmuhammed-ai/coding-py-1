import math

# 1. Define your angle in degrees
angle_degrees = 45

# 2. Convert degrees to radians (math functions require radians)
angle_radians = math.radians(angle_degrees)

# 3. Calculate Sin, Cos, and Tan
sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

# 4. Display the results
print(f"Angle: {angle_degrees}° ({angle_radians:.4f} radians)")
print(f"Sine:    {sine_val:.4f}")
print(f"Cosine:  {cosine_val:.4f}")
print(f"Tangent: {tangent_val:.4f}")