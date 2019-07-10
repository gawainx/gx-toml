import toml
import os


class _obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a,
                        [_obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, _obj(b) if isinstance(b, dict) else b)

class config:
    'Main class of gx-toml'

    def __init__(self, fname):
        """

        :param fname: should be absolute path?
        """
        self._fname = fname
        if os.path.isfile(fname):
            self._cfg_dict = toml.load(fname)
            tmp = _obj(self._cfg_dict)
            for k in tmp.__dict__.keys():
                self.__setattr__(k,tmp.__dict__[k])
        else:
            raise FileNotFoundError
