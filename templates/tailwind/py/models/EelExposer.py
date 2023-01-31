import eel
import logging
import py.functions


class EelExposer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.fns = [
            v
            for k, v in py.functions.__dict__.items()
            if callable(v) and not k.startswith("_")
        ]

    def expose_fns(self, fns: list = None):
        functions = fns if fns is not None else self.fns
        for fn in functions:
            self.logger.info(f"Exposing {fn.__name__}")
            eel.expose(fn)
