import os
import sys
import platform
from enum import Enum

_ports_used = []

_ports_used = []

class Port:
    def __init__(self, num):
        self.num = num
        if self.num in _ports_used:
            raise TypeError("num already used")
        _ports_used.append(self.num)

    def is_used(self):
        if self.num in _ports_used:
            return True
        else:
            return False

    def is_not_used(self):
        return not self.is_used()

def create_port(num):
    return Port(num)

class PORTS(Enum):
    port_0 = create_port(0)
    port_1 = create_port(1)
    port_2 = create_port(2)
    port_3 = create_port(3)
    port_4 = create_port(4)
    port_5 = create_port(5)
    port_6 = create_port(6)
    port_7 = create_port(7)
    port_8 = create_port(8)
    port_9 = create_port(9)
    port_10 = create_port(10)
    port_11 = create_port(11)
    port_12 = create_port(12)
    port_13 = create_port(13)
    port_14 = create_port(14)
    port_15 = create_port(15)
    port_16 = create_port(16)
    port_17 = create_port(17)
    port_18 = create_port(18)
    port_19 = create_port(19)
    port_20 = create_port(20)
    port_21 = create_port(21)
    port_22 = create_port(22)
    port_23 = create_port(23)
    port_24 = create_port(24)
    port_25 = create_port(25)
    port_26 = create_port(26)
    port_27 = create_port(27)
    port_28 = create_port(28)
    port_29 = create_port(29)
    port_30 = create_port(30)
    port_31 = create_port(31)
    port_32 = create_port(32)
    port_33 = create_port(33)
    port_34 = create_port(34)
    port_35 = create_port(35)
    port_36 = create_port(36)
    port_37 = create_port(37)
    port_38 = create_port(38)
    port_39 = create_port(39)
    port_40 = create_port(40)
    port_41 = create_port(41)
    port_42 = create_port(42)
    port_43 = create_port(43)
    port_44 = create_port(44)
    port_45 = create_port(45)
    port_46 = create_port(46)
    port_47 = create_port(47)
    port_48 = create_port(48)
    port_49 = create_port(49)
    port_50 = create_port(50)
    port_51 = create_port(51)
    port_52 = create_port(52)
    port_53 = create_port(53)
    port_54 = create_port(54)
    port_55 = create_port(55)
    port_56 = create_port(56)
    port_57 = create_port(57)
    port_58 = create_port(58)
    port_59 = create_port(59)
    port_60 = create_port(60)
    port_61 = create_port(61)
    port_62 = create_port(62)
    port_63 = create_port(63)
    port_64 = create_port(64)
    port_65 = create_port(65)
    port_66 = create_port(66)
    port_67 = create_port(67)
    port_68 = create_port(68)
    port_69 = create_port(69)
    port_70 = create_port(70)
    port_71 = create_port(71)
    port_72 = create_port(72)
    port_73 = create_port(73)
    port_74 = create_port(74)
    port_75 = create_port(75)
    port_76 = create_port(76)
    port_77 = create_port(77)
    port_78 = create_port(78)
    port_79 = create_port(79)
    port_80 = create_port(80)
    port_81 = create_port(81)
    port_82 = create_port(82)
    port_83 = create_port(83)
    port_84 = create_port(84)
    port_85 = create_port(85)
    port_86 = create_port(86)
    port_87 = create_port(87)
    port_88 = create_port(88)
    port_89 = create_port(89)
    port_90 = create_port(90)
    port_91 = create_port(91)
    port_92 = create_port(92)
    port_93 = create_port(93)
    port_94 = create_port(94)
    port_95 = create_port(95)
    port_96 = create_port(96)
    port_97 = create_port(97)
    port_98 = create_port(98)
    port_99 = create_port(99)
    port_100 = create_port(100)

class Terminal:
    def __init__(self, port = PORTS.port_0):
        self.port = port

    def print(self, value):
        print(value)

    def clear(self):
        os.system("clear")
    
    def input(self, value):
        return input(value)
    
    def close(self):
        try:
            system_name = platform.system()

            if system_name == "Windows":
                os.system("taskkill /F /PID " + str(os.getppid()))

            elif system_name in ("Linux", "Darwin"):
                os.kill(os.getppid(), 9)

            else:
                print(f"Unsupported OS: {system_name}")
                sys.exit(1)

        except Exception as e:
            print(f"Error closing terminal: {e}")
            sys.exit(1)

    def exit(self, exit_code = None):
        sys.exit(exit_code)

print(PORTS.port_0.num)