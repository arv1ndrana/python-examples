class FileMaster():
    def __init__(self, filepath):
        self.filepath_list = filepath.split("/")
        self.file          = self.filepath_list.pop()
        self.file_list     = self.file.split(".")

    def extension(self):
        return self.file_list[0]

    def filename(self):
        return self.file_list[-1]

    def dirpath(self):
        return ("/".join(self.filepath_list)) + "/"

file = FileMaster("/home/arvind/.config/nvim/init.lua")

print(file.extension())
print(file.filename())
print(file.dirpath())
