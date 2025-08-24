from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

# 准备数据并直接传递给模板
@app.route('/')
def index():
    r=requests.get('https://api.tanshuapi.com/api/toutiao/v1/index?key=c4d35ff2c83c9a3b840482b2b042d617&type=头条&num=5&start=0')
    r.endoding='utf-8'
    news_json=json.loads(r.text)
    news_data=news_json["data"]["list"]
    return render_template('index.html', data=news_data)

if __name__ == '__main__':
    app.run(debug=True)