search_websource_dir = './websource/search.php'
login_websource_dir = './websource/login.php'

with open(search_websource_dir, 'r', encoding='utf-8') as search_file:
    search_content = search_file.read()
    print("search.php 내용:")
    print(search_content)

with open(login_websource_dir, 'r', encoding='utf-8') as login_file:
    login_content = login_file.read()
    print("\nlogin.php 내용:")
    print(login_content)
