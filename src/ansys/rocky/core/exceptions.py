class PyRockyError(Exception):
    """Generic exception for PyRocky API"""

class RockyLaunchError(PyRockyError):
    """Raised for errors occurred during Rocky application launch"""
    
class RockyApiError(Exception):
    """
    Exception class representing an error generated in the API layer.
    """