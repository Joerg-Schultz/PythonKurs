class Robot:

    def __init__(self, name):
        # The properties of each robot
        self.name = name
        self.left_arm_raised = False
        self.right_arm_raised = False
        self.internal_position = (0, 0)  # x,y coordinates of the robots position list of two values

    # print the status of an instance of the Robot class
    def __str__(self):
        return f"Name: {self.name}\n\tLeft arm is up: {self.left_arm_raised}\n\tI am at position {self.position()}"

    def position(self):
        return self.internal_position

    # in OO speech functions are called methods
    def move_left(self):
        self.internal_position = (self.internal_position[0] - 1, self.internal_position[1])

    def move_right(self):
        self.internal_position = (self.internal_position[0] + 1, self.internal_position[1])

    def move_up(self):
        self.internal_position = (self.internal_position[0], self.internal_position[1] + 1)

    def move_down(self):
        self.internal_position = (self.internal_position[0], self.internal_position[1] - 1)

    def change_left_arm_position(self):
        self.left_arm_raised = not self.left_arm_raised

    def change_right_arm_position(self):
        self.right_arm_raised = not self.right_arm_raised


class RobotWithLight(Robot):

    def __init__(self, name):
        super().__init__(name)
        self.light = False

    def __str__(self):
        return super(RobotWithLight, self).__str__() + f"\n\tLight Status: {self.light}"

    def switch_light(self):
        self.light = not self.light

    def move_left(self):
        super().move_left()
        super().move_left()

