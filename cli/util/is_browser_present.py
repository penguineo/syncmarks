import os

from util.log import logger as log

# NOTE: Installed Browsers are being deteced by finding the executable file.


def is_browser_present_linux(name: str) -> bool:
    log.info(f"Starting to detect {name} in Linux.")
    try:
        for file in os.listdir("/usr/bin"):
            if file == name:
                log.success(f"Starting to detect {name} in Linux.")
                return True
        log.warning(f"{name} not found in Linux")
        return False
    except Exception as e:
        log.error(f"Failed detecting browser in Linux {e}")
        return False


# TODO: Implement the function below for detecting installed browser in window.
def is_browser_present_windows(name: str) -> bool:
    return False


# TODO: Implement the function below for detecting installed browser in mac.
def is_browser_present_mac(name: str) -> bool:
    return False
