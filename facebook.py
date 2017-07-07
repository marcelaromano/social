import requests
import simplejson
import codecs


# definicion de las funciones

def get_access_token():
    # pedir access token
    # este primero client id es mi id para usar la api
    client_id = '234693623606637'
    client_secret = '6382e55e8cffca1b1e4230089ea5ccd5'
    url_access_token = 'https://graph.facebook.com/oauth/access_token?%20client_id={}&client_secret={}&grant_type=client_credentials'.format(client_id, client_secret)
    response = requests.get(url_access_token)
    access_token = simplejson.loads(response.text)['access_token']
    return access_token


def get_posts_from_fanpage(page_id, access_token, next_url=None):
    # resonse.text  es un string el contenido de la repuesta... loads lo hace diccionario y de ahi los corchetes obtengo la clave accesos token
    # pedir el feed (muro) de posts de la pagina

    if next_url is None:
        url_feed = 'https://graph.facebook.com/v2.8/{}/feed?access_token={}'.format(page_id, access_token)
    else:
        url_feed = next_url

    response = requests.get(url_feed)

    # el request es lo que llama la info con la url feed que incorpora esos dos argumentos
    json = simplejson.loads(response.text)  # loads convierte el string de JSON a un diccionario de Python
    #post4_id = json['data'][3]['id']
    return json


def get_comments_from_post(post_id, access_token):
    # pedir los comments del post
    # https://graph.facebook.com/v2.8/121305961374091_688955347942480/comments?access_token=234693623606637|g37OnFOwJcnckcSvkayhfImOlTM
    url_comments = 'https://graph.facebook.com/v2.8/{}/comments?access_token={}'.format(post_id, access_token)
    response = requests.get(url_comments)
    json = simplejson.loads(response.text)
    return json


def save_comments_to_csv(comments, filename):
    archivo = codecs.open(filename, 'a', "utf-8")

    for comment_data in comments['data']:
        message = comment_data['message']
        date = comment_data['created_time']
        user_name = comment_data['from']['name']
        user_id = comment_data['from']['id']
        print('{} ({}, {}): {}'.format(user_name, user_id, date, message))

        linea = '{},{},{},{}\n'.format(user_id, user_name, date, message)
        archivo.write(linea)

    archivo.close()


# comienzo del programa principal, donde se llaman las funciones
access_token = get_access_token()
posts = get_posts_from_fanpage('cocacolaar', access_token)
post4_id = posts['data'][3]['id']
# posts = get_posts_from_fanpage('pepsi', access_token)
# posts = get_posts_from_fanpage('cocacolaar', access_token)

comments_post4 = get_comments_from_post(post4_id, access_token)
save_comments_to_csv(comments_post4, 'facebook_comments.csv')

# recorrer todos los posts (primeros 25) y obtener los comentarios de cada uno de ellos
print('------------')
for post in posts['data']:
    print(post['message'])

    post_id = post['id']
    comments = get_comments_from_post(post_id, access_token)

    for comment in comments['data']:
        print(' - ' + comment['message'])

    save_comments_to_csv(comments, 'facebook_comments.csv')

next_url = posts['paging']['next']
posts = get_posts_from_fanpage('cocacolaar', access_token, next_url)

        # accedo a data , luego al cuarto elem por ej que es el que tine el comentario y luego le saco el id
#https://graph.facebook.com/v2.8/onlyforluxurylifestyle/feed?access_token=234693623606637|g37OnFOwJcnckcSvkayhfImOlTM
# esto recorro primero y luego



# comment_data:
# {
#     "created_time": "2017-01-10T14:11:11+0000",
#     "from": {
#         "name": "Natali  Hricheva",
#         "id": "1060343614077727"
#     },
#     "message": "\u041a\u0440\u0443\u0442\u043e\ud83d\ude0d\ud83d\ude0d\ud83d\ude0d",
#     "id": "688955347942480_689266391244709"
# },


    # next_url = comments_post4['paging']['next']
    # print('Next: {}'.format(next_url))
    # response = requests.get(next_url)
    # print(response.text)

    # aca sacamos el id de la posicion 4.... pero habria que hacerlo para todos los posts.
# ghasta aca llegamos
        # https://developers.facebook.com/apps/234693623606637/settings/
#graph.facebook.com/v2.8/121305961374091_688955347942480/comments?access_token=234693623606637|g37OnFOwJcnckcSvkayhfImOlTM
#https://graph.facebook.com/oauth/access_token?%20client_id=234693623606637&client_secret=6382e55e8cffca1b1e4230089ea5ccd5&grant_type=client_credentials
#https://graph.facebook.com/oauth/access_token?%20client_id=234693623606637&client_secret=6382e55e8cffca1b1e4230089ea5ccd5&grant_type=client_credentials
#https://developers.facebook.com/docs/graph-api/reference
#http://stackoverflow.com/questions/12948809/trying-to-get-app-access-token
#https://www.facebook.com/pg/onlyforluxurylifestyle/posts/
#http://stackoverflow.com/questions/12065492/rest-api-for-website-which-uses-facebook-for-authentication