while True:
    input_height = float(input("Введите рост тела, см: "))
    if input_height == float("999"):
        break
    else:
        input_veight = float(input("Введите вес тела, кг: "))
        input_sex = input("Введите ваш пол, m/f: ")
        input_age = float(input("Введите ваш возраст, лет: "))
        bmi_value = round(input_veight/((input_height*0.01)**2))
        print("Ваш имт составляет ", bmi_value, " едениц")
        f = ["=", "=", "=", "=", "=", "=", "=", "=", "="]
        i = (round((bmi_value-20)/3))-1
        f[i] = "|"
        h = " ".join(f)
        print("20", h, "50")
        if bmi_value < 30:
            if input_age <= 30:
                if input_sex == "m":
                    print("Секс наркотики и рокнрол")
                else:
                    if input_sex == "f":
                        print("Секс наркотики и рокнрол, макияж")
            else:

                if input_age <= 60 and input_age > 30:
                    if input_sex == "m":
                        print("Секс наркотики и рокнрол, танометр")
                    else:
                        if input_sex == "f":
                            print("Секс наркотики и рокнрол, макияж, танометр")
                else:
                    if input_age > 60:
                        if input_sex == "m":
                            print("Секс наркотики и рокнрол, танометр, валидол")
                        else:
                            if input_sex == "f":
                                print("Секс наркотики и рокнрол, макияж, танометр, валидол")
        else:
            if bmi_value < 40 and bmi_value > 30:
                if input_age <= 30:
                    if input_sex == "m":
                        print("Ты  толстенький, похудей, а потом Секс наркотики и рокнрол")
                    else:
                        if input_sex == "f":
                            print("Ты  толстенькая, похудей, а потом Секс наркотики и рокнрол, макияж")
                else:
                    if input_age <= 60 and input_age > 30:
                        if input_sex == "m":
                            print("Ты  толстенький, похудей, а потом Секс наркотики и рокнрол, танометр")
                        else:
                            if input_sex == "f":
                                print("Ты  толстенькая, похудей, а потом Секс наркотики и рокнрол, макияж, танометр")
                    else:
                        if input_age > 60:
                            if input_sex == "m":
                                print("Ты  толстенький, похудей, а потом Секс наркотики и рокнрол, танометр, валидол")
                            else:
                                if input_sex == "f":
                                    print("Ты  толстенькая, похудей, а потом Секс наркотики и рокнрол, макияж, танометр, валидол")
            else:
                if bmi_value > 40:
                    if input_age <= 30:
                        if input_sex == "m":
                            print("Ты хряк, быстрей худей, а потом Секс наркотики и рокнрол")
                        else:
                            if input_sex == "f":
                                print("Ты хрюша, быстрей худей, а потом Секс наркотики и рокнрол, макияж")
                    else:

                        if input_age <= 60 and input_age > 30:
                            if input_sex == "m":
                                print("Ты хряк, быстрей худей, а потом Секс наркотики и рокнрол, танометр")
                            else:
                                if input_sex == "f":
                                    print("Ты хрюша, быстрей худей, а потом Секс наркотики и рокнрол, макияж, танометр")
                        else:
                            if input_age > 60:
                                if input_sex == "m":
                                    print("Ты хряк, быстрей худей, а потом Секс наркотики и рокнрол, танометр, валидол")
                                else:
                                    if input_sex == "f":
                                        print("Ты хрюша, быстрей худей, а потом Секс наркотики и рокнрол, макияж, танометр, валидол")

# Доделать BMI:
# Дозапросить пол и возраст
# Выдавать рекомендации
# 10 градаций:
# 2 пола и по 3 рекомендаци для каждого + возраст
