from TCR import Downlink, translate
from . import settings
import pprint

dl = Downlink(settings.TELEMACHUS_HOST, settings.TELEMACHUS_PORT, settings.FREQUENCY)
for key in settings.SUBSCRIPTIONS:
    dl.subscribe(key)

while True:
    data = dl.update()
    if data:
        print(translate(data, settings.PRINT_TRANSLATION))
    # pprint.pprint(d)
