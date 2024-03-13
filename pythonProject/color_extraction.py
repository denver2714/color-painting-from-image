import colorgram

rgb_colors = []

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)

print(rgb_colors)

#After printing the values, take it and put it in a new array