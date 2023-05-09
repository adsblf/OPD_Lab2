import random
import glob

def give_me_photo_adress():
    ran = random.randrange(1, 51)
    if (ran >= 10):
        photo_adress = "0000" + str(ran)
    else:
        photo_adress = "00000" + str(ran)
    a = glob.glob("C:/Users/main/Desktop/OPD_2/pic/" + photo_adress + "*")
    return a