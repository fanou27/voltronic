from wksSendCommand import wksProtocol
from inverter import Inverter

class wksGetStatus:
    def __init__(self, portName):
        self.__portName = portName
        self.__inverter = Inverter()

        command = "QPIRI"
        wks = wksProtocol(self.__portName, command)
        wks.send()
        if wks.isFrameOk():
            fields = wks.getFields()
            self.__inverter.setBatteryType(int(fields[12]))
            self.__inverter.setOutputSourcePriority(int(fields[16]))
            self.__inverter.setChargerSourcePriority(int(fields[17]))

        command = "QPIGS"
        wks = wksProtocol(self.__portName, command)
        wks.send()
        if wks.isFrameOk():
            fields = wks.getFields()
            self.__inverter.setConso(int(fields[4]))
            self.__inverter.setBatteryVoltage(float(fields[8]))
            self.__inverter.setBatteryChargingCurrent(float(fields[9]))
            self.__inverter.setBatteryCapacity(int(fields[10]))
            self.__inverter.setPVCurrent(float(fields[12]))
            self.__inverter.setPVVoltage(float(fields[13]))
            self.__inverter.setBatteryDischargingCurrent(int(fields[15]))
            self.__inverter.setPVPower(int(fields[19]))

        command = "QMOD"
        wks = wksProtocol(self.__portName, command)
        wks.send()
        if wks.isFrameOk():
            fields = wks.getFields()
            self.__inverter.setMode(fields[0])

    def toJson(self):
        return self.__inverter.toJson()


class wksGetWarning:
    def __init__(self, portName):
        self.__portName = portName
        self.__warnings = []

        command = "QPIWS"

        wks = wksProtocol(self.__portName, command)
        wks.send()
        if wks.isFrameOk():
            fields = wks.getFields()
            size = len(fields)
            frameOK =wks.isFrameOk()
            ack = wks.isAck()
            nack = wks.isNack()
            if ( size == 1 and frameOK and not ack and not nack):
                warnings = ["PV Loss","Inverter fault","Bus over fault","Bus under fault","Bus soft fail fault","Line fail warning","OPV short warning","Inverter voltage too low fault","Inverter voltage too high fault","Over temperature fault","Fan locked fault","Battery voltage to high fault","Battery low alarm warning","RESERVED","Battery under shutdown warning","RESERVED","Overload fault","EEPROM fault","Inverter over current fault","Inverter soft fail fault","Self test fail fault","OP DC voltage over fault","Bat open fault","Current sensor fail fault","Battery short fault","Power limit warning","PV voltage high warning","MPPT overload fault","MPPT overload warning","Battery too low to charge warning","RESERVED","RESERVED"]

                pos = 0;
                #print(len(fields[0]))
                for warn in fields[0]:
                    if (warn == '1'):
                        #print(pos)
                        self.__warnings.append(warnings[pos])
                    pos += 1

    def toJson(self):
         st = "{\"warnings\": "
         st += str(self.__warnings)
         st += "}"
         return str(self.__warnings)



    # QET: Query total PV generated energy  QEYyyyy: Query PV generated energy of year QEMyyyymm: Query PV generated energy of month  unit: Wh
    # QLT: Query total Load energy  QLYyyyy: Query Load energy of year QLMyyyymm: Query Load energy of month  unit: Wh
    # QT : Time inquiry YYYYMMDDHHMMSS
    # DAT< YYMMDDHHMMSS><cr>: Date and time
    # Command = QBMS  ==> (0 079 0 0 0 532 532 450 0110 0110sð
    # PCP02 (HS only: set solar and utility), PCP03 (set solar only charging)
    # POP01 (Line Mode SUB), POP02 (Battery Mode SBU)
    # Command = QID : Voltronic => 92832105600008 WKS => 96332205100501