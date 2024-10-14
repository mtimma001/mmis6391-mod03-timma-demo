from flask import Flask, g
from .app_factory import create_app

app = create_app()

from . import routes
