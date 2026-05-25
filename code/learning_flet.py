# Import
import flet as ft

# Flet App Structure & Setup
def main(page: ft.Page):
  page.title = "Temperature Converter"
  page.theme_mode = ft.ThemeMode.DARK
  page.window_width = 100
  page.window_height = 100
  page.window_resizable= True
  page.padding = 20

  # Input fields for C, F, K
  celcius_input = ft.TextField(
    label="Celsius C",
    hint_text = "Enter Temperature in Celsius",
    keyboard_type = ft.KeyboardType.NUMBER,
    color=ft.Colors.WHITE,
    border_color=ft.Colors.WHITE,
    on_change = lambda e: convert_to_celcius(e.control.value)
  )

  fahrenheit_input = ft.TextField(
    label="Fahrenheit F",
    hint_text = "Enter Temperature in Fahrenheit",
    keyboard_type = ft.KeyboardType.NUMBER,
    color=ft.Colors.WHITE,
    border_color=ft.Colors.WHITE,
    on_change = lambda e: convert_to_fahrenheit(e.control.value)
  )

  kelvin_input = ft.TextField(
    label="Kelvin K",
    hint_text = "Enter Temperature in Kelvin",
    keyboard_type = ft.KeyboardType.NUMBER,
    color=ft.Colors.WHITE,
    border_color=ft.Colors.WHITE,
    on_change = lambda e: convert_to_kelvin(e.control.value)
  )

  # ADd functionality to the APP
  def convert_to_celcius(value):
    if value and value.strip():
      try:
        celcius = float(value)
        fahrenheit = (celcius * 9/5) + 32 
        kelvin = celcius + 273.15

        fahrenheit_input.value = f"{fahrenheit:.2f}"
        kelvin_input.value = f"{kelvin:.2f}"
        page.update()
      except ValueError:
        celcius_input.value = f"ERROR!"
    
  def convert_to_fahrenheit(value):
    if value and value.strip():
      try:
        fahrenheit = float(value)
        celcius = (fahrenheit - 32) * 5/9 
        kelvin = celcius + 273.15

        celcius_input.value = f"{celcius:.2f}"
        kelvin_input.value = f"{kelvin:.2f}"
        page.update()
      except ValueError:
        celcius_input.value = f"ERROR!"

  def convert_to_kelvin(value):
    if value and value.strip():
      try:
        kelvin = float(value)
        celcius = kelvin - 273.15
        fahrenheit = (celcius * 9/5) + 32 

        fahrenheit_input.value = f"{fahrenheit:.2f}"
        celcius_input.value = f"{celcius:.2f}"
        page.update()
      except ValueError:
        celcius_input.value = f"ERROR!"

  def clear_all(e):
    celcius_input.value = ""
    fahrenheit_input.value = ""
    kelvin_input.value = ""
    page.update()


  # Create main UI -> Containers
  page.add(
    ft.Column([
      ft.Text("Temperature Converter", size = 28, weight = ft.FontWeight.BOLD, text_align = ft.TextAlign.CENTER, color=ft.Colors.BLUE_700),
      ft.Divider(height=20),

      celcius_input, 
      ft.Divider(height=20),
      fahrenheit_input,
      ft.Divider(height=20),
      kelvin_input,
      ft.Divider(height=20),

      ft.Divider(height=20),

      ft.ElevatedButton(
        "Clear All",
        icon=ft.Icons.CLEAR,
        on_click=clear_all,
        style=ft.ButtonStyle(
          bgcolor=ft.Colors.RED_400,
          color=ft.Colors.WHITE,
        )
      ),

      ft.Divider(height=20),

      ft.Container(
        content=ft.Column([
          ft.Text("Conversion Formulas:", weight=ft.FontWeight.BOLD),
          ft.Text("- Celsius to Fahrenheit: F = (C x 9/5) + 32"),
          ft.Text("- Fahrenheit to Celsius: C = (F - 32) x 5/9"),
          ft.Text("- Celsius to Kelvin: K = C + 273.15")
        ], spacing=5),

        border_radius = 10
      )
    ],
    scroll= ft.ScrollMode.AUTO,
    spacing=0
    )
  )

# Run a Flet App
if __name__ == "__main__":
  ft.app(target=main)