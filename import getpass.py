import getpass

def reset_program():
    print("\u0d94\u0db6\u0dd9\u0d9c\u0dca \u0dc0\u0dd2\u0dc1\u0dd9\u0dc2 \u0d85\u0dc0\u0dc3\u0dbb \u0db8\u0dad \u0db8\u0db8 \u0dc0\u0da9\u0dca\u0dc3\u0da7\u0dbb\u0dd4\u0dc3\u0db1 \u0db1\u0dc0\u0dad \u0d95\u0dd1\u0dc3\u0dd2 \u0d95\u0dbb\u0dd9\u0dcf \u0dbb\u0d9a\u0dcf\u0dc3\u0dbb\u0dca\u0dc2\u0dd9\u0dc3\u0da7.")

def authenticate():
    correct_password = "Sani2005"
    attempts = 3

    while attempts > 0:
        password = getpass.getpass("\u0d9a\u0dbb\u0dd4\u0db1\u0dcf\u0d9a\u0dbb \u0db8\u0dd6\u0dbb\u0db4\u0daf\u0dba \u0d87\u0db8\u0dd9\u0db8\u0dba\u0db1\u0dd2: ")
        if password == correct_password:
            print("\u0dc3\u0dcf\u0dbb\u0dca\u0dad\u0dcf\u0d9a \u0db4\u0dd2\u0dc0\u0dd2\u0dc3\u0dd6\u0db8\u0dcf\u0db1\u0dca \u0dc3\u0dd2\u0dad\u0dd4 \u0dc0\u0dd2\u0dba!")
            reset_program()
            return
        else:
            attempts -= 1
            print(f"\u0dc0\u0dd9\u0dbb\u0dc3\u0dd2 \u0db8\u0dd6\u0dbb\u0db4\u0daf\u0dba\u0dba. \u0d89\u0dca\u0d9a\u0dd3\u0dbb\u0dd2 \u0d89\u0db3\u0dc4\u0dca\u0dc3\u0dcf\u0dc4 {attempts} \u0dba\u0dd2.")
    
    print("\u0d89\u0dcf\u0daf\u0dd2\u0dba \u0dc3\u0dd0\u0db8\u0dca\u0db4\u0dd4\u0dbb\u0dca\u0dc3\u0d9c\u0dd4\u0db8. \u0dc0\u0dad\u0d85\u0dc0\u0dc3\u0db1 \u0d9a\u0dd0\u0dbb\u0db8\u0dd2\u0dc3\u0dba.")
    return

if __name__ == "__main__":
    print("\u0d85\u0db4\u0dca\u0d9c\u0dca\u0db8\u0dcf\u0dbb \u0db4\u0dd2\u0db1\u0dca\u0dad\u0dd4\u0dbb \u0dbb\u0db4\u0dd2\u0dc3\u0dca\u0dc3\u0dcf\u0db1 \u0dc1\u0dbb\u0dcf \u0db8\u0dd9\u0d9a\u0dd2\u0dc0\u0db8\u0dd4 \u0dc3\u0dc0\u0d9a\u0dbb\u0dcf\u0db1\u0dca\u0db8\u0dc0\u0dcf \u0db4\u0dd2\u0dc5\u0dba!")
    authenticate()
