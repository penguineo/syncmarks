import platform
from pathlib import Path
from shutil import copy2

import yaml  # type: ignore

from util.log import logger as log


def load_config(path: Path):
    log.info(
        "Loading config",
        extra={"function": load_config.__name__, "config_path": path},)

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    for key, value in config.items():
        if isinstance(value, str):
            try:
                config[key] = value.format(**config)
            except KeyError as e:
                raise ValueError(f"Missing key during interpolation: {e}")
            except Exception as e:
                raise RuntimeError(f"Error formatting key '{key}': {e}")
    log.success(
        "Loading config",
        extra={"function": load_config.__name__, "config_path": path},
    )
    return config


def config_path() -> Path:
    """
    Return the path of default config file based on the current OS.

    Args:
        None

    Returns:
        Path: A Path object pointing to the default config file location.

    Raises:
        None: This function does not raise any exceptions.
    """
    log.info("Determining config path")
    os_name = platform.system()
    match os_name:
        case "Linux":
            log.debug("Detected OS: Linux")
            log.success("Determining config path")
            return Path("~/.config/syncmarks/config.yml").expanduser()
        # TODO: Implement default folder location for config in windows and macOs,
        #
        # case "Windows":
        #     log.debug("Detected OS: Windows")
        #     return ""
        # case "Darwin":
        #     log.debug("Detected OS: macOS")
        #     return ""
        case _:
            log.error(f"Unsupported OS: {os_name}")
            return Path("")


def generate_sample_config(path: Path):
    """
    Generate a sample configuration file at the specified path.

    Args:
        path (Path): The path where the sample configuration will be saved.
            This should be a `Path` object pointing to the desired location.

    Returns:
        None
    """
    log.info("Generating sample config")
    dest_path = Path(path)
    if not dest_path.exists():
        log.debug(f"Config path not found {path}")
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    sample_config_path = Path.cwd() / "sample_config.yaml"
    copy2(sample_config_path, dest_path)
    log.info(f"Sample config copied to {dest_path}")
