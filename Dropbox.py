import dropbox

class Getfile:
    def __init__(self, accessToken):
        self.accessToken= accessToken
    
    def uploadFile(self, file1, namefile):
        tbx = dropbox.Dropbox(self.accessToken)
        f= open(file1, 'rb')
        tbx.files_upload(f.read(), namefile)

def main():
    accessToken= "sl.Av9XnMl-T5lNQAffjZ3O-D9FEjocKvCpJrzWUNXA2qIibqlyYyWxEUNzZCyI-KRXCqFW9tPwZ4zPUSmWXF5qAv9OCdVsqWwaSaA0JoacoHhW0t1qWHz6zs8sGnjTGqhlZuh_yCjn-Gg"
    getfile = Getfile(accessToken)
    file1 = input("What is the file that you would like to upload? Upload the entire path: ")
    file2 = input("What is the name of the file: ")
    getfile.uploadFile(file1,file2)
    print("The file has been moved from your local system to the dropbox.")

main()