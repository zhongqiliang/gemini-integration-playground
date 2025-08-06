import math

def calculate_circle_area(radius):
  """
  Calculates the area of a circle given its radius.
  """
  if radius < 0:
    return "Error: Radius cannot be negative."
  
  # The formula for the area of a circle is A = π * r^2
  area = math.pi * (radius ** 2)
  return area

# Set a radius value
circle_radius = 5

# Call the function and store the result
result_area = calculate_circle_area(circle_radius)

# Print the result to the console
print(f"The area of a circle with radius {circle_radius} is: {result_area:.2f}")

