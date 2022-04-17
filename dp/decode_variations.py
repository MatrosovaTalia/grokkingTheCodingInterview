def decodeVariations(S):
    def count_mappings(n, s):
        if s[0] == '0':
            return 0

        if len(s) == 1 or len(s) == 0:
            return len(s)

        # if len(s) == 2:
        #     if int(s) > 26 or :
        #         return 0

        one_prev, two_prev = 1, 1
        cur = one_prev
        for i in range(1, len(s)):
            if s[i] == "0":
                if 0 < int(s[i - 1:i + 1]) <= 20:
                    cur = two_prev
                else:
                    return 0
            elif int(s[i - 1:i + 1]) <= 26:
                cur = two_prev + 1
            else:
                cur = one_prev
            two_prev = one_prev
            one_prev = cur

        return cur

                







        # "0" -> 0
        # "23701" -> 1 2 2 ret 0
        # "21201" -> 1 2 3 2 2 
        # "23201" -> 1 2 3 2 2 
        # "23200"
        # "2012" -> 
        # 1 2 
        # 2 3 20 1
        # 23 20 1

print(decodeVariations("26"))