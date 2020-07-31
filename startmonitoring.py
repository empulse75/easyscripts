import os
port = 0
while port<10:
    print('wlp0s20f0u' +str(port)+'')
    os.system("sudo ip link set wlp0s20f0u" +str(port)+' down')
    os.system("sudo iw dev wlp0s20f0u" +str(port)+' set type monitor')
    os.system("sudo ip link set wlp0s20f0u" +str(port)+' up')
    port = port +1