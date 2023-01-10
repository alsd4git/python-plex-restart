from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from decouple import config
import psutil
import subprocess
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {config('USER', default='admin'): config('PASSWD', default='password')}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    print(users)
    return False


def restart_plex():
    for proc in psutil.process_iter():
        if proc.name() == "Plex Media Server.exe":
            print(f"Killing Plex process with pid {proc.pid}")
            proc.kill()

    # start the service
    os.chdir("C:\\Program Files (x86)\\Plex\\Plex Media Server\\")
    subprocess.Popen(["Plex Media Server.exe"])
    print("Plex Media Server has been restarted.")


@app.route("/", methods=["POST"])
@auth.login_required
def handle_command():
    # Extract the command from the request
    command = request.json["command"]
    # Handle the command
    if command == "start":
        print("start")
        restart_plex()
        pass
    elif command == "stop":
        print("stop")
        # Stop some process
        pass
    else:
        return "Invalid command", 400
    return "Command received", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config('APP_PORT', default=8000))
