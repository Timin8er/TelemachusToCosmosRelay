from TCL import Downlink
from . import settings
import pprint

dl = Downlink(settings.TELEMACHUS_HOST, settings.TELEMACHUS_PORT, 500)
dl.subscribe("v.altitude")
dl.subscribe("r.resource[LiquidFuel]")

while True:
    d = dl.update()
    pprint.pprint(d)
