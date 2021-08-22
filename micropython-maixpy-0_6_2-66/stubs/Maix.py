"""
Module: 'Maix' on micropython-maixpy-0.6.2-66
"""
# MCU: {'ver': '0.6.2-66', 'build': '66', 'sysname': 'MaixPy', 'platform': 'MaixPy', 'version': '0.6.2', 'release': '0.6.2', 'port': 'MaixPy', 'family': 'micropython', 'name': 'micropython', 'machine': 'Sipeed_M1 with kendryte-k210', 'nodename': 'MaixPy'}
# Stubber: 1.3.9

class Audio:
    ''
    def finish():
        pass

    def init():
        pass

    def play():
        pass

    def play_process():
        pass

    def record():
        pass

    def record_process():
        pass

    def to_bytes():
        pass

    def volume():
        pass


class FFT:
    ''
    def amplitude():
        pass

    def freq():
        pass

    def run():
        pass


class FPIOA:
    ''
    CLK_I2C1 = 23
    CLK_I2C2 = 203
    CLK_SPI1 = 22
    CLK_SPI2 = 202
    CMOS_D0 = 138
    CMOS_D1 = 139
    CMOS_D2 = 140
    CMOS_D3 = 141
    CMOS_D4 = 142
    CMOS_D5 = 143
    CMOS_D6 = 144
    CMOS_D7 = 145
    CMOS_HREF = 136
    CMOS_PCLK = 137
    CMOS_PWDN = 134
    CMOS_RST = 133
    CMOS_VSYNC = 135
    CMOS_XCLK = 132
    GPIO0 = 56
    GPIO1 = 57
    GPIO2 = 58
    GPIO3 = 59
    GPIO4 = 60
    GPIO5 = 61
    GPIO6 = 62
    GPIO7 = 63
    GPIOHS0 = 24
    GPIOHS1 = 25
    GPIOHS10 = 34
    GPIOHS11 = 35
    GPIOHS12 = 36
    GPIOHS13 = 37
    GPIOHS14 = 38
    GPIOHS15 = 39
    GPIOHS16 = 40
    GPIOHS17 = 41
    GPIOHS18 = 42
    GPIOHS19 = 43
    GPIOHS2 = 26
    GPIOHS20 = 44
    GPIOHS21 = 45
    GPIOHS22 = 46
    GPIOHS23 = 47
    GPIOHS24 = 48
    GPIOHS25 = 49
    GPIOHS26 = 50
    GPIOHS27 = 51
    GPIOHS28 = 52
    GPIOHS29 = 53
    GPIOHS3 = 27
    GPIOHS30 = 54
    GPIOHS31 = 55
    GPIOHS4 = 28
    GPIOHS5 = 29
    GPIOHS6 = 30
    GPIOHS7 = 31
    GPIOHS8 = 32
    GPIOHS9 = 33
    I2C0_SCLK = 126
    I2C0_SDA = 127
    I2C1_SCLK = 128
    I2C1_SDA = 129
    I2C2_SCLK = 130
    I2C2_SDA = 131
    I2S0_IN_D0 = 90
    I2S0_IN_D1 = 91
    I2S0_IN_D2 = 92
    I2S0_IN_D3 = 93
    I2S0_MCLK = 87
    I2S0_OUT_D0 = 94
    I2S0_OUT_D1 = 95
    I2S0_OUT_D2 = 96
    I2S0_OUT_D3 = 97
    I2S0_SCLK = 88
    I2S0_WS = 89
    I2S1_IN_D0 = 101
    I2S1_IN_D1 = 102
    I2S1_IN_D2 = 103
    I2S1_IN_D3 = 104
    I2S1_MCLK = 98
    I2S1_OUT_D0 = 105
    I2S1_OUT_D1 = 106
    I2S1_OUT_D2 = 107
    I2S1_OUT_D3 = 108
    I2S1_SCLK = 99
    I2S1_WS = 100
    I2S2_IN_D0 = 112
    I2S2_IN_D1 = 113
    I2S2_IN_D2 = 114
    I2S2_IN_D3 = 115
    I2S2_MCLK = 109
    I2S2_OUT_D0 = 116
    I2S2_OUT_D1 = 117
    I2S2_OUT_D2 = 118
    I2S2_OUT_D3 = 119
    I2S2_SCLK = 110
    I2S2_WS = 111
    JTAG_TCLK = 0
    JTAG_TDI = 1
    JTAG_TDO = 3
    JTAG_TMS = 2
    RESV0 = 120
    RESV1 = 121
    RESV2 = 122
    RESV3 = 123
    RESV4 = 124
    RESV5 = 125
    RESV6 = 20
    RESV7 = 21
    SCCB_SCLK = 146
    SCCB_SDA = 147
    SPI0_ARB = 16
    SPI0_D0 = 4
    SPI0_D1 = 5
    SPI0_D2 = 6
    SPI0_D3 = 7
    SPI0_D4 = 8
    SPI0_D5 = 9
    SPI0_D6 = 10
    SPI0_D7 = 11
    SPI0_SCLK = 17
    SPI0_SS0 = 12
    SPI0_SS1 = 13
    SPI0_SS2 = 14
    SPI0_SS3 = 15
    SPI1_ARB = 82
    SPI1_D0 = 70
    SPI1_D1 = 71
    SPI1_D2 = 72
    SPI1_D3 = 73
    SPI1_D4 = 74
    SPI1_D5 = 75
    SPI1_D6 = 76
    SPI1_D7 = 77
    SPI1_SCLK = 83
    SPI1_SS0 = 78
    SPI1_SS1 = 79
    SPI1_SS2 = 80
    SPI1_SS3 = 81
    SPI_SLAVE_D0 = 84
    SPI_SLAVE_SCLK = 86
    SPI_SLAVE_SS = 85
    TIMER0_TOGGLE1 = 190
    TIMER0_TOGGLE2 = 191
    TIMER0_TOGGLE3 = 192
    TIMER0_TOGGLE4 = 193
    TIMER1_TOGGLE1 = 194
    TIMER1_TOGGLE2 = 195
    TIMER1_TOGGLE3 = 196
    TIMER1_TOGGLE4 = 197
    TIMER2_TOGGLE1 = 198
    TIMER2_TOGGLE2 = 199
    TIMER2_TOGGLE3 = 200
    TIMER2_TOGGLE4 = 201
    UART1_BAUD = 158
    UART1_CTS = 148
    UART1_DCD = 150
    UART1_DE = 160
    UART1_DSR = 149
    UART1_DTR = 153
    UART1_OUT1 = 156
    UART1_OUT2 = 155
    UART1_RE = 159
    UART1_RI = 151
    UART1_RS485_EN = 161
    UART1_RTS = 154
    UART1_RX = 64
    UART1_SIR_IN = 152
    UART1_SIR_OUT = 157
    UART1_TX = 65
    UART2_BAUD = 172
    UART2_CTS = 162
    UART2_DCD = 164
    UART2_DE = 174
    UART2_DSR = 163
    UART2_DTR = 167
    UART2_OUT1 = 170
    UART2_OUT2 = 169
    UART2_RE = 173
    UART2_RI = 165
    UART2_RS485_EN = 175
    UART2_RTS = 168
    UART2_RX = 66
    UART2_SIR_IN = 166
    UART2_SIR_OUT = 171
    UART2_TX = 67
    UART3_BAUD = 186
    UART3_CTS = 176
    UART3_DCD = 178
    UART3_DE = 188
    UART3_DSR = 177
    UART3_DTR = 181
    UART3_OUT1 = 184
    UART3_OUT2 = 183
    UART3_RE = 187
    UART3_RI = 179
    UART3_RS485_EN = 189
    UART3_RTS = 182
    UART3_RX = 68
    UART3_SIR_IN = 180
    UART3_SIR_OUT = 185
    UART3_TX = 69
    UARTHS_RX = 18
    UARTHS_TX = 19
    def get_Pin_num():
        pass

    def help():
        pass

    def set_function():
        pass


class GPIO:
    ''
    GPIO0 = 32
    GPIO1 = 33
    GPIO2 = 34
    GPIO3 = 35
    GPIO4 = 36
    GPIO5 = 37
    GPIO6 = 38
    GPIO7 = 39
    GPIOHS0 = 0
    GPIOHS1 = 1
    GPIOHS10 = 10
    GPIOHS11 = 11
    GPIOHS12 = 12
    GPIOHS13 = 13
    GPIOHS14 = 14
    GPIOHS15 = 15
    GPIOHS16 = 16
    GPIOHS17 = 17
    GPIOHS18 = 18
    GPIOHS19 = 19
    GPIOHS2 = 2
    GPIOHS20 = 20
    GPIOHS21 = 21
    GPIOHS22 = 22
    GPIOHS23 = 23
    GPIOHS24 = 24
    GPIOHS25 = 25
    GPIOHS26 = 26
    GPIOHS27 = 27
    GPIOHS28 = 28
    GPIOHS29 = 29
    GPIOHS3 = 3
    GPIOHS30 = 30
    GPIOHS31 = 31
    GPIOHS4 = 4
    GPIOHS5 = 5
    GPIOHS6 = 6
    GPIOHS7 = 7
    GPIOHS8 = 8
    GPIOHS9 = 9
    IN = 0
    IRQ_BOTH = 3
    IRQ_FALLING = 1
    IRQ_NONE = 0
    IRQ_RISING = 2
    OUT = 3
    PULL_DOWN = 1
    PULL_NONE = -1
    PULL_UP = 2
    WAKEUP_NOT_SUPPORT = 0
    def disirq():
        pass

    def init():
        pass

    def irq():
        pass

    def mode():
        pass

    def value():
        pass


class I2S:
    ''
    CHANNEL_0 = 0
    CHANNEL_1 = 1
    CHANNEL_2 = 2
    CHANNEL_3 = 3
    DEVICE_0 = 0
    DEVICE_1 = 1
    DEVICE_2 = 2
    IGNORE_WORD_LENGTH = 0
    LEFT_JUSTIFYING_MODE = 4
    RECEIVER = 1
    RESOLUTION_12_BIT = 1
    RESOLUTION_16_BIT = 2
    RESOLUTION_20_BIT = 3
    RESOLUTION_24_BIT = 4
    RESOLUTION_32_BIT = 5
    RIGHT_JUSTIFYING_MODE = 2
    SCLK_CYCLES_16 = 0
    SCLK_CYCLES_24 = 1
    SCLK_CYCLES_32 = 2
    STANDARD_MODE = 1
    TRANSMITTER = 0
    def channel_config():
        pass

    def init():
        pass

    def play():
        pass

    def record():
        pass

    def set_sample_rate():
        pass

    def wait_record():
        pass


class MIC_ARRAY:
    ''
    def deinit():
        pass

    def get_dir():
        pass

    def get_map():
        pass

    def init():
        pass

    def set_led():
        pass


class config:
    ''
    def get_value():
        pass


class freq:
    ''
    def get():
        pass

    def get_cpu():
        pass

    def get_kpu():
        pass

    def set():
        pass


class utils:
    ''
    def flash_read():
        pass

    def gc_heap_size():
        pass

    def heap_free():
        pass

