import subprocess
from psutil import process_iter

def port_in_use(port=5000):
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                return True
    return False

def cmd_kill_port(port=5000):
    subprocess.run(['fuser', '-k', str(port) + '/tcp'])
