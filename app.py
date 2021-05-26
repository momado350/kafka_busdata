from flask import Flask, render_template, Response
from pykafka import kafkaClient


def get_kafka_client():
    return kafkaClient(hosts='127.0.0.1:9092')




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True, port=5001)


