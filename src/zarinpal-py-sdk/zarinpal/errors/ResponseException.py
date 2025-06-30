class ResponseException(Exception):
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code

    def get_status_code(self) -> int:
        return self.status_code