class Robot:

    def __init__(self, name, x_pos, y_pos):
        self._name = name # This is Python private :D
        self.xPos = x_pos
        self.yPos = y_pos
        self.left_arm_up = False
        self.right_arm_up = False

    def __str__(self):
        left_arm = "up" if self.left_arm_up else "down"
        right_arm = "up" if self.right_arm_up else "down"
        return f"{self._name}: Position({self.xPos}, {self.yPos}), Arms({left_arm}, {right_arm})"

    def move_left_arm(self):
        self.left_arm_up = not self.left_arm_up

    def move_right_arm(self):
        self.right_arm_up = not self.right_arm_up

    def move(self,x_direction, y_direction):
        self.xPos += x_direction
        self.yPos += y_direction


willi = Robot("Willi", 0, 0)
willi.move_left_arm()
print(willi)
maja = Robot("Maja", 1, 1)
print(maja)
maja.move(0,1)
print(maja)
