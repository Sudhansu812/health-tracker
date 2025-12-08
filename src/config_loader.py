import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

try:
    from deepmerge import always_merger
except ModuleNotFoundError, ImportError, Exception:
    always_merger = None  # fallback to simple merge

def load_env():
    project_root = Path(__file__).resolve().parents[1]
    env_file_path = project_root / "config" / "secrets.env"
    if env_file_path.exists():
        load_dotenv(env_file_path)
    else:
        # Just a learning project, so silently ignore missing .env file
        pass
    return env_file_path

# Simple merge in case deepmerge is not available
def _simple_merge(base: dict, override: dict) -> dict:
    result = dict(base or {})
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = _simple_merge(result.get(k, {}), v)
        else:
            result[k] = v
    return result


def load_yaml(env_name: str = "development", base_cfg_file_name: str = "base"):
    project_root = Path(__file__).resolve().parents[1]
    cfg_dir = project_root / "config"
    base_cfg_file = cfg_dir / f"{base_cfg_file_name}.yaml"
    env_cfg_file = cfg_dir / f"{env_name}.yaml"

    base_cfg = {}
    env_cfg = {}

    if base_cfg_file.exists():
        with open(base_cfg_file, "r", encoding="utf-8") as f:
            base_cfg = yaml.safe_load(f) or {}
    if env_cfg_file.exists():
        with open(env_cfg_file, "r", encoding="utf-8") as f:
            env_cfg = yaml.safe_load(f) or {}

    if always_merger:
        cfg = always_merger.merge(base_cfg, env_cfg)
    else:
        cfg = _simple_merge(base_cfg, env_cfg)

    return cfg

def load_config():
    load_env()
    env_name = os.getenv("ENV", "development")
    base_cfg_file_name = os.getenv("BASE_CONFIG", "base")
    cfg = load_yaml(env_name, base_cfg_file_name)
    return cfg