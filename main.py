""" "my logger"""

import sys
from pathlib import Path

from loguru import logger


def get_logger(name: str):
    """
    Configure and return a loguru logger with daily rotation every 14 days.

    Args:
        name: Logger name/module identifier

    Returns:
        Configured loguru logger instance
    """
    # Remove default handler
    logger.remove()

    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Format string with clean output
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )

    # Add console handler (stdout)
    logger.add(
        sys.stdout,
        format=log_format,
        level="DEBUG",
        colorize=True,
    )

    # Add daily rotating file handler (14 day retention)
    log_file = log_dir / "app_{time:YYYY-MM-DD}.log"
    logger.add(
        str(log_file),
        format=log_format,
        level="DEBUG",
        rotation="00:00",  # Rotate at midnight daily
        retention="14 days",  # Keep logs for 14 days
        colorize=False,
    )

    return logger
