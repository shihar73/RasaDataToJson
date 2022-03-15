import json

# nlu.yml to CBT_intent.json
data = {}
intent= ""
intent_list = []
with open("nlu.yml", "r", encoding='utf-8') as f :
    for i, line in enumerate(f, 1):
        if line[:9] == "- intent:":
            
            if intent != "":
                data[intent] = intent_list

            intent_list = []
            intent = line[10:]
            

        elif line[:11] == "  examples:":
            pass
        else:
            intent_list.append(line[6:])
        

        if i == 9752:
            data[intent] = intent_list 
            break


with open("CBT_intent.json", "w", encoding='utf-8') as i:
    json.dump(data, i)



# domain.yml to CBT_response.json
data = {}
intent= ""
intent_list = []
img = False
with open("domain.yml", "r", encoding='utf-8') as f :
    for i, line in enumerate(f, 1):
        if line[:8] == "  utter_":
            
            if intent != "":
                data[intent] = intent_list

            intent_list = []
            intent = line[2:-2]
            
        elif line[:9] == "  - text:":
           intent_list.append(line[9:])
            
        elif line[:10] == "  - image:" or line[:9] == "    text:":
            if line[:10] == "  - image:" :
                image = line[11:]
                
            else:
                text = line[10:]
                img = True

            if img:
                img_dic = {
                    "image": image,
                    "text": text
                }
                intent_list.append(img_dic)
                img =False
        

        if i == 317:
            data[intent] = intent_list 
            break


with open("CBT_response.json", "w", encoding='utf-8') as i:
    json.dump(data, i)