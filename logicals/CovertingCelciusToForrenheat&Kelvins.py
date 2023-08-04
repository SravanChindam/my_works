#program for coverting celcius temp to forrenheat and kelvins
#taking celcius temp as ct
ct = float(input("enter current temparature : "))
#formula for converting ct to forrenheat temp
ft = 1.8 * ct +32
#formula for converting ct to kelvins temp
k = ct + 273.15
print("temp in forreheat is : ",ft)
print("temp in kelvins is : ",k)
