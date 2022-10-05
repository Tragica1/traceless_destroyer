import os


class Destroyer:
    def fill(self, path, char, count):
        with open(path, 'a+') as myfile:
            myfile.write(char * count)
        with open(path, 'r') as myfile:
            text = myfile.read()
        return text

    def destroy(self, path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
        else:
            return 'File does not exist!'
        return 'File/directory has been destroyed!'
