"""
Input: s = "anagram", t = "nagaram"
Output: true
"""


def is_anagram(s, t):
    s_store, t_store = {}, {}
    if len(s) != len(t): return False
    for i in range(len(s)):
        s_store[s[i]] = 1 + s_store.get(s[i], 0)
        t_store[t[i]] = 1 + t_store.get(t[i], 0)
    return s_store == t_store


print(is_anagram("anagram", "nagaram"))
