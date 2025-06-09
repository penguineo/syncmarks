from argparse import Namespace

from util.config import config_path, generate_sample_config
def handle_args(args: Namespace):
    if hasattr(args, "func"):
        args.func()


def handle_generate_sample_parser():
    output_path = config_path()
    generate_sample_config(output_path)
