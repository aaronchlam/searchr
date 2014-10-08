import random
import requests
import os
from flask import Flask, render_template, request, abort, redirect, url_for
app = Flask(__name__, instance_relative_config = True)

app.config.from_object('config')

flickr_params = {'api_key': os.environ['FLICKR_API_KEY'],
                 'method': 'flickr.photos.search',
                 'format': 'json', 'nojsoncallback': '1',
                 'page':  '1', 'per_page': '100'}

photo_url = 'https://farm%d.staticflickr.com/%s/%s_%s.jpg'

@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html', img_url = None, search_term = 'Search Flickr...')

  search_term = str(request.form['search-term'])
  search_params = flickr_params.copy()
  search_params['text'] = search_term
  search_params['tag'] = search_term

  response = requests.get(app.config['FLICKR_API_URL'], params = search_params)
  r_json = response.json()
  if r_json['stat'] != 'ok':
    abort(406)
  rand_photo = random.choice(r_json['photos']['photo'])
  rand_url = photo_url % (rand_photo['farm'],
                          rand_photo['server'],
                          rand_photo['id'],
                          rand_photo['secret'])
  return render_template('index.html', img_url = rand_url, search_term = search_term)

if __name__ == '__main__':
  app.run(debug = True)
