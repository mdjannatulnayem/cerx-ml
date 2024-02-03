import pickle
from utility import *

def main():
    utililty = crex_utility()
    utililty.take_input()

    with open('./model/classifier.pkl','rb') as cls:
        model = pickle.load(cls)

    utililty.det = model.predict([[utililty.ed,utililty.nd,\
                        utililty.l,utililty.mat_S,utililty.fuel,\
                            utililty.ewt,utililty.lwt]])

    print(utililty.det)

    return

if __name__ == "__main__":
    main()