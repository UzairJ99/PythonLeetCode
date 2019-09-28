class Solution:
    def uniqueMorseRepresentations(self, words):
        translator = {'a': ".-", 'b': "-...", 'c': "-.-.",'d': "-..",'e': ".", 'f': "..-.", 'g': "--.",'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",'l': ".-..",'m': "--",'n': "-.",'o': "---",'p': ".--.", 'q': "--.-",'r': ".-.",'s': "...",'t': "-",'u': "..-",'v': "...-",'w': ".--",'x': "-..-",'y': "-.--",'z': "--.."}
        
        morseCodes = []
        
        for word in words:
            morse = ""
            for letter in range(len(word)):
                if word[letter].isspace():
                    continue
                else:
                    morse += translator.get(word[letter])
            if (morse not in morseCodes) and (len(morse) > 0):
                morseCodes.append(morse)
        return len(morseCodes)