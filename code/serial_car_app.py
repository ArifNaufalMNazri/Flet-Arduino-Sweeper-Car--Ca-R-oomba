# Imports
import flet as ft 
import serial
import time
import asyncio

#Serial ports
port = 'COM3'
baud_rate = 9600

arduino = serial.Serial(port = port, baudrate = baud_rate, timeout = 1)

#App Structure and UI
#Async function to: 1. Send serial to Arduino
#                   2. Check for button hold
async def main(page: ft.Page):
  page.title = "SERIAL CAR CONTROL APP"
  page.theme_mode = ft.ThemeMode.DARK
  page.height = 500
  page.width = 500
  page.resizable = True
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

  hold_button = False

  async def send_serial(message):
    while hold_button:
      data = message + '\n'
      arduino.write(data.encode('utf-8'))
      await asyncio.sleep(0.1)

  def held_down(e,message):
    nonlocal hold_button 
    hold_button = True
    page.run_task(send_serial, message)
    direction.value = message

  def not_held(e):
    nonlocal hold_button 
    hold_button = False
    
    arduino.write('stop\n'.encode('utf-8'))
    direction.value = "stop"
  
  def button(button_name, message):
    return ft.GestureDetector(
      mouse_cursor = ft.MouseCursor.CLICK,

      on_long_press_start = lambda e: held_down(e, message),
      on_long_press_end = not_held,
      on_tap_down = lambda e: held_down(e, message),
      on_tap_up = not_held,
      on_tap_cancel = not_held,
      
      content = ft.Container(
        content = ft.Icon(
          icon = button_name,
          color = ft.Colors.WHITE,
          size = 50,
        ),
        bgcolor = ft.Colors.RED_400,
        padding = 10,
        border_radius = 10,  
        width = 80,
        height = 80,
      )
    )
  
  async def windowClose(e):
    if e.data == "close":
      if 'ardunio' in locals() and arduino.is_open:
        nonlocal hold_button
        hold_button = False
        arduino.close()

      await page.window.destroy()

  page.window.on_event = windowClose

  direction = ft.TextField(
          label = "Direction",
          keyboard_type = ft.KeyboardType.TEXT, 
          read_only = True,
          color = ft.Colors.WHITE,
          border_color = ft.Colors.WHITE
          )

  page.add(
    ft.Column(
     controls = [
        ft.Text("SERIAL CAR CONTROLLER", size = 40, weight = ft.FontWeight.BOLD, text_align = ft.TextAlign.CENTER, color=ft.Colors.BLUE_700),

      ft.Row([
        button(ft.Icons.ARROW_UPWARD, "forward")
      ], 
      alignment = "center"),

      ft.Row([
        button(ft.Icons.ARROW_LEFT, "left"),
        ft.Container(width = 50),
        button(ft.Icons.ARROW_RIGHT, "right"),

      ], 
      alignment = "center"),

      ft.Row([
        button(ft.Icons.ARROW_DOWNWARD, "backward")
      ],
      alignment = "center"),
      
      ft.Row([
        direction
      ], alignment = ft.Alignment.TOP_RIGHT)
      ],
     spacing = 10
    )
  )

if __name__ == "__main__":
  ft.app(target = main)