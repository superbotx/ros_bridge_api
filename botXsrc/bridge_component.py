from botX.components import BaseComponent
from botX.applications import external_command_pool
from .utils import cmd_kill_port, port_in_use

class BridgeComponent(BaseComponent):

    def __init__(self):
        super(BridgeComponent, self).__init__()
        self.server_pid = 'terminated'

    def setup(self):
        command = 'rosrun ros_bridge server.py'
        cmd_kill_port(port=5000)
        self.server_pid = external_command_pool.start_command(command)

    def shutdown(self):
        external_command_pool.end_command(self.server_pid)
        self.server_pid = 'terminated'
