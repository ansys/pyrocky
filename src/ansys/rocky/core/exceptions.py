class PyRockyError(Exception):
    """Generic exception for PyRocky API"""

class RockyLaunchError(PyRockyError):
    """Raised for errors occurred during Rocky application launch"""