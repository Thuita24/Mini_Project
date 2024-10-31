import cairo
import math

# Set up image surface
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Create the wooden lane background with a wood grain effect
for i in range(15):
    # Alternate between light and medium brown for wood plank effect
    if i % 2 == 0:
        context.set_source_rgb(0.85, 0.7, 0.5)  # Lighter wood
    else:
        context.set_source_rgb(0.75, 0.6, 0.4)  # Darker wood

    # Draw vertical stripes to simulate planks
    context.rectangle(i * (width // 15), 0, width // 15, height)
    context.fill()

# Add a shadow gradient near the pins to add depth
shadow_gradient = cairo.LinearGradient(0, height // 4, 0, height // 2)
shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0)  # Transparent
shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0.4)  # Darker shadow
context.set_source(shadow_gradient)
context.rectangle(0, 0, width, height // 2)
context.fill()

# Define bowling ball properties and place it near the bottom
center_x, center_y = width // 2, height - 80
radius = 50

# Create a radial gradient for the 3D effect on the bowling ball
gradient = cairo.RadialGradient(center_x - radius / 3, center_y - radius / 3, radius / 4, center_x, center_y, radius)
gradient.add_color_stop_rgb(0, 0.7, 0.2, 0.2)  # Highlight color (light red)
gradient.add_color_stop_rgb(0.3, 0.5, 0, 0)  # Middle darker red
gradient.add_color_stop_rgb(1, 0.3, 0, 0)  # Dark edge red

# Draw the bowling ball
context.set_source(gradient)
context.arc(center_x, center_y, radius, 0, 2 * math.pi)
context.fill()

# Define positions for the finger holes
hole_radius = 8
holes = [
    (center_x - 15, center_y - 20),  # Top-left hole
    (center_x + 5, center_y - 25),  # Top-right hole
    (center_x - 5, center_y)  # Bottom hole
]

# Draw the finger holes with a shadow effect for depth
for (x, y) in holes:
    hole_gradient = cairo.RadialGradient(x, y, hole_radius / 4, x, y, hole_radius)
    hole_gradient.add_color_stop_rgb(0, 0.1, 0.1, 0.1)  # Darker center
    hole_gradient.add_color_stop_rgb(1, 0.3, 0.3, 0.3)  # Lighter edge

    context.set_source(hole_gradient)
    context.arc(x, y, hole_radius, 0, 2 * math.pi)
    context.fill()

# Draw pins in a triangular formation at the top of the lane
pin_positions = [
    (width // 2 - 40, 80), (width // 2, 80), (width // 2 + 40, 80),
    (width // 2 - 20, 120), (width // 2 + 20, 120),
    (width // 2, 160)
]

# Draw each pin with red stripes for detail
for (px, py) in pin_positions:
    # Draw the pin body (rectangle with rounded top)
    context.set_source_rgb(0.95, 0.95, 0.95)  # Light gray color for the pin
    context.rectangle(px - 7, py + 5, 14, 35)  # Slightly wider and taller pin body
    context.fill()

    # Draw the top of the pin (circle)
    context.arc(px, py + 5, 10, 0, 2 * math.pi)
    context.fill()

    # Add red stripes on the pin for realism
    context.set_source_rgb(1, 0, 0)  # Red color for stripes
    context.rectangle(px - 7, py + 20, 14, 4)  # First stripe
    context.fill()
    context.rectangle(px - 7, py + 26, 14, 4)  # Second stripe
    context.fill()

# Save the image
surface.write_to_png("Output/BowlingAlleyWithBall.png")
