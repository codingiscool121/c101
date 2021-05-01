import dropbox
import os
class TransferData():
    def __init__(self, accessToken):
        self.accessToken=accessToken
    def uploadFile(self,file1,file2):
        print("WENT INTO UPLOAD FILE.")
        ubx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file1):
            for namefile in files:
                path1 = os.path.join(root,namefile)
                relativepath = os.path.relpath(path1, file1)
                dropboxpath = os.path.join(file2, relativepath)
                with open(path1, 'rb' ) as f:
                    ubx.files_upload(f.read(), dropboxpath)
                    print("files uploaded")
transferdata = TransferData("sl.Av9XnMl-T5lNQAffjZ3O-D9FEjocKvCpJrzWUNXA2qIibqlyYyWxEUNzZCyI-KRXCqFW9tPwZ4zPUSmWXF5qAv9OCdVsqWwaSaA0JoacoHhW0t1qWHz6zs8sGnjTGqhlZuh_yCjn-Gg")
file1 = input("Put file path here: ")
file2 = input("Name of the file: ")

transferdata.uploadFile(file1,file2)
