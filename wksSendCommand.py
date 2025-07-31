import time

import crc16
import serial
import shlex

from serial.serialutil import SerialException


class wksProtocol:
    def __init__(self, portName, command):
        self.__portName = portName
        self.__command = command
        self.__open()
        self.__frameOK = True
        self.__ACK = False
        self.__NACK = False

    def isAck(self):
        return self.__ACK

    def isNack(self):
        return self.__NACK
    def __checkFrame(self, frame):
        size = len(frame)
        startCh = frame[0]
        lastCh = frame[size - 1]
        crc = frame[size - 3: size - 1]
        #crc= crc.encode()
        data = frame[1:size - 3]
        cmd = frame[0:size - 3]
        crcComputed = crc16.crc16xmodem(cmd.encode()).to_bytes(2, 'big')
        # check
        if (startCh != '(' or lastCh != '\r'): # or crc != crcComputed) :
            self.__frameOK = False
            return []
        fields = shlex.split(data)
        if (len(fields) == 0):
            self.__ACK = (fields[0] == "ACK")
            self.__NACK = (fields[0] == "NACK")

        return fields

    def __open(self):
        try:
            self.__port = serial.Serial(self.__portName, 2400)
            self.__port.close()
            self.__port.open()
        except SerialException as error:
            print("serial port in use wait 2s and retry")
            time.sleep(2)
            try:
                self.__port = serial.Serial(self.__portName, 2400)
                self.__port.close()
                self.__port.open()
            except SerialException as error:
                print("serial fail", error)
                exit()

    def __getResult(self):
        res = ""
        i = 0
        while '\r' not in res:  # and i < 20
            try:
                # time.sleep(1)
                nb = self.__port.in_waiting
                res += "".join([chr(i) for i in self.__port.read(nb) if i != 0x00])
            except Exception as e:
                if e.errno == 110:
                    pass
                else:
                    raise
            i += 1
        return res

    def __getCommand(self):
        cmd = self.__command.encode('utf-8')
        crc = crc16.crc16xmodem(cmd).to_bytes(2, 'big')
        cmd = cmd + crc
        cmd = cmd + b'\r'
        return cmd

    def send(self):
        self.__port.write(self.__getCommand())
        self.__fields = self.__checkFrame(self.__getResult())
        self.__port.close()

    def isFrameOk(self):
        return self.__frameOK

    def getCommand(self):
        return self.__command

    def getFields(self):
        return self.__fields