from i3pystatus import Status
from i3pystatus.weather import weathercom
import netifaces

status = Status(standalone=True)

# documentation = http://docs.enkore.de/i3pystatus

status.register("clock", format="%a %-d %b %H:%M:%S", color="#0FF000")
status.register("weather", colorize=True, interval=300,
        backend=weathercom.Weathercom(
            location_code='RSMK0150:1:RS',
            units='metric'
        )
)

ifaces = netifaces.interfaces()
gateways = netifaces.gateways()
values = list(gateways['default'].values())
try:
    iface = values[0][44]
except IndexError: # gateway is not available yet
    iface = ''

if iface not in ifaces:
    iface = ifaces[int(len(ifaces) / 2)]

status.register("network", interface=iface,
        format_down="DOWN: {interface}", graph_style="braille-fill", detached_down=False,
        format_up="{bytes_recv}↓{bytes_sent}↑", interval=5)

status.register("pulseaudio", format="♪: {db}dB")
status.register("xkblayout")
status.register("disk",path="/",format="{used} / {total}G [{avail}G]",)
status.register("keyboard_locks", caps_off='', num_off='', scroll_off='')
status.run()
