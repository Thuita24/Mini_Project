import cairo
import math

# Set up image surface
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Define the 8-ball properties
center_x, center_y = width // 2, height // 2
radius = 100

# Create a radial gradient for the 3D effect in black
gradient = cairo.RadialGradient(center_x - radius / 3, center_y - radius / 3, radius / 4, center_x, center_y, radius)
gradient.add_color_stop_rgb(0, 0.3, 0.3, 0.3)    # Highlight color (dark gray)
gradient.add_color_stop_rgb(0.3, 0.1, 0.1, 0.1)  # Middle gray
gradient.add_color_stop_rgb(1, 0, 0, 0)          # Dark edge black

# Draw the 8-ball with the gradient
context.set_source(gradient)
context.arc(center_x, center_y, radius, 0, 2 * math.pi)
context.fill()

# Draw the white circle for the "8"
white_circle_radius = 30
context.set_source_rgb(1, 1, 1)  # White color for the circle
context.arc(center_x, center_y - 20, white_circle_radius, 0, 2 * math.pi)
context.fill()

# Draw the number "8" in the white circle
context.set_source_rgb(0, 0, 0)  # Black color for the number
context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
context.set_font_size(30)

# Calculate text positioning to center the "8"
text = "8"
(x_bearing, y_bearing, text_width, text_height, _, _) = context.text_extents(text)
text_x = center_x - text_width / 2
text_y = center_y - 20 + text_height / 2

# Draw the "8"
context.move_to(text_x, text_y)
context.show_text(text)

# Save the image
surface.write_to_png("Output/8_ball.png")
