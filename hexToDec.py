import pytest
import os,sys,inspect
import struct
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import libcode

def test_converter_hex_to_dec():
	start_val = [0, 10, 100, 1000, 10000, 20000, 30000, 40000, 50000]
	end_val = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000, 65535]
	for i in range(0,8):
		for i in range (start_val[i],end_val[i]):
			dataRecv = struct.pack("i",i)
			libcode_result = libcode.hexToDec(dataRecv)
			if i == 0:
				return libcode_result
			elif i == 1 | i == 2 :
				return libcode_result[3]+libcode_result[0:3]+libcode_result[4:]
			else:
				return libcode_result[2:4]+libcode_result[0:2]+libcode_result[4:]
			for i in range(start_val[i],end_val[i]):
				list_hex_converter_indexing = list(hex(i))[2:]
				unit_test_result = ''
				if i == 0 | i == 1:
					unit_test_result = '0'+''.join(list_hex_converter_indexing)+'0'*((unit_test_result.count('0', 0, len(libcode_result)))-1)
				elif i == 3:
					unit_test_result = ''.join(list_hex_converter_indexing)+'0'*((unit_test_result.count('0', 0, len(libcode_result)))-1)
				else:
					unit_test_result = ''.join(list_hex_converter_indexing)+'0'*((unit_test_result.count('0', 0, len(libcode_result))))
	assert unit_test_result == libcode_result

