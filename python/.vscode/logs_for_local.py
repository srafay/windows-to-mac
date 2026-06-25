"""
Debug setup script to configure logging for VS Code debugging sessions.
This file is automatically executed before debugging Python files.
"""

import logging
import sys

# Configure root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add StreamHandler if not already present
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Try to use coloredlogs if available
    try:
        import coloredlogs

        coloredlogs.install(
            level="INFO",
            fmt="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
        )
        print("✓ Coloredlogs enabled for debug session")
    except ImportError:
        print(
            "✓ Standard logging configured (install 'coloredlogs' for colored output)"
        )

print(f"✓ Debug logging configured at {logging.getLevelName(logger.level)} level")
