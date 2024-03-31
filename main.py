from Classes.ServerMonitoring import ServerMonitoring
from Classes.ServerRepository import ServerRepository
from settings import settings
from time import sleep
import psutil


repository = ServerRepository(settings.server_host, settings.server_port)

s = ServerMonitoring()
type_point_list = repository.get_all_type_point()

key_type_point = {}

for type_point in type_point_list:
    key_type_point[type_point["name"]] = type_point["id"]

print(key_type_point["CPU_temperature"])
print(key_type_point["CPU_load"])
print(key_type_point["disk_size"])


token = repository.login_pc(settings.login, settings.password)["access_token"]
repository.token = token


while True:
    space, free = s.disk_size()
    load = s.cpu_load()
    temp = s.cpu_temp()

    space = round(space / (1024 * 1024 * 1024), 2)
    free = round(free / (1024 * 1024 * 1024), 2)

    print(f"CPU_temperature: {temp}")
    print(f"disk_size: {space}  free_size: {free}")
    print(f"CPU_load: {load}")

    repository.post_point(str(temp), key_type_point["CPU_temperature"])
    repository.post_point(str(space), key_type_point["disk_size"], str(free))
    repository.post_point(str(load), key_type_point["CPU_load"])

    sleep(settings.time_sleep)

