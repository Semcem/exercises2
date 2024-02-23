def user_choice():
    number = input("""Lütfen devam etmek için işlem seçiniz.
            1.Uygulama
            2.Uygulama
            3.Parola Değiştir
            4.Çıkış Yap """)
    if number == "1":
        return ("Uygulama 1")
    elif number == "2":
        return ("Uygulama 2")
    elif number == "3":
        return change_password()
    elif number == "4":
        print("Çıkış yapıldı.")
        return input("Kullanıcı adını giriniz: ")

def change_password():
    password = input("Lütfen güncel şifrenizi giriniz: ")
    if login_password == password:
        new_password = input("kompleks şifrenizi giriniz: ")
        np_count = 2
        while np_count > 0:
            if new_password.isalnum():
                new_password = input("""Lütfen özel karakter'*/@-?!' içeren yeni şifrenizi oluşturun.""")
                np_count -= 1
            else:
                new_password_verification = input("Yeni parolayı tekrar giriniz: ")
                if new_password_verification == new_password:
                    new_user_info_dict.pop(login_username)
                    new_user_info_dict.update({login_username:new_password})
                    print("Yeni şifreniz:", new_password, "olarak değişti.")
                    np_count = 0
                else :
                    new_password = input("""Lütfen özel karakter'*/@-?!' içeren yeni şifrenizi oluşturun.""")
    return user_choice()

user_info_dict = {"sema1": "sifre1", 
                  "username2": "userpass2",
                  "username3": "userpass3" }

new_user_info_dict = user_info_dict.copy()

login_username = input("Kullanıcı adını giriniz: ")

if login_username.lower() == "q":
    print("Çıkış yapıldı.")
    
elif login_username in user_info_dict.keys():
    login_password = input("Şifrenizi giriniz: ")
    
    password_attempt = 2    
    while password_attempt > 0 :
        if login_password == user_info_dict.get(login_username):
            user_choice()
            password_attempt = 0
        else:
            print("yanlış şifre girdiniz, kalan hak:", password_attempt)
            login_password = input("Şifrenizi giriniz: ")
            password_attempt -= 1 
            if password_attempt == 0:
                print("sistemden çıkış yapıldı.")
    
else:
    print("Sistemde olmayan bir kullancı girdiniz. Lütfen sayfayı yenileyip tekrar deneyin.") 
    