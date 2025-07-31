import json
import jsonpickle
from enum import Enum
import re

class OutputSourcePriority(Enum):
    USB = 0
    SUB = 1
    SBU = 2
class ChargerSourcePriority(Enum):
    SolarFirst = 1
    SolarAndUtility = 2
    OnlySolar = 3
class BatteryType(Enum):
    AGM = 0
    FLOODED = 1
    USER = 2
    PYLON = 3
    UNKNOWN = 4
    WECO = 5
    SOLTARO = 6
class Inverter:
    def toJson(self):
        str = jsonpickle.encode(self, unpicklable=False)
        str = json.dumps(str, indent=4)
        str = jsonpickle.decode(str)
        str = re.sub('_Inverter__', '', str)
        return str

    def setOutputSourcePriority(self, osp):
        self.__outputSourcePriority = OutputSourcePriority(osp).name

    def setMode(self, mode): #"P": "Power on", "S": "Standby", "L": "Line", "B": "Battery", "F": "Fault", "H": "Power saving"
        if (mode == "P"):
            self.__mode = "Power on"
        if (mode == "S"):
            self.__mode = "Standby"
        if (mode == "L"):
            self.__mode = "Line"
        if (mode == "B"):
            self.__mode = "Battery"
        if (mode == "F"):
            self.__mode = "Fault"
        if (mode == "H"):
            self.__mode = "Power saving"

    def getOutputSourcePriority(self):
        return self.__outputSourcePriority

    def setChargerSourcePriority(self, csp):
        self.__chargingSourcePriority = ChargerSourcePriority(csp).name

    def getChargerSourcePriority(self):
        return self.__chargingSourcePriority
    def setConso(self, conso):
        self.__conso = conso

    def setBatteryVoltage(self, batteryVoltage):
        self.__batteryVoltage = batteryVoltage
    def setBatteryChargingCurrent(self, batteryChargingCurrent):
        self.__batteryChargingCurrent = batteryChargingCurrent

    def setBatteryType(self, batteryType):
        self.__batteryType = BatteryType(batteryType).name

    def setBatteryDischargingCurrent(self, batteryDischargingCurrent):
        self.__batteryDischargingCurrent = batteryDischargingCurrent

    def setBatteryCapacity(self, batteryCapacity):
        self.__batteryCapacity = batteryCapacity
    def setPVCurrent(self, PVCurent):
        self.__pVCurent = PVCurent
    def setPVVoltage(self, PVVoltage):
        self.__pVVoltage = PVVoltage
    def setPVPower(self, PVPower):
        self.__pVPower = PVPower
