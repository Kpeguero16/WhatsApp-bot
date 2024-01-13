import pywhatkit
import time

# Get the current time as a struct_time object
# current_time_struct = time.localtime()

# # Extract the hour and minute components
# current_hour = current_time_struct.tm_hour
# current_minute = current_time_struct.tm_min

# message = "Good afternoon! Remember to weight yourself :)"
# while True:
#     current_hour = time.localtime().tm_hour
#     current_minute = time.localtime().tm_min
#     print(current_hour, ":" ,current_minute)
#     if current_hour == 12 and current_minute == 00:
#         pywhatkit.sendwhatmsg_to_group("DMxYjJSzauBBEiPwerV9fd", message, current_hour, current_minute+1, 30, True, 5)
#         break
#     time.sleep(60)

print('Welcome\n')
receiver = input('Would you like to message: 1- Personal number or 2- Group Chat? (1/2): ')
number = input('Please input phone number or group ID: ')
message = input('What message would you like to send:\n')
hour = int(input('At what hour of the day would you like to send the message? (24h): '))
minutes = int(input(f'At what minute of hour {hour} would you like to send the message? ')) + 1

def send_message(type):
    if type == '1':
        pywhatkit.sendwhatmsg(number, message, hour, minutes, 30, True, 5)
    else: pywhatkit.sendwhatmsg_to_group(number, message, hour, minutes, 30, True, 5)

send_message(receiver)




