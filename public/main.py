from browser import document, html

# flowin1 = document.getElementById("flowin1").style
# flowin2 = document.getElementById("flowin2").style
# flowin3 = document.getElementById("flowin3").style
# flowin4 = document.getElementById("flowin4").style
# waterLev = document.getElementById("waterLev").style
CAN_HEIGHT = 700
CAN_WIDTH = 500
CAN_S = 500*500

SPEED = 1000  # 恒定 1000px/s  1px/ms 50px/50ms


MAX_FLOWIN = 2450000
# 每秒最大流入量 1000x70x70=49000000
# 每50ms最大流入量 50x70x70=2450000
#
# 每秒最大流出量 1000x40x40 = 1600000
# 每50ms最大流出量 50x40x40 = 800000

# 理论每秒水位最大上涨量 4900000/500/500=19.6px

MAX_FLOWOUT = 800000
TARGET = 300

waterLev_t0 = 100
waterLev_t = waterLev_t0


def flowin_speed():
    ele = document.getElementById("flowin1")
    style = ele.style
    speed = float(style.height.replace('px', ''))
    return speed


def flowout_speed():
    ele = document.getElementById("flowout")
    style = ele.style
    speed = float(style.height.replace('px', ''))
    return speed


def set_flowin_speed(speed):
    """set the flowin speed in range [0-100]

    Arguments:
        speed {int} -- [0-100]%
    """
    flowin1 = document.getElementById("flowin1").style
    flowin2 = document.getElementById("flowin2").style
    flowin3 = document.getElementById("flowin3").style
    flowin4 = document.getElementById("flowin4").style
    flowin1.height = str(speed*70/100)+"px"
    flowin2.height = str(speed*70/100)+"px"
    flowin3.height = str(speed*70/100+5)+"px"
    flowin3.width = str(speed*70/100)+"px"
    flowin4.width = str(speed*70/100)+"px"


def set_flowout_speed(speed):
    pass


def t0_status():
    global waterLev_t
    global waterLev_t0
    waterLev = document.getElementById("waterLev")
    style_lev = waterLev.style
    style_lev.height = str(waterLev_t0-5)+"px"
    style_lev.width = "100%"
    flowin4 = document.getElementById("flowin4")
    style_flowin = flowin4.style
    style_flowin.height = str(CAN_HEIGHT-waterLev_t0)+"px"


def calculate():
    # 水位上涨量 流入-流出 / 底面积
    set_flowin_speed(10)
    global waterLev_t
    if waterLev_t <= 690 and waterLev_t >= 5:
        waterLev_t += ((flowin_speed()/70)*MAX_FLOWIN -
                       (flowout_speed()/40)*MAX_FLOWOUT)/500/500
        waterLev = document.getElementById("waterLev")
        style_lev = waterLev.style
        style_lev.height = str(waterLev_t-5)+"px"

        flowin4 = document.getElementById("flowin4")
        style_flowin = flowin4.style
        style_flowin.height = str(700-waterLev_t)+"px"

    if waterLev_t < 50:
        flowout = document.getElementById("flowout").style
        flowout.height = str(waterLev_t-5)+"px"

    try:
        script = document.getElementById("pid")
        exec(script.html)
    except:
        print('没法运行')
    # print(scr.html)





agent = document.getElementById('calculator').bind('click', calculate)
init = document.getElementById("init").bind('click', t0_status)
init.click()
