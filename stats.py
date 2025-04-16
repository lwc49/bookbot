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
            character_count[lowercase]=1
    return character_count

def sort_on(dict):
    return dict["num"]

def sorting(character_count):
    sorted_list=[]
    for key, value in character_count.items():
        d={}
        d["name"]=key
        d["num"]=value
        sorted_list.append(d)
    sorted_list.sort(reverse=True, key=sort_on)


    return sorted_list
                
        