def rep():
    '''This function asks the user if he wants to continue working or finish

        Keyword arguments:
            check - verification variable

        Return value:
            rep() - recursion in case of incorrect input
            check - verification variable
    '''


    try:
        check = int(input("Do you want to continue? (1 - YES, 0 - NO): "))
    except ValueError:
        print("ERROR")
        return rep()
    if check != 1 and check != 0:
        print("ERROR")
        return rep()
    return check