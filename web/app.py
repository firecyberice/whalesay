from flask import Flask
from flask import Response
from docker import Client
import time


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
#            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance = Client(base_url='unix://var/run/docker.sock')
        return cls._instance


def getdocker(*args, **kwargs):
    request = kwargs['call']

    # from docker import Client
#        docker_obj = Client(base_url='unix://var/run/docker.sock')
    docker_obj = Singleton()
    created_container = docker_obj.create_container(
                                tty=True,
                                detach=True,
                                stdin_open=True,
                                image="firecyberice/whalesay",
                                command=request )

    docker_id = created_container.get("Id")
    time.sleep(1)
    docker_obj.start(docker_id)
    time.sleep(1)
    resultz = docker_obj.logs(docker_id)
    time.sleep(1)
    docker_obj.remove_container(docker_id)
#    resp = resultz.decode('ascii')
#    return resp
    return resultz


app = Flask(__name__)

@app.route('/message/<msg>')
def show_user_profile(msg):
    responsemsg = getdocker(call=msg)
    return Response(responsemsg, mimetype='text/plain')
#    return 'your message is '+msg

@app.route('/')
def hello_world():
    return "Please enter: /message/'your urlencoded message'"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
