# Windows Management Instrumentation to get system Information

import wmi

c = wmi.WMI()
my_system = c.win32_computerSystem()[0]
print(f'Manufacturer: {my_system.Manufacturer}\033[m')
print(f'Model: \033[1:31m{my_system.Model}\033[m')
print(f'Name: \033[1:31m{my_system.Name}\033[m')
print(f'NumberOfProcessors:\033[1:31m{my_system.NumberOfProcessors}\033[m')
print(f'SystemType: \033[1:31m{my_system.SystemType}\033[m')
print(f'SystemFamily: \033[1:31m{my_system.SystemFamily}\033[m')






