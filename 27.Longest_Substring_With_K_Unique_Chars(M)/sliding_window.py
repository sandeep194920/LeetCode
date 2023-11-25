class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        i, j = 0, 0
        maximum, count = -1, 0
        frequency = {}

        while j < len(s):

            frequency[s[j]] = frequency.get(s[j], 0) + 1
            if frequency[s[j]] == 1:
                count += 1

            if count < k:
                j += 1

            elif count == k:
                maximum = max(maximum, j - i + 1)
                j += 1

            elif count > k:
                while count > k:
                    frequency[s[i]] -= 1
                    if frequency[s[i]] == 0:
                        count -= 1
                    i += 1
                j += 1

        return maximum


# result = Solution().longestSubstring(s="aabacbebebe", k=3)
result = Solution().longestSubstring(
    s="hnxnounsapgerhquorqvplxnohltjuusticazitmwdyaxyxmdfziierhtbjpuohswfwcknticshuzoltcqffyoptyjcnfrfkavauceavhmjzdwdaquewtiidnkywpmecwkilefwsdwiqqmrlrnswnkzoqajkltetleapwbpiyorsbvbnupzrquvsaanojtjczkhxsmzuvydsqwwuhepytimcucmpzcooqlsrzonybiurawiplzyypiknbcwqokuqbhscozwhbswwcicqfiutryagpgpujgdnaxfgaekteqonegayfzhsyaawgidgtcteldnsgrzrecanhtyiueprgracdhxfhdofopwzodcljwyoiynxfpzdarnqljyaznfzqbqdwmvkqfauzrdqxsakjcjprlwzdjnhotgavhwlqnbeoryscfxzkpflhendmrbwybkfkacsniijuinooekrhhvlngkorxapsegsnxvtsgfliifeqvxtvjznhzfeszxjgqsufrbxsdclfrfhbpzuumyqrzycizvnbilwdtpmxxxplahclgpwcocnjemrncrjnlfjppapwqvbvfbcjlogpdfgmdtduymywjgmzwqhqnskinzosjgukkcqjztpkaaapqcsiofldfgrcfddaehxlddvfqfrngdunepshzpgeolvmjeeaibpwviuqvliwlueuvmbzbsrhvfrymslvqqzypevfaqiojbjaeixlsxrzklzhjnrvcgmgtwxgfyqacaciocfjmzrdfefobdlxdnkqtwvcetdstqjaxionfethglsxpvyubtesemqqnkgkqxpwecjajuasayaujqvipgolaaxwqvihkxowvtzpkxbgtvwkisjzxvvteiensnfublnfchptditogxpfchjqrvvoyu",
    k=14)
print(result)
