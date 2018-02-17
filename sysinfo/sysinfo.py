# -*- coding: utf-8 -*-

"""Main module."""

import platform
import shutil

def get_platform_info():
    platformInfo = platform.platform() #Will print platform information
    total, used, free = shutil.disk_usage(__file__)
    return '{}\ntotal {}, used {}, free {}: '.format(platformInfo, total, used, free)

if __name__ == '__main__':
    get_platform_info()