import random


class Robot:
    VIN_Code = "ROB731"
    Memory = 32768
    Processor = "Intel I9-11900KB"


class SpotMini(Robot):
    name = "SpotMini"
    Sub_VIN_Code = name + str(random.random())

    def SpotMini(self):
        system_info = f"My name: {SpotMini.name}, my VIN_Code: {Robot.VIN_Code + SpotMini.Sub_VIN_Code}. I have {Robot.Memory} memory, and have {Robot.Processor}"
        return system_info


class Atlas(Robot):
    name = "Atlas"
    Sub_VIN_Code = name + str(random.random())

    def Atlas(self):
        system_info = f"My name: {Atlas.name}, my VIN_Code: {Robot.VIN_Code + Atlas.Sub_VIN_Code}. I have {Robot.Memory} memory, and have {Robot.Processor}"
        return system_info


class Handle(Robot):
    name = "Handle"
    Sub_VIN_Code = name + str(random.random())

    def Handle(self):
        system_info = f"My name: {Handle.name}, my VIN_Code: {Robot.VIN_Code + Handle.Sub_VIN_Code}. I have {Robot.Memory} memory, and have {Robot.Processor}"
        return system_info


SpMi = SpotMini()
print(SpMi.SpotMini())
At = Atlas()
print(At.Atlas())
Hd = Handle()
print(Hd.Handle())
