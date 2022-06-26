"""
Summary:
    Check if all required environment variables are given
"""
import os
import sys

from dotenv import load_dotenv

load_dotenv()

REQUIRED_VARS = ("DATABASE_URL", "OTHER_VAR")


def _validate_environment():
    """Validate required environment variables are provided"""
    empty_vars = []
    for var in REQUIRED_VARS:
        if not os.getenv(var):
            empty_vars.append(var)
    if empty_vars:
        sys.exit(f"Missing required environment variables: {empty_vars}")


def main() -> int:
    _validate_environment()
    print("SHOWING SECRETS".center(70, "-"))
    print(os.getenv("DATABASE_URL"))
    print("warning: Don't show anyone!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
