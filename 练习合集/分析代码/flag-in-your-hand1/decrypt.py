#  var a = [118, 104, 102, 120, 117, 108, 119, 124, 48,123,101,120];
#     if (s.length == a.length) {
#         for (i = 0; i < s.length; i++) {
#             if (a[i] - s.charCodeAt(i) != 3)
#                 return ic = false;
#         }
#         return ic = true;
#     }

a = [118, 104, 102, 120, 117, 108, 119, 124, 48,123,101,120]
s = []
for i in a:
    e = i - 3
    s.append(chr(e))
tag = "".join(s)
print(tag)

# security-xbu
