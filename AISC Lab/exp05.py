def input_meth():
    elements = [i for i in input("Enter elements >>> ").split(",")]
    membership_val = []
    print("Enter membership function for all these elements>>> ")
    for i in range(len(elements)):
        mem = float(input())
        if(0 <= mem <= 1):
            membership_val.append(mem)
        else:
            print("Membership values are between [0,1]")
            mem = float(input("Please Enter values between 0-1 >>> "))
            while True:
                if(0 <= mem <= 1):
                    membership_val.append(mem)
                    break
                else:
                    print("Membership values are between [0,1]")
                    mem = float(input("Please Enter values between 0-1 >>> "))
    # Creating the Main Function
    mu = {}
    for i in range(len(elements)):
        mu[membership_val[i]] = elements[i]
    return mu, membership_val, elements


print("--------------------Enter values of SET A--------------------")
set_A, set_A_ele, set_A_vars = input_meth()
print(">>>>>PLEASE ENSURE ELEMENTS ARE SAME!! TO GET PROPER ANSWERS<<<<<")
print("--------------------Enter values of SET B--------------------")
set_B, set_B_ele, set_B_vars = input_meth()
print("Set A is  >>> ", set_A)
print("Set B is  >>> ", set_B)
print("-----------------------------------------------------------")

# Union of Set A and B
AuB = []
AuB_vals = []
for i in range(len(set_A)):
    AuB.append(str(set_A_vars[i])+"/"+str(max(set_A_ele[i], set_B_ele[i])))
    AuB_vals.append(max(set_A_ele[i], set_B_ele[i]))
print("Union of set A and set B is {}".format(AuB))

# Intersection of Set A and B
AintB = []
AintB_vals = []
for i in range(len(set_A)):
    AintB.append(str(set_A_vars[i])+"/"+str(min(set_A_ele[i], set_B_ele[i])))
    AintB_vals.append(min(set_A_ele[i], set_B_ele[i]))
print("Intersection of set A and set B is {}".format(AintB))

# Complement of Set A
A_c = []
A_c_vals = []
for i in range(len(set_A)):
    A_c.append(str(set_A_vars[i])+"/"+str(format(1.0 - set_A_ele[i], ".1f")))
    A_c_vals.append(format(1.0 - set_A_ele[i], ".1f"))

print("Complement of set A is {}".format(A_c))

# Complement of Set B
B_c = []
B_c_vals = []
for i in range(len(set_B)):
    B_c.append(str(set_A_vars[i])+"/"+str(format(1.0 - set_B_ele[i], ".1f")))
    B_c_vals.append(format(1.0 - set_B_ele[i], ".1f"))
print("Complement of set B is {}".format(B_c))

# Difference of Set A and B
AminusB = []
for i in range(len(set_A)):
    AminusB.append(str(set_A_vars[i])+"/" +
                   str(format(set_A_ele[i] - set_B_ele[i], ".1f")))
print("Difference of set A and set B is {}".format(AminusB))

# To-Do
# Prove De Morgan's Law
print("-----------------------------------------------------------")
print("To prove is (A union B)' = A' intersection B'")
AuB_c = [format(float(1.0 - i), ".1f") for i in AuB_vals]
AcintBc_vals = []
for i in range(len(set_A)):
    AcintBc_vals.append(min(A_c_vals[i], B_c_vals[i]))
print(" (A union B)' = ", AuB_c)
print("A' intersection B' = {}".format(AcintBc_vals))

if(AuB_c == AcintBc_vals):
    print("Proved that (A union B)' = A' intersection B'")
else:
    print("CANNOT BE PROVED HERE")

print("-----------------------------------------------------------")
print("To prove is (A intersection B)' = A' union B'")
AintB_c = [format(float(1.0 - i), ".1f") for i in AintB_vals]

AcuBc_vals = []
for i in range(len(set_A)):
    AcuBc_vals.append(max(A_c_vals[i], B_c_vals[i]))
print(" (A intersection B)' = ", AintB_c)
print("A' union B' = {}".format(AcuBc_vals))
if(AuB_c == AcintBc_vals):
    print("Proved that (A intersection B)' = A' union B'")
else:
    print("CANNOT BE PROVED HERE")

print("-----------------------------------------------------------")

# Support of A and B
Sup_A = []
for i in range(len(set_A)):
    if(set_A_ele[i] > 0):
        Sup_A.append(set_A_vars[i])
if(Sup_A == []):
    Sup_A.append("PHI")
print("Support of A is {}".format(Sup_A))

Sup_B = []
for i in range(len(set_B)):
    if(set_B_ele[i] > 0):
        Sup_B.append(set_B_vars[i])
if(Sup_B == []):
    Sup_B.append("PHI")
print("Support of B is {}".format(Sup_B))


# Core of A and B
Core_A = []
for i in range(len(set_A)):
    if(set_A_ele[i] == 1):
        Core_A.append(set_A_vars[i])
if(Core_A == []):
    Core_A.append("PHI")
print("Core of A is {}".format(Core_A))

Core_B = []
for i in range(len(set_B)):
    if(set_B_ele[i] == 1):
        Core_B.append(set_B_vars[i])
if(Core_B == []):
    Core_B.append("PHI")
print("Core of B is {}".format(Core_B))


# Height of A and B
print("Height of A is {}".format(max(set_A_ele)))
print("Height of B is {}".format(max(set_B_ele)))

# Cardinality of A and B
print("Cardinality of A is {}".format(sum(set_A_ele)))
print("Cardinality of B is {}".format(sum(set_B_ele)))

# Relative Cardinality of A and B
print("Relative Cardinality of A is " +
      str(format(sum(set_A_ele)/len(set_A_ele), ".2f")))
print("Relative Cardinality of B is " +
      str(format(sum(set_B_ele)/len(set_A_ele), ".2f")))

print("-----------------------------------------------------------")
alpha = float(
    input("Enter Alpha value for alpha cut and strong alpha cut[0-1] >>> "))
# Alpha Cuts of A and B
alpcut_A = []
for i in range(len(set_A)):
    if(set_A_ele[i] >= alpha):
        alpcut_A.append(set_A_vars[i])
if(alpcut_A == []):
    alpcut_A.append("PHI")
print("Alpha Cut of A({}) is {}".format(alpha, alpcut_A))

alpcut_B = []
for i in range(len(set_B)):
    if(set_B_ele[i] >= alpha):
        alpcut_B.append(set_B_vars[i])
if(alpcut_B == []):
    alpcut_B.append("PHI")
print("Alpha Cut of B({}) is {}".format(alpha, alpcut_B))


# Strong Alpha Cuts of A and B
alpcut_A = []
for i in range(len(set_A)):
    if(set_A_ele[i] > alpha):
        alpcut_A.append(set_A_vars[i])
if(alpcut_A == []):
    alpcut_A.append("PHI")
print("Strong Alpha Cut of A({}) is {}".format(alpha, alpcut_A))

alpcut_B = []
for i in range(len(set_B)):
    if(set_B_ele[i] > alpha):
        alpcut_B.append(set_B_vars[i])
if(alpcut_B == []):
    alpcut_B.append("PHI")
print("Strong Alpha Cut of B({}) is {}".format(alpha, alpcut_B))


# If the given set A and B are normal or subnormal
if(1.0 in set_A_ele):
    print("A is normal")
else:
    print("A is subnormal")
if(1.0 in set_B_ele):
    print("B is normal")
else:
    print("B is subnormal")
print("-----------------------------------------------------------")
