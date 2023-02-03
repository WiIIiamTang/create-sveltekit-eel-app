import argparse
import logging
import sys
import platform
import io


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=800)
    parser.add_argument("--height", type=int, default=600)
    parser.add_argument("--dev", action="store_true", default=False)
    parser.add_argument("--console", action="store_true", default=False)
    parser.add_argument("--mode", type=str, default="chrome")
    return parser.parse_args()


def main(args: argparse.Namespace):
    if not args.console:
        # Fix for when packaging app with --noconsole
        # https://github.com/python-eel/Eel/issues/654
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

    # WARN: Any imports that use eel must be after the above fix
    import eel
    from py.models import EelExposer

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
    )

    eel.init(
        "build" if not args.dev else "src",
        [".tsx", ".ts", ".jsx", ".js", ".html", ".svelte"],
    )
    EelExposer().expose_fns()

    logging.info("Eel ws running on ws://localhost:8888")

    try:
        eel.start(
            "" if not args.dev else {"port": 5173},
            size=(args.width, args.height),
            port=8888,  # this should not be changed
            mode=None if args.mode == "None" else args.mode,
        )
    except EnvironmentError:
        if sys.platform in ["win32", "win64"]:
            try:
                platform_release = int(platform.release())
            except ValueError:
                raise EnvironmentError("Eel failed to start.")
            if platform_release >= 10:
                logging.error(
                    f"Eel failed to start with {args.mode}, defaulting to Edge"  # noqa
                )
                eel.start(
                    "" if not args.dev else {"port": 5173},
                    size=(args.width, args.height),
                    port=8888,  # this should not be changed
                    mode="edge",
                )
        else:
            raise EnvironmentError("Eel failed to start.")


if __name__ == "__main__":
    main(parse_args())
