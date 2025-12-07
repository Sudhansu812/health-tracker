from config_loader import load_config
cfg = load_config()
app_name = cfg["app"].get("name", "app")

from logging_config import setup_logging
import logging
setup_logging()
logger = logging.getLogger(app_name + ".main")
logger.info(f"{app_name} started.")

import cli as app

def main():
    app.run(cfg)

if __name__ == '__main__':
    main()
