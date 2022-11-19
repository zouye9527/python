def getTempandHum():
    """
    读取温度和湿度
    :return:
    """
    while 1:
        with open("/sys/devices/w1_bus_master1/5a-00000895472d/w1_slave") as reader:
            lines = reader.readlines()

        temp = lines[0].strip().split('=')[1]
        humi = lines[1].strip().split("=")[1]
        print("温度：%s  湿度:%s%%" % (temp, humi))