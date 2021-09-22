#part1
weight = float(input("Enter your weight:"));
height = float(input("Enter your height in inches:"));
age = float(input("Enter your age in years:"));
bmrFemale = float(655.1 + (4.35 * weight)+(4.7 * height)-(4.7 * age));#Female
bmrMale = float(66 + (6.2 * weight)+(12.7 * height)-(6.76 * age));#Male
chocolatebar_Female = float(bmrFemale/214);
chocolatebar_Male = float(bmrMale/214);
print(chocolatebar_Female);
print(chocolatebar_Male);





