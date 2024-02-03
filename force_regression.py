import pickle
from utility import *

def main():
    utililty = crex_utility()
    utililty.take_input()
    
    with open('./model/regressor.pkl','rb') as rgr:
        model = pickle.load(rgr)

    utililty.max_t = model.predict([[utililty.ed,utililty.nd,\
                        utililty.l,utililty.mat_S,utililty.fuel,\
                            utililty.ewt,utililty.lwt,utililty.det]])

    print(utililty.max_t)
    
    return

if __name__ == "__main__":
    main()