import subprocess
import sys


def init_process():
    cmd = "generator-windows-amd64.exe"
    process = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    return process


def start_process(process):
    while True:
        out = process.stderr.readline()
        if out == '' and p.poll() != None:
            break
        if out != '':
            # sys.stdout.write(out)
            # sys.stdout.flush()
            yield out


process = init_process()
start_process(process)
