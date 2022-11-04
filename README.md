# pico_fogger_controller
Pi Pico Code to control a fog machine via variable timer or motion sensors

## Background

I bought [this fog machine](
https://www.amazon.com/AGPTEK-Colorful-Receiver-Wireless-Halloween/dp/B07T28NQKX/ref=sr_1_2_sspa?keywords=fog+machine+agptek&qid=1667520137&qu=eyJxc2MiOiIyLjM4IiwicXNhIjoiMi4yMyIsInFzcCI6IjEuOTAifQ%3D%3D&sprefix=fog+machine+agp%2Caps%2C197&sr=8-2-spons&psc=1) for Halloween. It worked great, but almost too great. The automatic mode ran 30 seconds every 2-3 minutes which seems fine ... until after about 30 minutes and there's smoke all over our front yard into the street.

I wanted a way to control the duration it is on and off to not put out as much fog. But it didn't offer that. It only offered the automatic mode, a wireless button, and a mechanical button.

So I built a small microcontroller circuit to control it the way I wanted, with parts < $10.

## Design

So I did the following:
- Soldered two wire leads to the inside switch of the mechanical button,
- Bought a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/),
- hooked it to a [5V relay module](https://www.amazon.com/dp/B00LW15A4W?psc=1&ref=ppx_yo2ov_dt_b_product_details),
- Hooked relay to the switch leads,
- Wired this [PIR sensor module](https://www.amazon.com/gp/product/B09Q6GKGZV/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) to a GPIO pin, and
- Set the pin as an interrupt to trigger the fogger on motion as well as timer.

The relay module was a useful way to activate that mechanical switch with circuit isolation.

## Source Code

The `main.py` can be uploaded to the Pico via a tool like [Thonny](https://thonny.org/) after you flash it with [MicroPython](https://micropython.org/download/rp2-pico/) firmware.

The `main.py` is a timer that switches the onboard LED and relay pin ON/OFF. When the pins are OFF, it can be optionally interrupted via the interrupt pin (i.e. with a PIR motion detection event), which will turn the LED/relay back on. 
