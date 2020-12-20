import falcon
import json
import urllib
import requests
from falcon_cors import CORS

SCORE_CUTOFF = -0.7
MAGNITUDE_CUTOFF = 0.7

SENTINEL_PORT = '8000'
REDDIT_SCRAPER_PORT = '8080'
DATABASE_PORT = '8000'

SENTINEL_URL = 'http://localhost:' + SENTINEL_PORT
REDDIT_SCRAPER_URL = 'http://localhost:' + REDDIT_SCRAPER_PORT
DATABASE_URL = 'http://localhost:' + DATABASE_PORT

class ContentResource(object):

    def on_get(self, req, resp):
        test = '{"source": "https://old.reddit.com/r/doggos/comments/kg7a3s/never_let_your_dog_eat_skittles/"}'
        bad_subjects = []
        # analysis = get_analysis(content_node, bad_subjects)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        content_node = scrape(req)
        bad_subjects = []
        get_analysis(content_node, bad_subjects)
        response = {'content': content_node, 'bad_subjects': bad_subjects}
        resp.body = json.dumps(response)
        resp.status = falcon.HTTP_200


# Check the database
def check_resource(req):
    pass


# Send to scraper
def scrape(req):
    data = req.media['source']
    com = data.find('.com') + 5
    trimmed_url = data[com:]
    uri = urllib.parse.urlencode({'uri': trimmed_url})
    return requests.get(REDDIT_SCRAPER_URL + '/content?' + uri).json()


# Get sentiment analysis
def get_analysis(node, bad_subjects):
    process_node(node, bad_subjects)
    if not node['children']:
        pass
    else:
        # process children
        if type(node['children']) == dict:
            node['children'] = [node['children']]


        if len(node['children']) > 5:
            node['children'] = node['children'][:5]
            
        for child in node['children']:
            get_analysis(child, bad_subjects)


def process_node(node, bad_subjects):
    resp = requests.post(SENTINEL_URL + '/sentiment', data={ 'content': node['name'] + node['body'] }).json()
    # resp = {
    #     'naughty': 'False',
    #     'subjects': [
    #         {
    #             'name': 'test',
    #             'score': '-1',
    #             'magnitude': '1'
    #         }
    #     ]
    # }
    naughty = resp['naughty']
    node['sentiment'] = {}
    node['sentiment']['naughty'] = naughty
    node['sentiment']['subjects'] = resp['subjects']
    if naughty:
        for subject in node['sentiment']['subjects']:
            if float(subject['score']) < SCORE_CUTOFF and float(subject['magnitude']) > MAGNITUDE_CUTOFF:
                added = False
                for bad_subject in bad_subjects:
                    if subject['name'] == bad_subject['name']:
                        bad_subject['score'] = str((float(bad_subject['score']) + float(subject['score']))/2)
                        bad_subject['magnitude'] = str((float(bad_subject['magnitude']) + float(subject['magnitude']))/2)
                        added = True
                        break
                if not added:
                    bad_subjects.append(subject)


api = application = falcon.API(
    middleware=[
                CORS(
                    allow_all_origins=True,
                    allow_all_headers=True,
                    allow_all_methods=True,
                ).middleware,
            ])

content = ContentResource()
api.add_route('/api/analyse', content)
print("review service on")
