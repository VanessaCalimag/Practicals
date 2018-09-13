HEX_COLORS = {"Pink": "#ff69b4", "Pink1": "#ff6eb4", "Pink2": "#ee6aa7",
              "Pink3": "#cd6090", "Pink4": "#8b3a62", "Red": "#cd5c5c",
              "Red1": "#ff6a6a", "Red2": "#ee6363", "Red3": "#cd5555",
              "Red4": "#8b3a3a"}


color_name = input("Enter a colour name: ")
while color_name != "":
    print("The code for \"{}\" is {}".format(color_name, HEX_COLORS.get(color_name)))
    color_name = input("Enter a colour name: ")