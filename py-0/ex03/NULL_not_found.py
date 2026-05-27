def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print(f"Nothing: {object} {type(object)}")
        case float() if object != object:  # Check for NaN
            print(f"Cheese: {object} {type(object)}")
        case False:
            print(f"Fake: {object} {type(object)}")
        case 0:
            print(f"Zero: {object} {type(object)}")
        case str() if object == "":
            print(f"Empty: {type(object)}")
        case _:
            print("Type not Found")
            return 1

    return 0
