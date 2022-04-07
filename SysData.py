import platform

print("System information:")

SysInfo = platform.uname()

print("OS: {}".format(SysInfo[0]))
print("OS release: {}".format(SysInfo[2]))
print("OS version: {}".format(SysInfo[3]))
print("Machine type: {}".format(SysInfo[4]))
print("Machine name: {}".format(SysInfo[1]))