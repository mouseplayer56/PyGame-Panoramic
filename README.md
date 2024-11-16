# PyGame-Panoramic
Allows a Panoramic view (using PyGame for the GUI, and some maths). Will retain objects placed on certain panoramic panels independent of where they are viewed.
![east-south](https://github.com/user-attachments/assets/d2c062a6-a6b5-4bc2-ad4b-59965d928be2)
![north](https://github.com/user-attachments/assets/80c7fbe1-2708-4137-ae97-22cb6e40d89f)

If the print spam gets annoying, remove this line:
```
print(f"{r}, {panorama_x}, {panorama_x_local} -- {panorama_list_extra}")
```

And here are some values you can adjust in the code:
```
fps = 60
```
```
width, height = 1280, 720
```
```
lookspeed = 3000
```

And the code to adjust if you want to move the stickman:
```
(panora_part[1] + 500, 50))
```
