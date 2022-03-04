import Robots

# # Generate my robots
# robots = [Robots.Robot(name) for name in ("Willi", "Maja", "Flip")]
# robots.append(Robots.RobotWithLight("Carl"))
#
# # Move them
# for robot in robots:
#     robot.move_left()
#
# #[robot.move_left() for robot in robots]
# # Print their status
# for robot in robots:
#     print(robot)
#[print(robot) for robot in robots]

robot1 = Robots.Robot("Will")
print(robot1)
robot2 = Robots.Robot("Jean_Luc")
print(robot2)
robot3 = Robots.Robot("Will")
print(robot3)