class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            count = len(word)
            encoded += str(count) + "#" + word
        return encoded     
    def decode(self, s: str) -> List[str]:
        decoded =[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            j+=1
            decoded.append(s[j:j+count])
            i = j + count
        return decoded    
