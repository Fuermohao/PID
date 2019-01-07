cur_bais = 0
pre_bais = 0
bais_sum = 0
target = 300


def PID(kp=-16, ki=0.4, kd=2, value=100):
    global cur_bais
    global pre_bais
    global bais_sum
    global target
    global waterLev_t
    print("value: %s" % value)
    cur_bais = value - target
    bais_sum += cur_bais
    if bais_sum >= 5:
        bais_sum = 5
    elif bais_sum <= -5:
        bais_sum = -5
    div_bais = cur_bais - pre_bais
    pre_bais = cur_bais

    result = kp*cur_bais+ki*bais_sum+kd*div_bais
    if 0 < result < 100:
        return result
    elif result < 0:
        return 0
    elif result > 100:
        return 100


set_flowin_speed(PID(value=waterLev_t))
