# Print the upper bar
layout_1 = "{0:>9}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"
print(layout_1.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

# Print the dashed lines
layout_2 = "{0:>53}"
print(layout_2.format(":--------------------------------------------------"))

# Print the full table
layout_3 = "{0:>2}{1}{2:>6}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}{13:>4}"
for i in range(1, 13):
    print(layout_3.format(i, ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12, i*13))
