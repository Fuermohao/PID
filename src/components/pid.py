# PID 水位控制编程训练
# 目标： 
#   实现PID函数，控制左侧的水位模拟视图
# API： 
#   set_flowin_speed(speed) speed 进水速度 取值 0-100，用于设置进水阀门开关量 
#   mark_target(lev) lev 目标水位值，取值 0-700, 该函数用于标记目标水位
# 全局变量： 
#   lev_t  t时刻的水位值，该变量储存着当前的水位值，每次采样周期都会更新该值

cur_bias = 0  # 当前偏差
pre_bias = 0  # 上一次偏差
bias_sum = 0  # 累积偏差
target = 300  # 目标值水位 取值范围 0-700


def PID(kp=-16, ki=-0.4, kd=2,  value=100):
    """ PID 水位控制

    Keyword Arguments:
        kp {int} -- 比例系数 (default: {-16})
        ki {float} -- 积分系数 (default: {-0.4})
        kd {int} -- 微分系数 (default: {2})
        value {int} -- 当前采样反馈值，即当前水位 (default: {100})

    Returns:
        result -- 返回控制量，即进水阀门开关量，取值 0-100
    """
    global cur_bias
    global pre_bias
    global bias_sum
    global target
    
    cur_bias = value - target
    bias_sum += cur_bias

    # 限制积分偏差范围
    if bias_sum >= 5:
        bias_sum = 5
    elif bias_sum <= -5:
        bias_sum = -5
        
    delta_bias = cur_bias - pre_bias
    pre_bias = cur_bias

    result = kp * cur_bias + ki * bias_sum + kd * delta_bias
    if 0 < result < 100:
        return result
    elif result < 0:
        return 0
    elif result > 100:
        return 100

mark_target(target)
set_flowin_speed(PID(value=lev_t))
