import os
import importlib
from flask import Flask


def register(app: Flask):
    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{__name__}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            func = getattr(module, "register", None)
            if callable(func):
                func(app)
                print(f'> Registered \'{module_name}\' service')
