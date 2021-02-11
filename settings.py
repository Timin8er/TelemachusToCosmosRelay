TELEMACHUS_HOST = '127.0.0.1'
TELEMACHUS_PORT = 8085

FREQUENCY = 500

COSMOS_IP = '127.0.0.1'
COSMOS_PORT = 1248


SUBSCRIPTIONS = [
    # 'v.missionTime' removed because this is automatically recieved data
    'v.altitude',
    'r.resource[LiquidFuel]'
]


PRINT_TRANSLATION = {
    'v.missionTime':'{:.3f} ',
    'v.altitude':'{:.3f} ',
    'r.resource[LiquidFuel]':'{:.3f}'
}


STRING_TRANSLATION = {
    'v.missionTime':'{:20}',
    'v.altitude':'{:20}',
    'r.resource[LiquidFuel]':'{:20}'
}
