import ctypes
pqrst1_L1_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_L1_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]#correct

pqrst1_L2_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_L2_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_L3_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_L3_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_avL_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_avL_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]#correct

pqrst1_avR_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_avR_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]#correct

pqrst1_avF_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_avF_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V1_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V1_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V2_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V2_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V3_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V3_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V4_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V4_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V5_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V5_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst1_V6_x = [0.00, 0.1, 0.2, 0.25, 0.35, 0.45, 0.5, 0.6, 0.7, 0.75]
pqrst1_V6_y = [0, 0.05, 0.00, -0.1, 0.7, -0.2, 0.00, 0.05, 0.0, 0.0]

pqrst_xyvalues=[]
#pqrst_yvalues=[]
no_pqrst_segs = 2
lib = ctypes.CDLL("../../hal/HAL.so")
lib.write.argtypes = [ctypes.c_float, ctypes.c_float]
#increment_factor = [0,0,0,0,0,0,0,0,0,0,0,0]
for j in range(1, no_pqrst_segs):
    for i in range(0, 9):
            new_x = pqrst1_L1_x[i] + .75 * (j - 1)
            print("generator.py: [Data Count=""]Sending L1 data to HAL x=", round(new_x,2), " y=" , pqrst1_L1_y[i])        
            pqrst_xyvalues.append(new_x)
            pqrst_xyvalues.append(pqrst1_L1_y[i])
            
            new_x = pqrst1_L2_x[i] + .54 * (j - 1)
            print("generator.py: [Data Count=""]Sending L2 data to HAL x=", round(new_x,2), " y=" , pqrst1_L2_y[i]) 
            pqrst_xyvalues.append(new_x)
            pqrst_xyvalues.append(pqrst1_L2_y[i])       
            #lib.write(new_x, pqrst1_L2_y[i])
print(pqrst_xyvalues)
            

