SID = int(input("Enter your SID:"))#takes input of SID in integer type
Name = str(input("Enter your name here:"))#takes input of name in string type
Department_Name = str(input("Enter your department name here:"))#takes input of Department name in string type
CGPA = float(input("Enter your CGPA here:"))#takes input of CGPA in float type
#condition to specify the length and beginning characters of SID entered
if str(SID).startswith("2110"):
    SID = str(SID)[:8]
else:
    print("Invalid SID")
#conditions to limit the CGPA in between 0 and 10
try:
    CGPA = float(CGPA)
    if 0 <= CGPA <= 10:
        CGPA = round(CGPA, 2)
    else:
        print("Invalid CGPA")
except ValueError:
    print("Invalid CGPA")
#printing end result
print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", Department_Name, "department and my CGPA is", CGPA)
