# This Python file uses the following encoding: utf-8


import ctypes

class MyDllWrapper:
    def __init__(self, dll_path):
        # DLL 파일 로드
        self.dll = ctypes.CDLL(dll_path)

        self.dll.K23_ALL_WRITE.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool]
        self.dll.K23_ALL_WRITE.restype = ctypes.c_int

        self.dll.K23_ALL_LOAD.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool]
        self.dll.K23_ALL_LOAD.restype = ctypes.c_int

    # pid, savepath, resIndex, inEncoding
    def k23_all_load(self, str1: str, str2: str, num: int, flag: bool) -> int:
        # Encode strings to bytes
        str1_encoded = str1.encode('utf-8')
        str2_encoded = str2.encode('utf-8')

        num = 4 #일단 하드코딩 QHD
        flag = True

        return self.dll.K23_ALL_LOAD(str1_encoded, str2_encoded, num, flag)

    # pid, savepath, resIndex, inEncoding
    def k23_all_write(self, str1: str, str2: str, num: int, flag: bool) -> int:
        # Encode strings to bytes
        str1_encoded = str1.encode('utf-8')
        str2_encoded = str2.encode('utf-8')

        return self.dll.K23_ALL_WRITE(str1_encoded, str2_encoded, num, flag)


