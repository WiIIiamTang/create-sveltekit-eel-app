import eel
import logging
from py.functions import choose_file, hello_from_eel


class EelExposer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.fns = [choose_file, hello_from_eel]

    def expose_fns(self, fns: list = None):
        functions = fns if fns is not None else self.fns
        for fn in functions:
            self.logger.info(f"Exposing {fn.__name__}")
            eel.expose(fn)
