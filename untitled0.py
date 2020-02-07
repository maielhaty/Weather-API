import requests
from flask import jsonify, request, Flask
import json

app = Flask(__name__)

key = "591e748d9025c6e9a0ac8fbb502a8d28"



@app.route("/temperature/", methods=['GET'])

def weather():
    """get user age by his name
    """
    country = request.args.get('country', default=None, type=str)
    if country:
        url = "https://api.openweathermap.org/data/2.5/weather?"
        params={
        "APPID": key,
        "q" : country
                }
        res = requests.get(url, params=params)
        res = json.loads(res.text)
        return res



if __name__ == "__main__":
    app.run(debug=True)


