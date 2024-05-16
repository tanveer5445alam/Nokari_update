import configparser

config= configparser.RawConfigParser()
filepath ="D:\\programming\\Nokari_profile\\configuration\\config.ini"
config.read(filepath)

class ReadConfigProfile():

    @staticmethod
    def EnterProfile():
        job_profile =config.get(" common data","Job_profile")
        return job_profile
