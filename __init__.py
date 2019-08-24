import display
import leds
import utime
import math

WIDTH = 160
HEIGHT = 80

CWIDTH = 13
CHEIGHT = 20

XSTART = 15
YSTART = 10

OUTER_COLOR = (180, 180, 180)
SCROLLER_TEXT = "         Akronyme Analogiker - funny - but again - unprofessional"


def achar(d, row, col, offset):
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT -
           5 + offset, XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 3 + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 5 + offset, col=OUTER_COLOR)


def kchar(d, row, col, offset):
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 4 + offset, col=OUTER_COLOR)
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT -
           4 + offset, XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)
    d.line(XSTART + col * CWIDTH + CWIDTH - 4, YSTART + row * CHEIGHT +
           7 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + 7 + offset, col=OUTER_COLOR)


def rchar(d, row, col, offset):
    # oben
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 2 + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 5 + offset, col=OUTER_COLOR)
    # rechts
    d.line(XSTART + col * CWIDTH + CWIDTH - 4, YSTART + row * CHEIGHT +
           7 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + 7 + offset, col=OUTER_COLOR)
    # unten
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT -
           5 + offset, XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)


def rcharextended(d, row, col, offset):
    d.rect(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, XSTART +
           col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + CHEIGHT + 15 + offset, col=(0x99, 0xe5, 0x50))
    # unten
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + 15 + offset, col=OUTER_COLOR)
    # unten abschluss
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT +
           15 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + CHEIGHT + 15 + offset, col=OUTER_COLOR)


def ochar(d, row, col, offset):
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 8 + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 12 + offset, col=OUTER_COLOR)


def nchar(d, row, col, offset):
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 8 + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)


def ychar(d, row, col, offset):
    # oben
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + offset,
           XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + 8 + offset, col=OUTER_COLOR)
    # unten
    d.rect(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset, XSTART +
           col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + CHEIGHT + CHEIGHT + offset, col=(0x99, 0xe5, 0x50))
    d.line(XSTART + col * CWIDTH + 7, YSTART + row * CHEIGHT + CHEIGHT + offset,
           XSTART + col * CWIDTH + 7,  YSTART + row * CHEIGHT + CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR
           )


def mchar(d, row, col, offset):
    # links
    d.line(XSTART + col * CWIDTH + 4, YSTART + row * CHEIGHT + 12 + offset,
           XSTART + col * CWIDTH + 4, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)
    d.line(XSTART + col * CWIDTH + 9, YSTART + row * CHEIGHT + 12 + offset,
           XSTART + col * CWIDTH + 9, YSTART + row * CHEIGHT + CHEIGHT + offset, col=OUTER_COLOR)


def echar(d, row, col, offset):
    # oben
    d.line(XSTART + col * CWIDTH + CWIDTH - 4, YSTART + row * CHEIGHT +
           5 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + 5 + offset, col=OUTER_COLOR)
    # unten
    d.line(XSTART + col * CWIDTH + CWIDTH - 6, YSTART + row * CHEIGHT +
           12 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + 12 + offset, col=OUTER_COLOR)


def gchar(d, row, col, offset):
    # oben strich
    d.line(XSTART + col * CWIDTH + 2, YSTART + row * CHEIGHT +
           2 + offset, XSTART + col * CWIDTH + 4, YSTART + row * CHEIGHT + 2 + offset, col=OUTER_COLOR)
    # rechts mitte strich
    d.line(XSTART + col * CWIDTH + CWIDTH - 6, YSTART + row * CHEIGHT +
           10 + offset, XSTART + col * CWIDTH + CWIDTH, YSTART + row * CHEIGHT + 10 + offset, col=OUTER_COLOR)
    # mitte strich nach unten
    d.line(XSTART + col * CWIDTH + CWIDTH - 6, YSTART + row * CHEIGHT +
           10 + offset, XSTART + col * CWIDTH + CWIDTH - 6, YSTART + row * CHEIGHT + CHEIGHT - 3 + offset, col=OUTER_COLOR)


def outline(d, offset):
    # oben
    d.rect(29, 11+offset, 132, 17+offset, col=(0xdf, 0x71, 0x26))
    d.rect(29, 17+offset, 132, 23+offset, col=(0xfb, 0xf2, 0x36))
    d.rect(29, 23+offset, 132, 30+offset, col=(0x99, 0xe5, 0x50))

    d.rect(16, 31+offset, 145, 37+offset, col=(0x30, 0x60, 0x82))
    d.rect(16, 37+offset, 145, 43+offset, col=(0x76, 0x42, 0x8a))
    d.rect(16, 43+offset, 145, 50+offset, col=(0x8f, 0x97, 0x4a))


def akronyme_analogiker(d, offset):
    outline(d, offset)
    d.line(28, 10 + offset, 132, 10 + offset, col=OUTER_COLOR)
    d.line(15, 30 + offset, 145, 30 + offset, col=OUTER_COLOR)
    d.line(15, 50 + offset, 145, 50 + offset, col=OUTER_COLOR)
    for i in range(9):
        d.line(28+i*CWIDTH, 10 + offset, 28+i*CWIDTH,
               10 + CHEIGHT + offset, col=OUTER_COLOR)
    for i in range(11):
        d.line(15+i*CWIDTH, 30 + offset, 15+i*CWIDTH,
               30 + CHEIGHT + offset, col=OUTER_COLOR)

    achar(d, 0, 1, offset)
    achar(d, 1, 0, offset)
    achar(d, 1, 2, offset)
    kchar(d, 0, 2, offset)
    kchar(d, 1, 7, offset)
    rchar(d, 0, 3, offset)
    rchar(d, 1, 9, offset)
    ochar(d, 0, 4, offset)
    ochar(d, 1, 4, offset)
    nchar(d, 0, 5, offset)
    nchar(d, 1, 1, offset)
    ychar(d, 0, 6, offset)
    mchar(d, 0, 7, offset)
    echar(d, 0, 8, offset)
    echar(d, 1, 8, offset)
    gchar(d, 1, 5, offset)
    rcharextended(d, 0, 3, offset)


def scroller(t):
    char_width = 15  # 180/11
    offset = ft / 20.0

    full = int(offset / float(char_width))
    rest = char_width - (int(offset) % char_width)

    full = full % len(SCROLLER_TEXT)

    d.print(SCROLLER_TEXT[full:], posx=rest, posy=62)
    d.rect(0, 62, 15, 80, col=(0, 0, 0))
    d.rect(145, 62, 160, 80, col=(0, 0, 0))


global_start = utime.time_ms()
while True:
    t = utime.time_ms() - global_start
    ft = float(t)
    with display.open() as d:
        d.clear()
        # d.print("peng1", posy=0, fg=[100, 255, 255])
        # d.update()
        # d.print("peng2", posy=0, fg=[100, 255, 255])
        # d.update()
        # for y in range(HEIGHT):
        #     for x in range(WIDTH):
        #         d.pixel(x, y, col = (255, 255, 0))
        offset = int(5.0 * math.sin(ft / 300.0))
        start = utime.time_ms()
        akronyme_analogiker(d, offset)
        end = utime.time_ms()
        scroller(ft)
        d.update()
