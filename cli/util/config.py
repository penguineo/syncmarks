import yaml  # type: ignore

from util.log import logger as log


def load_config(path="config.yaml"):
    log.info(
        "Starting to load config",
        extra={"function": load_config.__name__, "config_path": path},
    )

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
        "Starting to load config",
        extra={"function": load_config.__name__, "config_path": path},
    )
    return config
