from src.config_loader import load_config
cfg = load_config()
app_name = cfg["app"].get("name", "app")

from src.logging_config import setup_logging
import logging
setup_logging(cfg)
logger = logging.getLogger(f"{app_name}.main")
logger.info(f"{app_name} started.")

import src.cli as app

def main():
    app.run(cfg)
    logger.info(f"{app_name} finished.")

if __name__ == '__main__':
    main()
