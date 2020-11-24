import subprocess
import sys
import json
import requests


class DataGenerator():
    def __init__(self, dst_url):
        self.dst_url = dst_url
        self.running = False

    @staticmethod
    def init_generator_process():
        cmd = "generator-windows-amd64.exe"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        return process

    @staticmethod
    def parse_json(str):
        try:
            return json.loads(str)
        except ValueError as err:
            return None

    def start_generating(self):
        print("start")
        process = self.init_generator_process()
        self.running = True
        while self.running:
            out = process.stdout.readline()
            if out == '' and process.poll() != None:
                break
            if out != '':
                json = self.parse_json(out)
                if json:
                    # print(json)
                    requests.post(self.dst_url, data=json)

    def stop(self):
        self.running = False


x = DataGenerator("http://localhost:8000/events/")
x.start_generating()
