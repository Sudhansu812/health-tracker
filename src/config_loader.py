import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from deepmerge import always_merger

def load_env():
    project_root = Path(__file__).resolve().parents[1]
    env_file_path = project_root / "config" / "secrets.env"
    load_dotenv(env_file_path)
    return env_file_path

def load_yaml(env_name = "debug", base_cfg_file_name = "debug"):
    project_root = Path(__file__).resolve().parents[1]
    cfg_dir = project_root / "config"
    base_cfg_file = cfg_dir / f"{base_cfg_file_name}.yaml"
    env_cfg_file = cfg_dir / f"{env_name}.yaml"

    with open(base_cfg_file, "r") as f:
        base_cfg = yaml.safe_load(f.read()) or {}
    with open(env_cfg_file, "r") as f:
        env_cfg = yaml.safe_load(f.read()) or {}

    cfg = always_merger.merge(base_cfg, env_cfg)

    return cfg

def load_config():
    load_env()
    env_name = os.getenv("ENV", "debug")
    base_cfg_file_name = os.getenv("BASR_CONFIG", "debug")
    cfg = load_yaml(env_name, base_cfg_file_name)
    return cfg