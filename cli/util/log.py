import sys

from loguru import logger


def configure_logger(log_level="INFO", log_file="logs/log_{time}.json"):
    logger.remove()

    logger.add(
        log_file,
        level=log_level,
        serialize=True,
        rotation="10 MB",
        retention="7 days",
    )

    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>",
        colorize=True,
        serialize=False,
    )
