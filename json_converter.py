# def numtostringconverter(input_string, num_to_replace):
#     if num_to_replace and type(num_to_replace) is not int:
#         return "Not Possible !!!"
#     splitter = '{'+ str(num_to_replace) +'}'
#     before_splitter = '{'+ str(num_to_replace-1) +'}'
#     # print(splitter, before_splitter)
#     arrs = input_string.split(splitter)
#     print("---->",arrs)
#     start_string = arrs[0]
#     arrs[0] = arrs[0].split(before_splitter)[-1]
#     end_string = arrs.pop()
#     if '{' not in start_string:
#         start_string = ''
#     formmatted_string = ''.join(
#         [element*(num_to_replace+1) for element in arrs]
#     )
#     final_string = '{}{}{}'.format(
#         start_string,
#         formmatted_string,
#         end_string
#     )
#     # print(arrs, start_string, end_string)
#     print("Input: {}, NumtoReplace: {}, Output: {}".format(
#         input_string,
#         num_to_replace,
#         final_string
#     ))
#
# numtostringconverter('acw{1}wd{1}f{1}wsd{2}zzz{2}qwe{3}', 2)
# # numtostringconverter('acw{1}wd{1}f{1}wsd{2}zzz{2}qwe{3}', 2)
# # numtostringconverter('acw{1}wd{1}f{1}wsd{2}zzz{2}qwe{3}sdsf', 3)
# # numtostringconverter('acw{1}wd{1}f{1}wsd{2}zzz{2}qwe{3}', -1)
# # numtostringconverter('acw{1}wd{1}f{1}wsd{2}zzz{2}qwe{3}', 0)
#
#
# # def check_mirror_image(root):
# #     def helper(l, r):
# #         if not l and not r:
# #             return True
# #         if not l or not r:
# #             return False
# #         return l.val == r.val and helper(l.right, r.left) and helper(l.left, r.right)
# #
# #     return helper(root, root)
#
# # try:
# #     print("In Try")
# #     a = 1/0
# # except Exception as e:
# #     print(e, "In except")
# # else:
# #     print("In Else")
# # finally:
# #     print("In finally")



import base64
for i in range(100):

    print(base64.b64encode(str(i).encode('utf-8')))
