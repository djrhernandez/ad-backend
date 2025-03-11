import os

# Base directory path for SQLite or other local files
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5000']
    DEBUG = True
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }