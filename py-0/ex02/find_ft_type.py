
def all_thing_is_obj(object: any) -> int:
    match object:
        case list() | tuple() | set() | dict():
            type_name = type(object).__name__
            type_name = type_name[0].upper() + type_name[1:]
            print(f"{type_name} :", type(object))
        case str():
            print(f"{object} is in the kitchen : {type(object)}")
        case _:
            print("Type not found")

    return 42
