from uuid import uuid4

def generate_random_id():
    code = str(uuid4()).replace('-','')
    return code