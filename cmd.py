# import os
# import time
#
# # Декоратор для отображения времени выполнения метода
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time of {func.__name__}: {end_time - start_time:.5f} seconds")
#         return result
#     return wrapper
#
# class CommandPrompt:
#     def __init__(self):
#         self.current_directory = os.getcwd()
#
#     @timing_decorator
#     def list_directories(self):
#         directories = os.listdir(self.current_directory)
#         for item in directories:
#             print(item)
#
#     @timing_decorator
#     def change_directory(self, new_directory):
#         try:
#             os.chdir(new_directory)
#             self.current_directory = os.getcwd()
#         except FileNotFoundError:
#             print(f"Directory '{new_directory}' not found.")
#
#     @timing_decorator
#     def create_directory(self, directory_name):
#         os.mkdir(directory_name)
#         print(f"Directory '{directory_name}' created.")
#
#     @timing_decorator
#     def delete_directory(self, directory_name):
#         os.rmdir(directory_name)
#         print(f"Directory '{directory_name}' deleted.")
#
#     @timing_decorator
#     def rename_directory(self, old_name, new_name):
#         os.rename(old_name, new_name)
#         print(f"Directory '{old_name}' renamed to '{new_name}'.")
#
#     @timing_decorator
#     def view_file(self, file_name):
#         try:
#             with open(file_name, 'r') as file:
#                 content = file.read()
#                 print(content)
#         except FileNotFoundError:
#             print(f"File '{file_name}' not found.")
#
# # Пример использования
# cmd = CommandPrompt()
#
# cmd.list_directories()
#
# cmd.change_directory("example_directory")
# cmd.list_directories()
#
# cmd.create_directory("new_directory")
# cmd.list_directories()
#
# cmd.rename_directory("new_directory", "renamed_directory")
# cmd.list_directories()
#
# cmd.delete_directory("renamed_directory")
# cmd.list_directories()
#
# cmd.view_file("example.txt")
from typing import Protocol


class CommandPromptInterface(Protocol):
    ...


class CommandPrompt:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, mode="r") as file:
                for line in file.readline():
                    print(line.replace("\n", ""))
        except FileNotFoundError:
            print(f'File with named "{self.file_name}" was not found!')

    def create_file(self):
        with open(self.file_name, mode="x") as file:
            ...
