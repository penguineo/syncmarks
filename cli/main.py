from util.config import load_config
from util.log import configure_logger
from util.log import logger as log


def main():
    try:
        log.info("Starting application.")
        config = load_config()
        configure_logger(log_level=config["log_level"])
        log.success("Starting application.")
    except Exception as e:
        log.error(f"Starting application: {e}")
        raise


if __name__ == "__main__":
    main()
