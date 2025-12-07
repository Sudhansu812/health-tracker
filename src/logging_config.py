import logging
import logging.config
import yaml
from pathlib import Path

def setup_logging() -> None:
    config_path = Path(__file__).resolve().parents[1] / "config" / "logging.yaml"
    with open(config_path, "r") as config_file:
        cfg = yaml.safe_load(config_file)
    logging.config.dictConfig(cfg)