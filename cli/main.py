from util.config import load_config
from util.log import configure_logger, logger


def main():
    try:
        logger.info("Starting application.")
        config = load_config()
        configure_logger(log_level=config["log_level"])
        logger.success("Starting application.", extra={"config": config})
    except Exception as e:
        logger.error("Starting application.", extra={"error": e})
        raise


if __name__ == "__main__":
    main()
