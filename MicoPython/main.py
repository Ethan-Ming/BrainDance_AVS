from machine import Pin, PWM
import utime
import uasyncio as asyncio

# Here we are adding frequencies from the mindroid website
frequency_collections = [
    [20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 25, 25],  # Frequency set 1
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25],          # Frequency set 2
    [500, 600, 300, 455, 33, 22, 67, 100]                      # Frequency set 3
]

total_collection_length = len(frequency_collections)
current_index = 0
blink_time = 0.5
buzz_pwm = PWM(Pin(32, Pin.OUT))

stop_out = 1 # 1 minute
total_duration = stop_out * 60 * 1000 # meaning 1 minute have 60 seconds 1 second have 1000 miliseconds
start_time = utime.ticks_ms() # this will give us the current time in milliseconds

# defining pin numbers for rgb led1
class RGB:
    def __init__(self,pin_r, pin_g, pin_b):
        self.red_led = PWM(Pin(pin_r, Pin.OUT))
        self.green_led = PWM(Pin(pin_g, Pin.OUT))
        self.blue_led = PWM(Pin(pin_b, Pin.OUT))
    
    def rgb_on(self,freq,color=(255,0,0)):
        self.red_led.freq(freq)
        self.green_led.freq(freq)
        self.blue_led.freq(freq)

        self.red_led.duty(color[0])
        self.green_led.duty(color[1])
        self.blue_led.duty(color[2])
    
    def rgb_off(self):
        self.red_led.duty(0)
        self.green_led.duty(0)
        self.blue_led.duty(0)


    
rgb1 = RGB(27,14,12)
rgb2 = RGB(15,21,4)
print(rgb1)
print(rgb2)



button_pin = Pin(33, Pin.IN, Pin.PULL_UP)
# New button added to select color for the led
button_pin2 = Pin(5, Pin.IN, Pin.PULL_UP) 

current_button_state = 0
previous_button_state = 0
button_debounce_time = 0.01  # seconds
previous_button_state2 = 0

current_list = frequency_collections[current_index]
current_task = None
current_color_index = 0

#           Red,            Green,      Blue
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  

async def frequency_led():
    while True:
        print(utime.ticks_diff(utime.ticks_ms(),start_time), total_duration)
        if utime.ticks_diff(utime.ticks_ms(),start_time) > total_duration:
            break
        for freq in current_list:
            buzz_pwm.freq(freq)
            buzz_pwm.duty(512)
            
            # Manually set RGB LED colors here based on current_color_index
            color = colors[current_color_index]
            print(freq,color)
            
            rgb1.rgb_on(freq,color)
            rgb2.rgb_on(freq,color)
            #########################
            
            await asyncio.sleep(blink_time)
            
            # Turn off buzzer and RGB LEDs
            buzz_pwm.duty(0)
            rgb1.rgb_off()
            rgb2.rgb_off()



async def button_task():
    global current_index
    global previous_button_state
    global current_task
    global current_list

    previous_button_state = 0

    while True:
        current_button_state = button_pin.value()
        await asyncio.sleep(button_debounce_time)

        if current_button_state == 1 and previous_button_state == 0:
            current_index = (current_index + 1) % total_collection_length
            current_list = frequency_collections[current_index]
            print("Current List:", current_list)

            if current_task:
                current_task.cancel()
            current_task = asyncio.create_task(frequency_led())

        previous_button_state = current_button_state

async def button_task2():
    global current_color_index
    global previous_button_state2

    previous_button_state2 = 0

    while True:
        current_button_state2 = button_pin2.value()
        await asyncio.sleep(button_debounce_time)

        if current_button_state2 == 1 and previous_button_state2 == 0:
            current_color_index = (current_color_index + 1) % len(colors)
            print("Current Color:", colors[current_color_index])

        previous_button_state2 = current_button_state2

async def main():
    await asyncio.gather(
        frequency_led(),
        button_task(),
        button_task2()
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
