#Input weight in one unit and output a converted unit value
weight = float(input("Enter weight here: "))
unit_type = input("(K)g or (L)bs: ")

#2.20462 lbs per 1 kg
lbs_to_kg_ratio = 2.20462

if unit_type.upper() == "L":
#converting lbs to kg, ratio is divided
    converted_weight = round(weight/lbs_to_kg_ratio,3)
    print("Weight in Kgs: " + str(converted_weight))
elif unit_type.upper() == "K":
 #converting kg to lbs, ratio is multiplied
    converted_weight = round(weight*lbs_to_kg_ratio,3)
    print("Weight in Lbs: " + str(converted_weight))
else: print("Error in conversion, check unit_type")

print("...Done")