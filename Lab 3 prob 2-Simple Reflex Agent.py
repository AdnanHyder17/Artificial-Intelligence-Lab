# Consider a scenario, cameras placed on every side of the car — front, rear, left and right —
# to stitch together a 360-degree view of the environment. For a three-lane road a car is
# moving on a middle lane, consider the below scenario
# • If the front camera detects the object within range of 8 meters breaks are applied automatically.
# • If the left camera detects the object within range of 2 meters car moves to the right lane.
# • If the right camera detects the object within range of 2 meters car moves to the left lane.
# • For parking the car if the rear camera detects the object within 5 cm breaks are applied.

import random
def detectObject(camera_position, object_distance):
    if camera_position == "front" and object_distance <= 8:
        return "apply_brakes"
    elif camera_position == "left" and object_distance <= 2:
        return "move_right"
    elif camera_position == "right" and object_distance <= 2:
        return "move_left"
    elif camera_position == "rear" and object_distance <= 0.05:
        return "apply_brakes_park"
    else:
        return "no_action"

front_camera_distance = random.uniform(0,10)
left_camera_distance = random.uniform(0,10)
right_camera_distance = random.uniform(0,10)
rear_camera_distance = random.uniform(0,10)

print("Front Camera Distance: ",front_camera_distance)
print("Left Camera Distance: ",left_camera_distance)
print("Right Camera Distance: ",right_camera_distance)
print("Rear Camera Distance: ",rear_camera_distance,"\n")

front_action = detectObject("front", front_camera_distance)
left_action = detectObject("left", left_camera_distance)
right_action = detectObject("right", right_camera_distance)
rear_action = detectObject("rear", rear_camera_distance)

print("Action taken by front camera:", front_action)
print("Action taken by left camera:", left_action)
print("Action taken by right camera:", right_action)
print("Action taken by rear camera:", rear_action)
