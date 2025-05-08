from browsers.google_chrome import GoogleChromeStable
from util.config import load_config
from util.log import configure_logger
from util.log import logger as log


def main():
    try:
        log.info("Starting application.")
        config = load_config()
        configure_logger(log_level=config["log_level"])
        log.success("Starting application.")
        browser_config: dict = config.get("browsers", {})
        for browser_name, browser_settings in browser_config.items():
            if not browser_settings.get("enabled", False):
                continue
            profiles = browser_settings.get("profiles")
            match browser_name:
                case "google-chrome-stable":
                    chrome_stable = GoogleChromeStable
                    if chrome_stable.is_installed:
                        data = chrome_stable.get_bookmarks(profiles)
                case "firefox":
                    pass
                case _:
                    log.warning(f"Unsupported browser: {browser_name}")
                    continue
    except Exception as e:
        log.error(f"Starting application: {e}")
        raise


if __name__ == "__main__":
    main()
