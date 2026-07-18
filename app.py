from config.settings import settings
from utils.logger import logger


def main():

    logger.info("Application Started")

    print("=" * 50)
    print(settings.APP_NAME)
    print(settings.APP_VERSION)
    print("=" * 50)

    print("Everything initialized successfully.")


if __name__ == "__main__":
    main()