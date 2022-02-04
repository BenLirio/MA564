import numpy as np
import bitarray


def string_to_bits(s):
    ba = bitarray.bitarray()
    ba.frombytes(s.encode('UTF-8'))
    return np.array(ba.tolist(), dtype=int)

if __name__ == '__main__':
    pass
