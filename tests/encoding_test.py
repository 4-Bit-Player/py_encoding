import json
from ast import literal_eval
from time import perf_counter

from py_encoding import encode_data, decode_data, compress_data
from tests.encoding_data_to_check import data_to_check
from copy import deepcopy

p_red = '\033[38;5;160m'
p_reset = '\033[0;0m'
#for char in "{(<[\"NTF]>)}":
#    print(char, ord(char))


def basic_check():
    data = data_to_check[0]

    encoded = encode_data(data)
    dec_data:dict = decode_data(encoded)
    passing = True
    for key, val in dec_data.items():
        if key not in data:
            print(p_red +f"Error in the en-/decoder!\n"
                  f"Key not found in original data: {key}" +p_reset)
            passing = False
            continue
        if data[key] != val and type(data[key]) != type(val):
            print(f"Error in the en-/decoder!\n"
                  f"Val was incorrect: {val}\n"
                  f"Should be        : {data[key]}\n"
                  f"Is type          : {type(data[key])}\n"
                  f"Should type      : {type(val)}")
            passing = False

    for key, val in data.items():
        if key not in dec_data:
            print(p_red + f"Error in the en-/decoder!\n"
                  f"Original not found: {key}" +p_reset)
            passing = False
            continue
    if passing:
        print("Basic En-/Decoding successful!")
    else:
        print("Basic En-/Decoding Failed!")


def full_check():
    passing = True
    for val in data_to_check:
        try:
            encoded_data = encode_data(val)
        except Exception as e:
            passing=False
            print(e)
            print(p_red+ "Failed encoding at:", p_reset, val)
            break

        try:
            dec_data = decode_data(encoded_data)
            if dec_data != val:
                passing = False
                print(p_red+f"Error de/encoding: {type(val)}", p_reset)
                print("Should:", val)
                print("Is    :", dec_data)
                print("Encoded data:" + encoded_data.replace("\3", "\\3"))
                exit()
        except Exception as e:
            passing=False
            print(e)
            print(p_red+"Failed decoding at:", p_reset, val)
            print("Encoded data:" + encoded_data.replace("\3", "\\3"))
            exit()
            break
    if passing:
        print("Full En-/Decoding successful!")
    else:
        print("Full En-/Decoding Failed!")







def small_compare_check():
    for data in data_to_check:
        str(data)
        encode_data(data)
        own_encode_start = perf_counter()
        m_enc_data = encode_data(data)

        own_encode_stop = perf_counter()


        decode_data(m_enc_data)
        own_decode_start = perf_counter()
        m_dec = decode_data(m_enc_data)
        own_decode_stop = perf_counter()
        if type(data) == str:
            continue
        py_encode_start = perf_counter()
        enc_data = str(data)
        py_encode_stop = perf_counter()
        literal_eval(enc_data)
        py_dec_start = perf_counter()
        p_dec = literal_eval(enc_data)
        py_dec_stop = perf_counter()



        if m_dec != p_dec:
            print(p_red+"Isn't the same!"+p_reset)

        print(f"Py enc time: {py_encode_stop -py_encode_start:.7f} seconds.\n"
              f"Py dec time: {py_dec_stop-py_dec_start:.7f} seconds.\n"
              f"My enc time: {own_encode_stop-own_encode_start:.7f} seconds.\n"
              f"My dec time: {own_decode_stop-own_decode_start:.7f} seconds.\n"
              f"Py len     : {len(enc_data)}\n"
              f"My len     : {len(m_enc_data)}")

def large_compare_check(size:int=15):
    #large_data = data_to_check[1]
    large_data = data_to_check[0]

    for i in range(size):
        large_data[i] = deepcopy(large_data)
        #large_data += deepcopy(large_data)


    print("Done creating large data...")
    own_encode_start = perf_counter()
    m_enc_data = encode_data(large_data)
    own_encode_stop = perf_counter()
    own_decode_start = perf_counter()
    m_dec = decode_data(m_enc_data)
    own_decode_stop = perf_counter()
    py_encode_start = perf_counter()
    enc_data = str(large_data)
    py_encode_stop = perf_counter()
    py_dec_start = perf_counter()
    #p_dec = literal_eval(enc_data)
    py_dec_stop = perf_counter()
    #m_dec != p_dec or
    #if m_dec != q_dec:
    #    print(p_red+"Isn't the same!"+p_reset)

    print("Large Data:")
    print(f"str() time         : {py_encode_stop -py_encode_start:.7f} seconds.\n"
          f"literal_eval() time: {py_dec_stop-py_dec_start:.7f} seconds.\n"
          f"My encoder time    : {own_encode_stop-own_encode_start:.7f} seconds.\n"
          f"My decoder time    : {own_decode_stop-own_decode_start:.7f} seconds.\n"
          f"build in string len: {len(enc_data):_} chars.\n"
          f"My string len      : {len(m_enc_data):_} chars.")





#basic_check()
#full_check()




#small_compare_check()
#large_compare_check()




