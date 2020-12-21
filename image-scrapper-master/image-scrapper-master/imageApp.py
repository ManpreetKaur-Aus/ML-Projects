import os
from flask import Flask, render_template, request, jsonify
from searchAndDownload import search_and_download

#DRIVER_PATH = './chromedriver'
DRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
print(DRIVER_PATH)
app = Flask(__name__)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def image_scrapper_via_postman():
    if (request.method=='POST'):
        search_term=request.json['search_term']
        imgurls = search_and_download(search_term=search_term, driver_path=DRIVER_PATH)  # method to download images
        imgurls_str=str(list(imgurls))
        print("urls"+imgurls_str)
        return jsonify(imgurls_str)


port = int(os.getenv("PORT"))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
