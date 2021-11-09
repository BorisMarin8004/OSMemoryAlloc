from .Colors import Colors


class MemManagerErrors:
    SPACE = "Failed to allocate, not enough space!"
    NOT_FOUND = "Failed to remove, not found!"

    @staticmethod
    def get_error(error: str):
        return Colors.FAIL + "ERROR: " + error + Colors.ENDC

