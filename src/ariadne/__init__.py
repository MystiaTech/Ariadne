from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:
    __version__ = version("ariadne")
except PackageNotFoundError:  # during editable dev before build metadata exists
    __version__ = "0.0.0"
