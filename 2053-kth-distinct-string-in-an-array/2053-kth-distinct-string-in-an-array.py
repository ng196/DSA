class Solution(object):
    def kthDistinct(self, arr, k):
        unique_lst = []
        nolst = set()
        ls = len(arr)

        for i in range(ls):
            if arr[i] in nolst:
                continue

            is_unique = True
            for j in range(ls):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    nolst.add(arr[i])
                    is_unique = False
                    break

            if is_unique:
                unique_lst.append(arr[i])

        if k <= len(unique_lst):
            return unique_lst[k - 1]
        else:
            return ""
