


def encode_data(data) -> str:
    f"""
    Small bad encoder to encode almost all basic types. \n
    Supported are:\n
    Float, Int, Str, None, Bool, list, dict, tuple, set. \n
    Not supported are:\n
    bytes and custom types\n
    !!!Warning: Don't use a " followed by an unescaped \3 in your strings! \n
    It will lead to errors!!! \n
    
    (Encoding pure strings will be larger than the basic ones.)
    """
    t = type(data)
    if t == list:
        return _enc_list(data)
    if t == dict:
        return _enc_dict(data)
    if t == tuple:
        return _enc_tuple(data)
    if t == set:
        return _enc_set(data)
    if t == float or t == int:
        return _enc_num(data)
    if t == str:
        return _enc_str(data)
    return _enc_val(data, t)



def _enc_dict(data:dict) -> str:
    out = ["{"]
    for key, val in data.items():
        k_type = type(key)
        v_type = type(val)
        if k_type == str:
            s_key = _enc_str(key)
        elif k_type == int or k_type == float:
            s_key = _enc_num(key)
        elif k_type == tuple:
            s_key = _enc_tuple(key)
        else:
            s_key = _enc_bool_and_none(key)

        if v_type == str:
            s_val = _enc_str(val)
        elif v_type == int or v_type == float:
            s_val = _enc_num(val)
        elif v_type == list:
            s_val = _enc_list(val)
        elif v_type == dict:
            s_val = _enc_dict(val)
        elif v_type == tuple:
            s_val = _enc_tuple(val)
        elif v_type == set:
            s_val = _enc_set(val)
        else:
            s_val = _enc_bool_and_none(val)
        out.append(s_key)
        out.append(s_val)


    out.append("}")
    return "".join(out)

def _enc_list(data:list) ->str:
    out = ["["]

    for val in data:
        v_type = type(val)
        if v_type == int or v_type == float:
            s_val = _enc_num(val)
        elif v_type == str:
            s_val = _enc_str(val)

        elif v_type == list:
            s_val = _enc_list(val)

        elif v_type == tuple:
            s_val = _enc_tuple(val)
        elif v_type == dict:
            s_val = _enc_dict(val)
        elif v_type == set:
            s_val = _enc_set(val)
        else:
            s_val = _enc_val(val, v_type)

        out.append(s_val)

    out.append("]")
    return "".join(out)


def _enc_set(data:set):
    out = ["<"]
    for key in data:
        k_type = type(key)
        if k_type == str:
            s_key = _enc_str(key)
        elif k_type == int or k_type == float:
            s_key = _enc_num(key)
        elif k_type == tuple:
            s_key = _enc_tuple(key)
        else:
            s_key = _enc_val(key, k_type)
        out.append(s_key)
    out.append(">")
    return "".join(out)




def _enc_tuple(data:tuple) -> str:
    out = ["("]

    for val in data:
        v_type = type(val)
        if v_type == int or v_type == float:
            s_val = _enc_num(val)
        elif v_type == str:
            s_val = _enc_str(val)
        elif v_type == list:
            s_val = _enc_list(val)

        elif v_type == tuple:
            s_val = _enc_tuple(val)
        elif v_type == dict:
            s_val = _enc_dict(val)
        elif v_type == set:
            s_val = _enc_set(val)
        else:
            s_val = _enc_val(val, v_type)

        out.append(s_val)



    out.append(")")
    return "".join(out)


def _enc_val(val, val_type):
    if val_type == bool or val_type == type(None):
        return str(val)[0] #+ "\3"


    if val_type == str:
        return _enc_str(val)
    if val_type == int or val_type == float:
        return _enc_num(val)
    error_str = "Encountered unsupported type: " + str(val_type)
    raise ValueError(error_str)

def _enc_bool_and_none(val):
    return str(val)[0]#+"\3"

def _enc_str(val)->str:
    return '"' + val + '"\3'

def _enc_num(val) -> str:
        return str(val) + "\3"





