import flet as ft
from components.todo import TodoApp


def main(page: ft.Page):
    page.title = "To-Do App"
           
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.update()
    
    # create application instance
    app = TodoApp()
    
    page.add(app)
    
ft.app(target=main)