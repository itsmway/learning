class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def printscore(self):
        print('%s:%s' % (self.__name,self.__score))
    def level(self):
        if self.__score > 90:
            return "a"
        elif self.__score>80:
            return "b"
        elif self.__score>60:
            return "c"
        else:
            return "d"

class Lilei(Student):
    def __len__(self):
        return 100
