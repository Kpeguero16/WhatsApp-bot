import pywhatkit
import time

# Get the current time as a struct_time object
current_time_struct = time.localtime()

# Extract the hour and minute components
current_hour = current_time_struct.tm_hour
current_minute = current_time_struct.tm_min

message = "test message. Sorry Maria."
while True:
    current_hour = time.localtime().tm_hour
    current_minute = time.localtime().tm_min
    print(current_hour, ":" ,current_minute)
    if current_hour == 0 and current_minute == 7:
        pywhatkit.sendwhatmsg_to_group("DMxYjJSzauBBEiPwerV9fd", message, current_hour, current_minute+1, 30, True, 5)
        break
    time.sleep(2)



