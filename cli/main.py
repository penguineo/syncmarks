from util.config import load_config


def main():
    try:
        config = load_config()
    except Exception as e:
        raise


if __name__ == "__main__":
    main()
