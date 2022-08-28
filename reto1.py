import math
area = float(input())
size_antenna = int(input())
type_antenna = str(input())
range_a = 2600
range_b = 19000
range_c = 1500
range_d = 19600
range_e = 6500
if((area >= 0) and (size_antenna >= 0) and ((type_antenna == "a") or (type_antenna == "b") or (type_antenna == "c") or (type_antenna== "d") or (type_antenna == "e"))):
        if( type_antenna == "a"):
            remaining_area = 11700 * size_antenna 
            if(area != remaining_area):
                missing_area = area - remaining_area
                new_antennas = missing_area / range_a
                if(new_antennas <= 0):
                    print(0)
                else: 
                    print(int(math.ceil(new_antennas)))
            else:
                print(remaining_area)
        elif(type_antenna == "b"):
            remaining_area = 11700 * size_antenna
            if(area != remaining_area):
                missing_area = area - remaining_area
                new_antennas = missing_area / range_b
                if (new_antennas <= 0):
                    print(0)
                else: 
                    print(int(math.ceil(new_antennas)))
            else:
                print(remaining_area)
        elif(type_antenna == "c"):
            remaining_area = 11700 * size_antenna 
            if(area != remaining_area):
                missing_area = area - remaining_area
                new_antennas = missing_area / range_c
                if(new_antennas <= 0):
                    print(0)
                else: 
                    print(int(math.ceil(new_antennas)))
            else:
                print(remaining_area)
        elif(type_antenna == "d"):
            remaining_area = 11700 * size_antenna 
            if(area != remaining_area):
                missing_area = area - remaining_area
                new_antennas = missing_area / range_d
                if(new_antennas <= 0):
                    print(0)
                else: 
                    print(int(math.ceil(new_antennas)))
            else:
                print(remaining_area)
        elif(type_antenna == "e"):
            remaining_area = 11700 * size_antenna 
            if(area != remaining_area):
                missing_area = area - remaining_area
                new_antennas = missing_area / range_e
                if(new_antennas <= 0):
                    print(0)
                else: 
                    print(int(math.ceil(new_antennas)))
            else:
                print(remaining_area)
        else:
            print("Error en los datos.")
else: 
    print("Error en los datos.")