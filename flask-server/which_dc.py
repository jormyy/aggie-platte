def WhichDC():
    '''
        prompts user for specific dining common to get link
        not case-sensitive but user must type "segundo", "tercero", or "cuarto"
        returns url
    '''
    valid = False
    while not valid:
        valid = True
        dc = input("Which dining commons did you eat at? Type Segundo, Tercero, or Cuarto: ")
        if dc.lower() == "segundo":
            url = "https://housing.ucdavis.edu/dining/menus/dining-commons/segundo/"
        elif dc.lower() == "tercero":
            url = "https://housing.ucdavis.edu/dining/menus/dining-commons/tercero/#"
        elif dc.lower() == "cuarto":
            url = "https://housing.ucdavis.edu/dining/menus/dining-commons/cuarto/"
        # elif dc.lower() == "latitude":
        #     url = "https://housing.ucdavis.edu/dining/menus/dining-commons/latitude/"
        else:
            print("Please enter a valid dining common.")
            valid = False

    return url