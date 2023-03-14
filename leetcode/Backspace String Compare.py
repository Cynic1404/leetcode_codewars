
# def backspaceCompare(s: str, t: str) -> bool:
#     def convert(s):
#         l = list(s)
#         counter = 0
#         while len(l)>counter:
#             if l[counter] == "#":
#                 if counter>0:
#                     del l[counter-1]
#                     del l[counter-1]
#                     counter-=1
#                 else:
#                     del l[counter]
#             else:
#                 counter+=1
#         return l
#     if convert(s)==convert(t):
#         return 1
#     else:
#         return 0
#
# print(backspaceCompare('axx#bb#c', 'axbd#c#c'))


def backspaceCompare(S, T):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)

    return build(S) == build(T)

print(backspaceCompare('axx#bb#c', 'axbd#c#c'))