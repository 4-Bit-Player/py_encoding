from tests import encoding_test, byte_encoding_test


def main():
    encoding_test.basic_check()
    encoding_test.full_check()
    byte_encoding_test.basic_check()
    byte_encoding_test.full_check()
    exit()






if __name__ == '__main__':
    main()