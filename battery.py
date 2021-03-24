#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import psutil
import pymsgbox
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

if plugged:
    pymsgbox.alert('Battery is at ' + percent + '%' + 'plugged in | ' + ' You\'re good to go!' )
else:
    if percent > 70:
        pymsgbox.alert('Battery is at ' + percent + '%' + ' but not plugged in | '+' Let\'s get to work!')
    elif percent < 70 and percent > 40:
        pymsgbox.alert('Battery is at ' + percent + '%' + ' but not plugged in | '+' Keep an eye on that battery level... ')
    elif percent < 40 and percent > 15:
        pymsgbox.alert('Battery is at ' + percent + '%' + ' but not plugged in | '+' She\'s running low. Time to get the charger')
    else:
        pymsgbox.alert('Battery is at ' + percent + '%' + ' but not plugged in | '+' You did this to yourself ( ° ͜ʖ͡°)╭∩╮')

