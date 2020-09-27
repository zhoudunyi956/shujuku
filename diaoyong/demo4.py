import configparser
#读取ini方法
def read_ini(inikey,inivaluse):
        config = configparser.ConfigParser()
        config.read("../config/base.ini")
        convaluse=config.get(inikey,inivaluse)
        return convaluse


if __name__ == '__main__':
    print(read_ini("appbase", "app"))


if __name__ == '__main__':
    print(read_ini("appbase","appPackage"))

