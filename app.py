from flask import Flask, render_template, Response
from pykafka import kafkaClient


def get_kafka_client():
    return kafkaClient(hosts='127.0.0.1:9092')




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
# consumer Api
@app.route('/topic/<topicname>')
def get_messsage(topicname):
    client = get_kafka_client()
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data:{o}\n\n'.format(i.value.decode('ascii'))
    return Response(events(), mimetype="text/event-stream")





if __name__ == '__main__':
    app.run(debug=True, port=5001)


