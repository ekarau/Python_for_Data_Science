def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and type(object) == int:
        print(f"Zero: {object} {type(object)}")
    elif object == "" and type(object) == str:
        print(f"Empty: {object} {type(object)}")
    elif object == False and type(object) == bool:
        print(f"Fake: {object} {type(object)}")
    else :
        print("Type not Found")
        return 1
    return 0