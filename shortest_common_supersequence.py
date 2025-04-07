class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        previous_row = [str2[0:j] for j in range(n + 1)]

        for i in range(1, m + 1):
            current_row = [str1[0:i]] + [None for _ in range(n)]

            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    current_row[j] = previous_row[j - 1] + str1[i - 1]
                else:
                    str1_option = previous_row[j]
                    str2_option = current_row[j - 1]

                    if len(str1_option) <= len(str2_option):
                        current_row[j] = str1_option + str1[i - 1]
                    else:
                        current_row[j] = str2_option + str2[j - 1]

            previous_row = current_row

        return previous_row[n]
