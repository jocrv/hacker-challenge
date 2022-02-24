def predictTemperature(startDate, endDate, temperature, n):
    try:


try:
        startDate = str(input())
    except:
        startDate = None

    try:
        endDate = str(input())
    except:
        endDate = None

    temperature_cnt = 0
    temperature_cnt = int(input())
    temperature_i = 0
    temperature = []
    while temperature_i < temperature_cnt:
        temperature_item = float(input())
        temperature.append(temperature_item)
        temperature_i += 1


    n = int(input())

    res = predictTemperature(startDate, endDate, temperature, n);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()
