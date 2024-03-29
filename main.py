import psutil


def get_fan_speeds():
    # возвращает список скоростей вращения вентиляторов в RPM
    return psutil.sensors_fans().values()


def get_cpu_load():
    # возвращает текущую загрузку CPU в процентах
    return psutil.cpu_percent()


while True:
    print(psutil.sensors_temperatures())
    print(get_fan_speeds())