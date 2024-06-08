class File:
    """
    File class represents a File that can be manipulated, stored, deleted, etc.
    """

    def __init__(self, file, path) -> None:
        self.file = file
        self.file_name = self.file.name
        self.path = f'{path}/{self.file_name}'

    def save(self) -> bool:
        """
        Tries to save the file in it's path.

        Returns:
            bool: True when transaction was successfull
                  False when transaction failed
        """
        try:
            with open(self.path, "wb+") as destination:
                for chunk in self.file.chunks():
                    destination.write(chunk)
            return True
        except Exception as e:
            print(e)
            return False
