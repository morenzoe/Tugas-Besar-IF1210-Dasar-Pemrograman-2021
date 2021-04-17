from constant import user

# prosedur akhir
def login(databases):
        username = input("Ketik username : ")
        password = input("Ketik password : ")

        file = databases[user]

        for row in file:
                if row[1] == username:
                        if row[4] == password:
                                print("Login berhasil!")
                                databases.append(row)
                                return True
                        else:
                                print("Login gagal! Password salah.")
                                return False
                else:
                        print("Login gagal! Username salah.")
                        return False

        return databases
