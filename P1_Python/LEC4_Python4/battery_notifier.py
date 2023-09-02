#-------------------------------------------------
# Run this code (% Battery and make Notification).
#-------------------------------------------------

from pynotifier import Notification

import psutil

battery = psutil.sensors_battery()
percent = battery.percent

print(percent)
Notification ("Battery Percentage", str (percent)+ "%Percent Remaining", duration=10).send()
