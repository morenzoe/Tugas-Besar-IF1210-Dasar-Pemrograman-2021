from constant import user

# prosedur akhir
def login(databases):
        username = input("Ketik username : ")
        password = input("Ketik password : ")

        file = databases[user]

        for row in file:
                if row == [username,password]:
                        print("Login berhasil!")
                        return True
                else:
                        print("Login gagal! Username atau password salah.")
                        return False

        return databases