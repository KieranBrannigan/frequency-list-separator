import json

import packages.jieba.posseg as pseg


def get_flag(word):
    return list(pseg.cut(word))[0].flag
    

def translate_flag(flag):
    "convert all the weird letter-code labels from ictclas into the ones we care about or 'other'"

    name = ['nr','nr1','nr2','nrj','nrf','ns','nsf','nt','nz','nl','ng']
    time = ['t','tg']
    verb = ['v','vd','vn','vshi','vyou','vf','vx','vi','vl','vg']
    adjective = ['a','ad','an','ag','al']
    other = ['b','bl','z']
    pronoun = ['r','rr','rz','rzt','rzs','rzv','ry','ryt','rys']

    if flag == 'n':
        return 'noun'
    elif flag == 's':
        return 'place'
    elif flag == 'f':
        return 'direction'
    elif flag in verb:
        return 'verb'
    elif flag in name:
        return 'name'
    elif flag in time:
        return 'time'
    elif flag in adjective:
        return 'adjective'
    elif flag in pronoun:
        return 'pronoun'
    elif flag in other:
        return 'other'
    else:
        print(flag)
        with open('other_labels.json','r') as ReadFile:
            content = json.loads(ReadFile.read())
        if flag not in content:
            content.append(flag)
            with open('other_labels.json','w') as OutFile:
                OutFile.write(json.dumps(content))
        

output = []
with open('frequency.json','r', encoding='utf-8') as ReadFile:
    r = ReadFile.read()
    content = json.loads(r,)
    for idx, word in enumerate(content):
        flag = translate_flag(get_flag(word))
        output.append([word,flag])

        if idx % 100 == 0:
            print(f"{(idx/len(content)) *100} % finished")

    print("finished")
with open('frequency_with_tokens.json','w', encoding='utf-8') as WriteFile:
    json.dump(output,WriteFile, ensure_ascii=False)