import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", "-v", action="store_true", help="print the version and exit")

    args = parser.parse_args()

    if args.version:
        from . import VERSION
        print(f"simplemdm {VERSION}")
        exit(0)


if __name__ == "__main__":
    main()
