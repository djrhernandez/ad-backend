from flask import Flask
from flask_cors import CORS

import sys 
import logging as log

from src.routes import init_app
from src.config import Config

# Configuring logs for App
handler = log.FileHandler('adlog.log', encoding='utf-8')
handler.setFormatter(log.Formatter('[%(asctime)s] %(levelname)s | %(name)s: %(message)s'))

log.basicConfig(
    level=log.INFO,
    handlers=[handler]
)
logger = log.getLogger(__name__)


app = Flask(__name__)
CORS(app, resources = {r"/*": {"origins": Config.CORS_ORIGINS }})


if __name__ == "__main__":
    init_app(app, logger)
    app.run(debug=True)