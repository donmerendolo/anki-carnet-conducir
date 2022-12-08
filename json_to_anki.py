import json
from pynput.mouse import Button, Controller
import pyperclip
from time import sleep

# Read the data from the JSON file
with open('data.json') as json_file:
    data = json.load(json_file)


# Create a mouse controller
mouse = Controller()
def paste(value, coordinates):
    mouse.position = coordinates
    mouse.click(Button.left)
    pyperclip.copy(value)
    mouse.click(Button.right)
    sleep(0.2)
    
    if coordinates == [1220, 60]:
        mouse.position = [coordinates[0]+50, coordinates[1]+80]
    else:
        mouse.position = [coordinates[0]+50, coordinates[1]+60]
    mouse.click(Button.left)
    sleep(0.2)
    
for dict in data[2600:]:
    paste(dict["explicacion"], [550, 740])
    paste(dict["correcta"], [550, 670])
    paste(dict["c."], [550, 600])
    paste(dict["b."], [550, 520])
    paste(dict["a."], [550, 450])
    paste("2", [550, 380])
    paste(dict["pregunta"], [550, 300])
    
    paste(dict["img"][2:], [1220, 60])
    sleep(0.4)
    
    mouse.position = [1000, 110]
    mouse.press(Button.left)
    sleep(0.2)
    mouse.position = [550, 220]
    sleep(0.2)
    mouse.release(Button.left)
    sleep(0.2)
    
    mouse.position = [650, 1017]
    mouse.click(Button.left)
    print(data.index(dict))
    sleep(0.2)
