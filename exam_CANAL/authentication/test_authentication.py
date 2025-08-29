import os
import requests

# définition de l'adresse de l'API depuis la variable d'environnement
api_address = os.environ.get('API_ADDRESS')
# port de l'API depuis la variable d'environnement
api_port = os.environ.get('API_PORT')


def _print_result(output):
    # affichage du résultat en sortie standard
    print(output)
    # impression dans un fichier si demandé par variable d'environnement
    if os.environ.get('LOG') == "1":
        with open('logs/api_test.log', 'a') as file:
            file.write(output)


def test_user_alice_password_ok():
    '''
    TEST 1 (utilisateur alice avec mot de passe correct)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': 'alice',
            'password': 'wonderland'
        }
    )
    # traduction du statut de la requête en statut de test
    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    # construction de l'output du résultat
    output = f'''
    ============================
        Authentication test 1
    ============================

    request done at "/permissions"
    | username="alice"
    | password="wonderland"

    Expected result = 200;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_bob_password_ok():
    '''
    TEST 2 (utilisateur bob avec mot de passe correct)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': 'bob',
            'password': 'builder'
        }
    )
    # traduction du statut de la requête en statut de test
    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    # construction de l'output du résultat
    output = f'''
    ============================
        Authentication test 2
    ============================

    request done at "/permissions"
    | username="bob"
    | password="builder"

    Expected result = 200;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_clementine_password_ko():
    '''
    TEST 2 (utilisateur clementine avec mot de passe incorrect)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': 'clementine',
            'password': 'mandarine'
        }
    )
    # traduction du statut de la requête en statut de test
    status_code = r.status_code
    if status_code == 403:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    # construction de l'output du résultat
    output = f'''
    ============================
        Authentication test 3
    ============================

    request done at "/permissions"
    | username="clementine"
    | password="mandarine"

    Expected result = 403;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def main():
    print("Lancement des tests directement avec python (sans pytest ni assert)")
    test_user_alice_password_ok()
    test_user_bob_password_ok()
    test_user_clementine_password_ko()


if __name__ == "__main__":
    main()
