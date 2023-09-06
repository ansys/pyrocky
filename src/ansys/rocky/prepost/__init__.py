from .client import connect_to_rocky
from .launcher import launch_rocky

# TODO: Set __version__
# try:
#     import importlib.metadata as importlib_metadata
# except ModuleNotFoundError:
#     import importlib_metadata
#
# __version__ = importlib_metadata.version(__name__.replace(".", "-"))


__all__ = [
    "connect_to_rocky",
    "launch_rocky",
]
