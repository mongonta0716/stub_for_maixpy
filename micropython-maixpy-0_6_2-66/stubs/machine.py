"""
Module: 'machine' on micropython-maixpy-0.6.2-66
"""
# MCU: {'ver': '0.6.2-66', 'build': '66', 'sysname': 'MaixPy', 'platform': 'MaixPy', 'version': '0.6.2', 'release': '0.6.2', 'port': 'MaixPy', 'family': 'micropython', 'name': 'micropython', 'machine': 'Sipeed_M1 with kendryte-k210', 'nodename': 'MaixPy'}
# Stubber: 1.3.9
HARD_RESET = 0

class I2C:
    ''
    I2C0 = 0
    I2C1 = 1
    I2C2 = 2
    I2C3 = 3
    I2C4 = 4
    I2C5 = 5
    I2C_EV_RESTART = 1
    I2C_EV_START = 0
    I2C_EV_STOP = 2
    I2C_SOFT = 6
    MODE_MASTER = 0
    MODE_MASTER_SOFT = 2
    MODE_SLAVE = 1
    def deinit():
        pass

    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def scan():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass


class PWM:
    ''
    def deinit():
        pass

    def disable():
        pass

    def duty():
        pass

    def enable():
        pass

    def freq():
        pass

    def init():
        pass

PWRON_RESET = 0

class SDCard:
    ''
    def ioctl():
        pass

    def remount():
        pass

SOFT_RESET = 1

class SPI:
    ''
    CS0 = 0
    CS1 = 1
    CS2 = 2
    CS3 = 3
    LSB = 1
    MODE_MASTER = 0
    MODE_MASTER_2 = 1
    MODE_MASTER_4 = 2
    MODE_MASTER_8 = 3
    MODE_SLAVE = 4
    MSB = 0
    SPI0 = 0
    SPI1 = 1
    SPI2 = 2
    SPI_SOFT = 4
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Timer:
    ''
    CHANNEL0 = 0
    CHANNEL1 = 1
    CHANNEL2 = 2
    CHANNEL3 = 3
    MODE_ONE_SHOT = 0
    MODE_PERIODIC = 1
    MODE_PWM = 2
    TIMER0 = 0
    TIMER1 = 1
    TIMER2 = 2
    UNIT_MS = 2
    UNIT_NS = 0
    UNIT_S = 3
    UNIT_US = 1
    def callback():
        pass

    def callback_arg():
        pass

    def deinit():
        pass

    def init():
        pass

    def period():
        pass

    def restart():
        pass

    def start():
        pass

    def stop():
        pass


class UART:
    ''
    PARITY_EVEN = 2
    PARITY_ODD = 1
    UART1 = 0
    UART2 = 1
    UART3 = 2
    UARTHS = 4
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readchar():
        pass

    def readinto():
        pass

    def readline():
        pass

    def repl_uart():
        pass

    def set_repl_uart():
        pass

    def write():
        pass


class WDT:
    ''
    WDT_DEVICE_0 = 0
    WDT_DEVICE_1 = 1
    def context():
        pass

    def feed():
        pass

    def stop():
        pass

WDT1_RESET = 3
WDT_RESET = 2
def reset():
    pass

def reset_cause():
    pass

def unique_id():
    pass

