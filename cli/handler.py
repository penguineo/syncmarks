from argparse import Namespace

from util.config import config_path, generate_sample_config
from util.log import configure_logger


def handle_args(args: Namespace):
    verbosity_level = args.verbose
    if verbosity_level:
        handle_verbose(verbosity_level)
    if hasattr(args, "func"):
        args.func()


def handle_verbose(verbosity_level: str):
    configure_logger(verbosity_level)


def handle_generate_sample_parser():
    output_path = config_path()
    generate_sample_config(output_path)
