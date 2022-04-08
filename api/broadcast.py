import subprocess
import os
import time
import psutil


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


class transmit:
    """
    Transmit data to the server.
    """

    def __init__(self, data):
        self.data = data

    def go(self):
        os.chdir("api/fm_transmitter/")
        print(os.getcwd())
        bashCommand = ["sudo", "./fm_transmitter", "-f", "102.3", "sample.wav"]
        self.process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
        return True

    def stop(self):
        kill(self.process.pid)
        return True

    def status(self):
        output, error = self.process.communicate()
        return output, error


# tr = transmit("ad")
# tr.go()
# time.sleep(3)
# tr.stop()
# print(tr.status())
