from os import system

install_resolvconf = \
"""
sudo apt install resolvconf
"""

resolvconf = \
"""
sudo echo "nameserver localhost
nameserver 9.9.9.9
nameserver 149.112.112.112
nameserver 1.1.1.1
nameserver 1.0.0.1" >> /etc/resolvconf/resolv.conf.d/head
"""

install_tor = \
"""
sudo apt install tor
"""

install_anonsurf = \
"""
git clone https://github.com/Und3rf10w/kali-anonsurf.git && sudo ./kali-anonsurf/installer.sh
"""

install_proxychains = \
"""
sudo apt install proxychains
"""

proxychains4_conf = \
"""
sudo echo "random_chain
chain_len = 2

Proxy DNS request - no leaks for DNS data
proxy_dns

remote_dns_subnet 224

tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
socks5 127.0.0.1 9050" >> /etc/proxychains4.conf
"""

install_requirements = \
"""
python -m pip install -r ../requirements.txt
"""

def check_exit_code(exit_code: int, command: str) -> None:
	if exit_code != 0:
		raise RuntimeError(f"Could not execute command: {command}")

check_exit_code(system(install_resolvconf), install_resolvconf)
check_exit_code(system(resolvconf), resolvconf)
check_exit_code(system(install_tor), install_tor)
check_exit_code(system(install_anonsurf), install_anonsurf)
check_exit_code(system(install_proxychains), install_proxychains)
check_exit_code(system(proxychains4_conf), proxychains4_conf)
check_exit_code(system(install_requirements), install_requirements)