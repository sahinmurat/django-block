import uuid 

def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-", "")
    print(type(code))
    return code

print(get_random_code())