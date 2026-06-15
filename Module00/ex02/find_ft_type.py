def all_thing_is_obj(object: any) -> int:
    type_of_object = type(object)
    all_types = {"List": list, "Tuple": tuple, "Set": set, "Dict": dict}
    found = False

    for k, v in all_types.items():
        if v == type_of_object:
            print(f"{k} : {type_of_object}")
            found = True
    if type_of_object == str:
        print(f"{object} is in the kitchen : {type_of_object}")
        found = True
    if not found:
        print("Type not found")
    return 42