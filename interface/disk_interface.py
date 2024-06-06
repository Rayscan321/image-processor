# 硬盘接口
import psutil


# 检测可移动硬盘接口
def detect_removable_disk_interface():
    drives = []
    # 获取所有分区
    partitions = psutil.disk_partitions(all=True)
    # 过滤可移动硬盘
    for partition in partitions:
        if 'removable' in partition.opts:
            drives.append(partition.device)
    return drives
