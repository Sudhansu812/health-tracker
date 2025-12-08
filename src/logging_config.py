import logging
import logging.config
import yaml
from pathlib import Path

def setup_logging(cfg: dict | None = None) -> None:
    # try to get from the cfg dict or from the logging.yaml file
    try:
        if cfg and isinstance(cfg.get("logging"), dict):
            logging.config.dictConfig(cfg["logging"])
            return

        config_path = Path(__file__).resolve().parents[1] / "config" / "logging.yaml"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as config_file:
                file_cfg = yaml.safe_load(config_file)
            logging.config.dictConfig(file_cfg)
            return

    except (KeyError, ValueError, TypeError, AttributeError, FileNotFoundError, PermissionError, OSError, yaml.YAMLError, ValueError, TypeError, KeyError, Exception):
        pass

    # try to get from the cfg dict
    level = logging.INFO
    try:
        if cfg:
            level_name = cfg.get("logging", {}).get("level", "INFO")
            level = getattr(logging, level_name.upper(), logging.INFO)
    except AttributeError, TypeError, Exception:
        level = logging.INFO
        pass

    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s %(message)s")