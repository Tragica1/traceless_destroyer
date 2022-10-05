import os


class Destroyer:
    def fill(self, filename, char, count):
        with open(filename, 'a+') as myfile:
            myfile.write(char * count)
        f = open(filename)
        text = f.read()
        f.close()
        return text
