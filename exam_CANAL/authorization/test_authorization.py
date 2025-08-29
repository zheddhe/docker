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


def test_user_alice_v1_access_ok():
    '''
    TEST 1 (utilisateur alice sur v1 autorisé)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params={
            'username': 'alice',
            'password': 'wonderland',
            'sentence': 'life is beautiful',
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
        Authorization test 1
    ============================

    request done at "/v1/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected result = 200;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_bob_v1_access_ok():
    '''
    TEST 2 (utilisateur bob sur v1 autorisé)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params={
            'username': 'bob',
            'password': 'builder',
            'sentence': 'life is beautiful',
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
        Authorization test 2
    ============================

    request done at "/v2/sentiment"
    | username="bob"
    | password="builder"
    | sentiment="life is beautiful"

    Expected result = 200;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_alice_v2_access_ok():
    '''
    TEST 3 (utilisateur alice sur v2 autorisé)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params={
            'username': 'alice',
            'password': 'wonderland',
            'sentence': 'life is beautiful',
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
        Authorization test 3
    ============================

    request done at "/v2/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected result = 200;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_bob_v2_access_ko():
    '''
    TEST 4 (utilisateur bob sur v2 non autorisé)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params={
            'username': 'bob',
            'password': 'builder',
            'sentence': 'life is beautiful',
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
        Authorization test 4
    ============================

    request done at "/v2/sentiment"
    | username="bob"
    | password="builder"
    | sentiment="life is beautiful"

    Expected result = 403;
    actual restult = {status_code}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def main():
    print("Lancement des tests directement avec python (sans pytest ni assert)")
    test_user_alice_v1_access_ok()
    test_user_bob_v1_access_ok()
    test_user_alice_v2_access_ok()
    test_user_bob_v2_access_ko()


if __name__ == "__main__":
    main()
