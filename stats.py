def get_word_num(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        splited_contents=file_contents.split()
        counter=0
        for splited_content in splited_contents:
            counter+=1
        return counter
    
def character_counter(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        lowercase_contents=file_contents.lower()
        splited_contents=lowercase_contents.split()
        character_count={}
        for splited_content in splited_contents:
            for character in splited_content:
                character_count[character]=0
        for key in character_count.keys():
            for splited_content in splited_contents:
                for character in splited_content:
                    if character == key:
                        character_count[key]+=1
        return character_count
            
        