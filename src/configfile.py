import configparser

config=configparser.ConfigParser()

#Add the structure to the file we create
config.add_section('apis')
config.set('apis','yahooapi','https://api.publicapis.org/entries')


#Write the new structure to the new file
with open(r"configfile.ini", 'w') as conf:
    config.write(conf)


def readconfigini():
    config_obj=configparser.ConfigParser()
    config_obj.read("configfile.ini")
    apihead=config_obj["apis"]

    #set your parameters after reading
    yourapi=apihead["yahooapi"]
    #print(yourapi)
    return(yourapi)