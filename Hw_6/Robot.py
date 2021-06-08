import random
import sys


class Robot:
    VIN_CODE = "ROB731"
    MEMORY = 32768
    PROCESSOR = "Intel I9-11900KB"

    def __init__(self, work_status=0):
        self.work_status = work_status


class SpotMini(Robot):
    NAME = "SpotMini"
    SUB_VIN_CODE = NAME + str(random.random())

    def __init__(self, work_status, speed):
        super().__init__(work_status)
        self.speed = speed

    def run_speed(self):
        if self.speed > 5.76:
            return "I can't move at a speed higher than 5.76 km/h"
        elif self.speed < 0:
            return "I can't have negative speed"
        elif self.speed == 0:
            return "Robot stop"
        else:
            return f"My speed is {self.speed} km/h"

    def Spot_Mini(self):
        if self.work_status >= 1:
            system_info = f"My name: {SpotMini.NAME}, my VIN_Code: {Robot.VIN_CODE + SpotMini.SUB_VIN_CODE}. " \
                          f"I have {Robot.MEMORY} memory, and have {Robot.PROCESSOR}"
            speed = self.run_speed()
            return system_info + "\n" + speed
        else:
            return "Robot off"


class Atlas(Robot):
    NAME = "Atlas"
    SUB_VIN_CODE = NAME + str(random.random())

    def __init__(self, work_status, jump_height):
        super().__init__(work_status)
        self.jump_height = jump_height

    def jump(self):
        if self.jump_height <= 2:
            return f"Jump height = {self.jump_height}"
        elif self.jump_height <= 0:
            return "I can't perform this action"
        else:
            return "I cannot jump more than two meters"

    def Atlas(self):
        if self.work_status >= 1:
            system_info = f"My name: {Atlas.NAME}, my VIN_Code: {Robot.VIN_CODE + Atlas.SUB_VIN_CODE}. " \
                          f"I have {Robot.MEMORY} memory, and have {Robot.PROCESSOR} "
            jump_status = self.jump()
            return system_info + "\n" + jump_status
        else:
            return "Robot off"


class Handle(Robot):
    NAME = "Handle"
    SUB_VIN_CODE = NAME + str(random.random())

    def __init__(self, work_status, weight_of_the_object_being_lifted):
        super().__init__(work_status)
        self.weight_of_the_object_being_lifted = weight_of_the_object_being_lifted

    def weight(self):
        if self.weight_of_the_object_being_lifted > 15:
            return "I can't lift things more than 15 kilograms"
        elif self.weight_of_the_object_being_lifted <= 0:
            return "I can't lift an object that weighs 0 or less kilograms"
        else:
            return f"Object lifted by weight {self.weight_of_the_object_being_lifted}"

    def Handle(self):
        if self.work_status >= 1:
            system_info = f"My name: {Handle.NAME}, my VIN_Code: {Robot.VIN_CODE + Handle.SUB_VIN_CODE}. " \
                          f"I have {Robot.MEMORY} memory, and have {Robot.PROCESSOR}"
            weight_object = self.weight()
            return system_info + "\n" + weight_object
        else:
            return "Robot off"


SpMi = SpotMini(1, 2)  # Sport Mini(work status, speed)
print(SpMi.Spot_Mini())
At = Atlas(1, 1)  # Atlas(work status, jump height)
print(At.Atlas())
Hd = Handle(1, 15)  # Handle(work status, item weight)
print(Hd.Handle())
