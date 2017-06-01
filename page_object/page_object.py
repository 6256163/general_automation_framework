


class PageObject(object):
    from .console import Console
    from .navigation import Navigation
    from .login import Login
    from .table import Table

    def get_instence(self, name):
        return self.__getattribute__(name)