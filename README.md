# Searchr
Searches and displays a random photo from Flickr according to user input.

Check out the app live on http://searchr-uoft.herokuapp.com

## Local Deploy

### Requirements
* Python 2.7
* pip

### Instructions

1. Install packages according to `requirements.txt`
2. Assign your Flickr API Key to the environmental variable `FLICKR_API_KEY`
3. Run the app.
```
  pip install -r requirements.txt
  export FLICKR_API_KEY=<your flickr api key here>
  python searchr.py
```
Visit `127.0.0.1:5000` on your favourite web browser and enjoy!
