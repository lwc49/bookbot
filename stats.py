def get_word_num(text):
    splited_contents=text.split()
    return len(splited_contents)
    
def character_counter(text):
    character_count={}
    for character in text:
        lowercase=character.lower()
        if lowercase in character_count:
            character_count[lowercase]+=1
        else:
            character_count[lowercase]=0
    return character_count
            
        