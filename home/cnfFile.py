import glob
import json
import os

from admin.settings import SN_ADDRESS, COMPANY, EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_TLS, SN_LOGIN, SN_PASSWD, TIMEZONE


class cnfFile():

    def __init__(self):
        self.pPath = os.getcwd()+'/'
        #self.pPath = '/mnt/c/Users/EvandroJosiasdeSaoJo/My Documents/GitHub/Test/django/'
        self.pFiles = []
        self.pParam = {}

    def setParams(self, pParam):
        self.pParam = pParam

    def getParams(self):
        return self.pParam

    def readFile(self, pName):
        self.pParam = {}
        try:
            with open(self.pPath+pName) as data_file:
                self.pParam = json.load(data_file)
                data_file.close
            return True
        except FileNotFoundError:
            empresa = {
                'COMPANY': COMPANY,
                'SN_ADDRESS': SN_ADDRESS,
                'SN_LOGIN': SN_LOGIN,
                'SN_PASSWD': SN_PASSWD,
                'TIMEZONE': TIMEZONE,
                'EMAIL_HOST': EMAIL_HOST,
                'EMAIL_USE_TLS': EMAIL_USE_TLS,
                'EMAIL_PORT': EMAIL_PORT,
                'EMAIL_HOST_USER': EMAIL_HOST_USER,
                'EMAIL_HOST_PASSWORD': EMAIL_HOST_PASSWORD,
            }
            f = open(self.pPath+pName, 'w')
            str_ = json.dumps(empresa, indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            f.write(str_)
            f.close()
            return False
        except IOError:
            return False

    def writeFile(self, pName):
        with open(self.pPath+pName, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(self.pParam, indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
            outfile.close

    def loadFiles(self, pExt):
        self.pFiles.clear()
        for f in glob.glob(pExt):
            self.pFiles.Add(f)
