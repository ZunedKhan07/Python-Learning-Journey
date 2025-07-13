# Dist. almost same as object.
# they are unordered, mutable(changable) and dublicate key not allow



# marks = {};

# a = int(input("Enter you phy marks : "));
# b = int(input("Enter you chem marks : "));
# c = int(input("Enter you math marks : "));

# marks.update({"phy" : a})
# marks.update({"chem" : b})
# marks.update({"math" : c})

# print(marks);



# 🟢 Sets
#  set is the collection of unique element
# set is mutaable but set each element is immutable and unique

# lang = ["python", "java", "js", "C"];
# print(lang.pop())
# print(lang.pop())

# set1 = {1, 2, 3};
# set2 = {3, 4, 5};

# print(set1.union(set2));
# print(set1.intersection(set2));

# coll = set()

# coll.add(1);
# coll.add(2);
# coll.add(3);
# coll.add(4);
# coll.add("Software");
# coll.add((7, 8, 9));
# # coll.add([4, 7, 6]); #this is not allowed because lists are  mutables

# print(coll);

# coll.remove(1)
# print(coll)

# coll.clear()
# print(coll);



# collection = {}; # empty dict
# collection = {}; # empty sets



# 🟢 Dictionary
# # nested dict
# student = {
#     "name" : "Zuned Khan",
#     "marks" : {
#         "maths" : 97,
#         "phy" : 93,
#         "chem" : 90
#     }
# }

# print(student["marks"]["maths"]);
# print(student.keys());
# print(student.values());
# print(student.items());
# print(student.get("marks"));
# student.update({"city" : "jaipur"})
# print(student);



# dict = {
#     "name" : "Juned Khan",
#     "cgpa" : 8.2,
#     "Subj" : ["python", "Java", "JS"]
# }

# print(dict["name"])
# print(dict["cgpa"])
# dict["name"] = "Zuned";
# print(dict)