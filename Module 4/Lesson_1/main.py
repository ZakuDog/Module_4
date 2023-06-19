# def strcounter(s):  Решение за O(N ** 2)
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)


# def strcounter(s): # Решение за O(N * M)
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
#
# strcounter('abca')


def strcounter(s): # Решение за O(N + M)
    mydct = {}
    for sym in s:
        mydct[sym] = mydct.get(sym, 0) + 1

    for sym, count in mydct.items():
        print(sym, count)


strcounter('abca')
