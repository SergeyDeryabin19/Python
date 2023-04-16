all_dict={}
# print(all_dict, type(all_dict))
def create_new_person():
    global all_dict
    new_key= len(all_dict)+1
    input_height = float(input("Введите рост тела, см: "))
    input_veight = float(input("Введите вес тела, кг: "))
    name_of_person = input("Введите имя пользователя: ")
    input_sex = input("Введите ваш пол, m/f: ")
    input_age = float(input("Введите ваш возраст, лет: "))
    bmi_value = round(input_veight/((input_height*0.01)**2))
    print("Ваш имт составляет ", bmi_value, " едениц")
    all_dict.update({name_of_person:{"height":input_height,"weight":input_veight,"sex":input_sex,"age":input_age,"bmi":bmi_value}})
    
    return all_dict   #можно не писать

# data_cal_bme[nomer_next_key+1] = {new_name:{"height": new_height, "weight": new_weight, "gender": new_gender, "age": new_age}}

create_new_person()
create_new_person()

create_new_person()


for item in all_dict:
    print(item)