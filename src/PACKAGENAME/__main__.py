"""
@Goal:
@Author:
@Date:
"""

import argparse
import logging as log

import PACKAGENAME

def main_MYPARSER():
    pass

def set_log_level(verbosity):
    verbosity = verbosity.lower()
    configs = {
        "debug": log.DEBUG,
        "info": log.INFO,
        "warning": log.WARNING,
        "error": log.ERROR,
        "critical": log.CRITICAL,
    }
    if verbosity not in configs.keys():
        raise ValueError(
            f"Unknown verbosity level: {verbosity}\nPlease use any in: {configs.keys()}"
        )
    log.basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=configs[verbosity],
    )

def main():
    parser = argparse.ArgumentParser(prog="PACKAGENAME")
    parser.add_argument(
        "--version",
        action="version",
        version=f"{parser.prog} {PACKAGENAME.__version__}",
    )

    subparsers = parser.add_subparsers(help="sub-command help")

    MYPARSER = subparsers.add_parser(
        "MY_PARSER",
        help="",
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )

    for subparser in (MYPARSER,):
        subparser.add_argument(
            "-v",
            "--verbosity",
            type=str,
            default="info",
            help="Verbosity level  [info]",
        )

    args = parser.parse_args()
    if not hasattr(args, "subparser"):
        parser.print_help()
    else:
        set_log_level(args.verbosity)
        log.debug(f"Args: {str(args)}")
        if args.subparser == "MYPARSER":
            main_MYPARSER()

if __name__ == "__main__":
    main()