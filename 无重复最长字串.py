def lengthOfLongestSubstring(s):
        dic = {}              #定义可查询的字典，当新来的字符进来的时候，会推入字典中并更新里面的值
        max_length = 0
        start = 0             #start是不重复字串的开头，遇到跟前面字符相同时，会跳到下个字符
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]]+1                        
            else:
                max_length = max(max_length,i-start+1)
            dic[s[i]] = i
        return max_length
