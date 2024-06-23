from django.contrib.auth.models import User


class Storable:
    def __init__(self) -> None:
        self.owner = None
        self.name = None
        self.father = None
        self.children = None
        self.path = None
        self.exists = False
        self.is_owned_by_user = False
        self.DB_object = None

    def validateExists(self):
        return True

    def validateUser(self):
        return True

    def getFullPath(self):
        return ''

    def save(self):
        return False

    def delete(self):
        return True


class Folder(Storable):
    def __init__(self, user: User, name: str, father) -> None:
        self.owner = user
        self.name = name
        self.father = father
        self.children = self.getChildren()
        # self.path = self.getFullPath()
        self.exists = self.validateExists()
        self.is_owned_by_user = self.validateUser()

    def getChildren(self):
        return [1, 2, 3]

    def getFullPath(self):
        return 'full_path_here'

    def save(self):
        return False

    def delete(self):
        return True


class File(Storable):
    """
    File class represents a File that can be manipulated, stored, deleted, etc.
    """

    def __init__(self, file, path: str, father: Folder, user: User) -> None:
        self.owner = user
        self.name = self.file.name
        self.father = father
        self.file = file
        # self.path = self.getFullPath()
        self.path = path
        self.exists = self.validateExists()
        self.is_owned_by_user = self.validateUser()

    def validateExists(self):
        return True

    def validateUser(self):
        return True

    def getFullPath(self):
        return ''

    def save(self) -> bool:
        """
        Tries to save the file in it's path.

        Returns:
            bool: True when transaction was successfull
                  False when transaction failed
        """
        try:
            full_path = self.path + '/' + self.name
            with open(full_path, "wb+") as destination:
                for chunk in self.file.chunks():
                    destination.write(chunk)
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        return True
