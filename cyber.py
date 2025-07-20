import socket
host = 'nsstudio-html.github.io'
print(socket.gethostbyname(host))

import subprocess
subprocess.call(['ping', '-c', '5', 'google.com'])