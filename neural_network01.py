import numpy as npdef relu(x):    return np.maximum(0, x)def relu_derivative(x):    return np.where(x > 0, 1, 0)def peremn_arr(array1, array2):    array1_np = np.array(array1)    array2_np = np.array(array2)    result_np = np.multiply(array1_np, array2_np)    result = result_np.tolist()    return resultdef arr_bias(arr, offset):    np_arr = np.array(arr)    result = list(np_arr + offset)    return resultdef sum_array(arr):    total = 0    for num in arr:        total += num    return totaldef f2_1in1_2(matrix):    return np.array(matrix).T.tolist()def s2(x, w_a, b):    s2_n = len(w_a)    nei2 = []    hn2 = []    w_b = f2_1in1_2(w_a)    for i in range(s2_n):        arr2 = w_a[i]        result_array = peremn_arr(x, arr2)        arr3 = arr_bias(result_array, b)        x_sl = sum_array(arr3)        hn2.append(x_sl)        x_sl = relu(x_sl)        nei2.append(x_sl)    return w_b, hn2, nei2def ner_netw(w_a, x, b):    sl_k = len(w_a)    wb = []    hn = []    yn = []    for i in range(sl_k):        w = w_a[i]        y = s2(x, w, b)        wb.append(y[0])        hn.append(y[1])        yn.append(y[-1])        x = y[-1]    return wb, hn, yndef find_difference(arr1, arr2):    return [a - b for a, b in zip(arr1, arr2)]def er1(ss, d):    y = ss[-1][-1]    hn = ss[1][-1]    e = find_difference(y, d)    e_exit = []    for ie in range(len(e)):        e0 = e[ie]        hn0 = hn[ie]        e1 = e0 * relu_derivative(hn0)        e_exit.append(e1)    return e_exitdef propagate_error(w, er, x):    ee = peremn_arr(w, er)    s_er = sum_array(ee)    e1 = s_er * relu_derivative(x)    return e1def s_er(ee, x, w0):    er1 = []    for i in range(len(x)):        x1 = x[i]        w1 = w0[i]        er0 = propagate_error(w1, ee, x1)        er1.append(er0)    return er1def backpropagation(nn, d):    ee = er1(nn, d)    wb = nn[0]    kol = len(wb) - 1    xx = nn[-1]    error = []    error.append(ee)    for j in range(kol):        j = 0 - (j+1)        x_pred = xx[j-1]        w0 = wb[j]        ee0 = s_er(ee, x_pred, w0)         ee = ee0        error.append(ee0)    return errordef fm(n, k):    m = []    for i in range(k):        m.append(n)    return mdef ob_n(e, x, w, l, b):    e0 = fm(e, len(x))    ex = peremn_arr(x, e0)    l0 = fm(l, len(x))    exl = peremn_arr(ex, l0)    w_new = find_difference(w, exl)    return w_newdef ob_sl(ww, ee, x, l, b):    kn = len(ee)    w_s_new = []    for i in range(kn):        e = ee[i]        w = ww[i]        w1a = ob_n(e, x, w, l, b)        w_s_new.append(w1a)    return w_s_newdef ob_nn(ee_a, l, b, x, ww):    ee_b = ee_a[::-1]    w_nn = []    for i in range(len(ww)):        w = ww[i]        e1 = ee_b[i]        w_s_new = ob_sl(w, e1, x, l, b)        w_nn.append(w_s_new)        y = s2(x, w_s_new, b)        x = y[-1]    return w_nn# Пример использования функцииx = [1, 2]d = [3]l = 0.005w_a = [[[0.8, 0.5]]]b = 0.1ep = 10nn = ner_netw(w_a, x, b)for i in range(ep):    print(nn[-1][-1])    err = backpropagation(nn, d)    w_nn = ob_nn(err, l, b, x, w_a)    nn1 = ner_netw(w_nn, x, b)    nn = nn1print(nn[-1][-1])