class Solution:
    def countAndSay(self, n: int) -> str:
        return recursive_count_and_say("1", n)

def recursive_count_and_say(s, count):
    if count == 1:  # last number
        return s
    else:
        current_num = s[0]
        counter = 0
        s_out = ''
        for i in range(len(s)):
            if s[i] == current_num:
                counter += 1
            else:
                s_out += str(counter) + str(current_num)
                current_num = s[i]
                counter = 1
        s_out += str(counter) + str(current_num)
        return recursive_count_and_say(s_out, count - 1)