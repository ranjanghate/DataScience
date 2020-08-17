#implicit conversion

int1 = 55
float1=55.55
sum = int1 + float1
print(sum)

#explicit conversion
float2 = 1.75
int2 = int(float2)
print(int2)

#string to int 
string = '555'
int3 = int(string)
float3=float(string)
print(int3,float3)

#int/float to string 
int4=55
float4=55.55

string1=str(int4)
string2=str(float4)

print(string1,string2,string1+string2,string2+string1)
