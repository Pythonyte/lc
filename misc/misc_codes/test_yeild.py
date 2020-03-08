def test_map(fs):
    def result_iterator(fs):
        print(fs)
        for future in fs:

            yield future*3

    return result_iterator(fs)


gen = test_map([1,2,3,4,5])
import pdb;pdb.set_trace()