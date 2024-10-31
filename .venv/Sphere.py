import cairo
import math

# Set up image surface
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Define the bowling ball properties
center_x, center_y = width // 2, height // 2
radius = 100

# Create a radial gradient for the 3D effect in blue
gradient = cairo.RadialGradient(center_x - radius / 3, center_y - radius / 3, radius / 4, center_x, center_y, radius)
gradient.add_color_stop_rgb(0, 0.7, 0.8, 1)    # Highlight color (light blue)
gradient.add_color_stop_rgb(0.3, 0.2, 0.3, 0.7) # Middle blue
gradient.add_color_stop_rgb(1, 0.1, 0.2, 0.4)  # Dark edge blue

# Draw the bowling ball with the gradient
context.set_source(gradient)
context.arc(center_x, center_y, radius, 0, 2 * math.pi)
context.fill()

# Define the positions for the finger holes
hole_radius = 10
holes = [
    (center_x - 20, center_y - 30),  # Top-left hole
    (center_x + 10, center_y - 35),  # Top-right hole
    (center_x - 5, center_y - 5)     # Bottom hole
]

# Draw the finger holes with shading for depth
for (x, y) in holes:
    hole_gradient = cairo.RadialGradient(x, y, hole_radius / 4, x, y, hole_radius)
    hole_gradient.add_color_stop_rgb(0, 0.1, 0.1, 0.1)  # Darker center
    hole_gradient.add_color_stop_rgb(1, 0.3, 0.3, 0.3)  # Lighter edge

    context.set_source(hole_gradient)
    context.arc(x, y, hole_radius, 0, 2 * math.pi)
    context.fill()

# Save the image
surface.write_to_png("Output/Sphere.png")
