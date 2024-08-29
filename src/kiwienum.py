from enum import StrEnum
    

class KiwiEnum(StrEnum):
    __keyword__ = ""

    def __init__(self, value):
        if self.name == "__keyword__":
            pass
        else:
            keyword = self.__keyword__
            if self.name == keyword:
                pass
            else:
                keyword_value = getattr(self, keyword)
                self._value_ = keyword_value + value