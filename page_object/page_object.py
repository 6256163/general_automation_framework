class PageObject(object):

    def get_instence(self, name):
        path = name.split('.')
        # 导入package.module
        pa = __import__('.'.join(path[:-1]))
        # 获取模块
        mo = getattr(pa, path[1])
        # 获取类
        cl = getattr(mo,path[-1])
        return cl