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


def test_user_alice_v1_sentiment_positif():
    '''
    TEST 1 (utilisateur alice sentiment positif sur v1)
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
    if status_code != 200:
        test_status = 'FAILURE'
        score_display = 'N/A (HTTP != 200)'
    else:
        # on parse le JSON et on lit le score
        data = r.json()
        score = float(data.get("score"))
        test_status = 'SUCCESS' if score >= 0 else 'FAILURE'
        score_display = score
    # construction de l'output du résultat
    output = f'''
    ============================
        Content test 1
    ============================

    request done at "/v1/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected score = Positif (>= 0)
    actual score = {score_display}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_alice_v1_sentiment_negatif():
    '''
    TEST 2 (utilisateur alice sentiment negatif sur v1)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params={
            'username': 'alice',
            'password': 'wonderland',
            'sentence': 'that sucks',
        }
    )
    # traduction du statut de la requête en statut de test
    status_code = r.status_code
    if status_code != 200:
        test_status = 'FAILURE'
        score_display = 'N/A (HTTP != 200)'
    else:
        # on parse le JSON et on lit le score
        data = r.json()
        score = float(data.get("score"))
        test_status = 'SUCCESS' if score < 0 else 'FAILURE'
        score_display = score
    # construction de l'output du résultat
    output = f'''
    ============================
        Content test 2
    ============================

    request done at "/v1/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected score = Negatif (< 0)
    actual score = {score_display}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_alice_v2_sentiment_positif():
    '''
    TEST 3 (utilisateur alice sentiment positif sur v2)
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
    if status_code != 200:
        test_status = 'FAILURE'
        score_display = 'N/A (HTTP != 200)'
    else:
        # on parse le JSON et on lit le score
        data = r.json()
        score = float(data.get("score"))
        test_status = 'SUCCESS' if score >= 0 else 'FAILURE'
        score_display = score
    # construction de l'output du résultat
    output = f'''
    ============================
        Content test 3
    ============================

    request done at "/v2/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected score = Positif (>= 0)
    actual score = {score_display}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def test_user_alice_v2_sentiment_negatif():
    '''
    TEST 4 (utilisateur alice sentiment negatif sur v2)
    '''
    # requête du test
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params={
            'username': 'alice',
            'password': 'wonderland',
            'sentence': 'that sucks',
        }
    )
    # traduction du statut de la requête en statut de test
    status_code = r.status_code
    if status_code != 200:
        test_status = 'FAILURE'
        score_display = 'N/A (HTTP != 200)'
    else:
        # on parse le JSON et on lit le score
        data = r.json()
        score = float(data.get("score"))
        test_status = 'SUCCESS' if score < 0 else 'FAILURE'
        score_display = score
    # construction de l'output du résultat
    output = f'''
    ============================
        Content test 4
    ============================

    request done at "/v2/sentiment"
    | username="alice"
    | password="wonderland"
    | sentiment="life is beautiful"

    Expected score = Négatif (< 0)
    actual score = {score_display}

    ==>  {test_status}

    '''
    # consignation du résultat
    _print_result(output)


def main():
    print("Lancement des tests directement avec python (sans pytest ni assert)")
    test_user_alice_v1_sentiment_positif()
    test_user_alice_v1_sentiment_negatif()
    test_user_alice_v2_sentiment_positif()
    test_user_alice_v2_sentiment_negatif()


if __name__ == "__main__":
    main()
