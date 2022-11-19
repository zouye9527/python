import psutil
print(' CPU频率 %d GHz ' % psutil.cpu_freq().max)
print(' CPU核数 %d 个' % psutil.cpu_count(logical=False))
print('内存大小 %f GB ' % (psutil.virtual_memory().total/(1024**3)))
print(' C盘大小 %f GB ' % (psutil.disk_usage('C:').total/(1024**3)))
print(' D盘大小 %f GB ' % (psutil.disk_usage('D:').total/(1024**3)))
print(' E盘大小 %f GB ' % (psutil.disk_usage('E:').total/(1024**3)))
print(' F盘大小 %f GB ' % (psutil.disk_usage('F:').total/(1024**3)))