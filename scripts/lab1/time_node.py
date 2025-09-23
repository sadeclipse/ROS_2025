#!/usr/bin/env python3
# 

import time
from datetime import datetime
while(True):
    current_datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_datetime_string}")
    time.sleep(5)

