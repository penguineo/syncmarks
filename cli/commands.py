import argparse

from handler import handle_args, handle_generate_sample_parser


def arg_parser():
    """
    Parse command-line arguments.

    Args:
        None

    Returns:
        None

    Raises:
        SystemExit: If invalid arguments are provided (raised by argparse).
    """
    parser = argparse.ArgumentParser(
        prog="syncmarks",
        description="Sync browser bookmarks.",
        epilog="copyright text",
    )

    # Default flags #
    parser.add_argument(
        "-V",
        "--verbose",
        metavar="[Verbosity_Level]",
        type=str,
        choices=["INFO", "DEBUG", "WARN", "ERROR"],
        help="Print logs for more verbose output.\
        Verbosity_Level = [INFO | DEBUG | WARN | ERROR].\
        Default Verbosity_Level is INFO",
    )

    sub_parser = parser.add_subparsers(dest="command", help="subcommand help")

    # Configuration Management #
    config_parser = sub_parser.add_parser("config", help="Config Management")
    config_subparser = config_parser.add_subparsers(
        dest="subcommand", required=True, help="Config subcommands"
    )
    generate_sample_parser = config_subparser.add_parser(
        "generate-sample", help="Generate a sample config file at default path"
    )

    generate_sample_parser.set_defaults(func=handle_generate_sample_parser)

    args = parser.parse_args()
    handle_args(args)
