import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import peentar_iot
import deviceHandlerSino

def test_convert_gps_package_data():
	#gps_2
	dataRecv = b'@@Y\x00\x04213GD2016001814\x00\x00\x00\x00\x00@\x01\x00!\xe6\xafX\xa7\xe6\xafX\x9f"\x02\x00\x00\x00\x00\x00h\n\x00\x00\x07\x00@\x00\x04\x00\x04d\x01W\n\x00\x03\x02\x01\x18\x02\x11\x075*\x18\xa0^\x01|z\xec\x16\x01\x00\n\r\xcd\x01^\x03E\x17\r\n'
	convert_result = peentar_iot.hexToDec(dataRecv)
	print (convert_result)
	print (len(convert_result))
	param_list = convert_result[54:len(convert_result)-8]
	gps_data = param_list[70:110]
	gpssat_avail_combi_list = ['cc','cd','ce','cf']
	gpssat_notavail_combi_list = ['0c','0d','0e','0f']
	satcount_combi_list = ['11','00']
	for i in range(len(gpssat_avail_combi_list)):
		gps_data1 = gps_data.replace(gps_data[38:40], gpssat_avail_combi_list[i])
		print (gps_data1)
		device_call = deviceHandlerSino.deviceIPHandler()
		function_result = device_call.gps_data_process(gps_data1)
		print (function_result)
	for a in range(len(gpssat_notavail_combi_list)):
		gps_data1 = gps_data.replace(gps_data[38:40], gpssat_notavail_combi_list[i])
		print (gps_data1)
		device_call = deviceHandlerSino.deviceIPHandler()
		function_result = device_call.gps_data_process(gps_data1)
		print (function_result)
	

print (test_convert_gps_package_data())


	







	

