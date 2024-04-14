import time
import threading
import datetime
import signal

#  Copyright (c) 2020. Zhangzhe
#  https://home.asec01.net/

savename = "link.txt"
import sys
import os

if len(sys.argv) >= 2:
    savename = sys.argv[1]
    print("保存的文件名:", savename)

maxThread = 1
if len(sys.argv) >= 3:
    savename = sys.argv[2]
    print("线程数:", maxThread)
else:
    maxThread = 25

if maxThread > 48:
    print("线程数设置太高，建议最大48线程！")
    input("按回车继续...")
elif maxThread > 32:
    print("建议尝试32线程，不要太高！")
    input("按回车继续...")

import json
import requests

'''
#汽车
response = requests.get('https://ics.autohome.com.cn/passport/Account/createGt?').text
response=json.loads(response)['result']
old_challenge = response['challenge']
gt=response["gt"]
'''

headers = {
    'Host': 'api.geetest.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Referer': 'https://ics.autohome.com.cn/passport/',
}

img_u = "https://static.geetest.com"
u_reset = "https://api.geetest.com/reset.php?gt={}&challenge={}"
u_ajax = "https://api.geetest.com/ajax.php?gt={}&challenge={}"
u_get_first = "https://api.geetest.com/get.php?is_next=true&gt={}&challenge={}"
u_refresh_start = "https://api.geetest.com/refresh.php?gt={}&challenge={}"


def sendRequest(gt, old_challenge):
    resultLink = []
    reset_txt = requests.get(u_reset.format(gt, old_challenge), headers=headers).text
    reset_dict = json.loads(reset_txt.split('(')[1][:-1])
    new_challenge = reset_dict["data"]["challenge"]
    old_challenge = new_challenge
    ajax_txt = requests.get(u_ajax.format(gt, new_challenge), headers=headers).text
    stat = json.loads(ajax_txt.split('(')[1][:-1])["status"]
    if stat != "success":
        print(1)
        return resultLink, old_challenge
    get_first_txt = requests.get(u_get_first.format(gt, new_challenge), headers=headers).text
    get_first_dict = json.loads(get_first_txt.split('(')[1][:-1])
    if get_first_dict["status"] != "success":
        print(2)
        return resultLink, old_challenge
    u_img = img_u + get_first_dict["data"]["pic"]
    resultLink.append(u_img)
    try:
        for i in range(5):
            u_refresh = u_refresh_start.format(gt, new_challenge)
            refresh_txt = requests.get(u_refresh, headers=headers).text
            refresh_dict = json.loads(refresh_txt.split('(')[1][:-1])
            if get_first_dict["status"] != "success":
                print(3)
                return False, old_challenge
            u_img = img_u + refresh_dict["data"]["pic"]
            resultLink.append(u_img)
    except:
        pass
    return resultLink, old_challenge



threadLock = threading.Lock()
crawled = 0
starttime = datetime.datetime.now()
resultList = []
threads = []
requestTerm = False


class myThread(threading.Thread):

    def __init__(self, threadID, daemon=None):
        super(myThread, self).__init__(daemon=daemon)
        self.__is_running = True
        self.daemon = daemon
        self.threadID = threadID

    def terminate(self):
        self.__is_running = False

    def run(self):
        printt(self.threadID, "Started")
        while True:
            try:
                response = requests.get(
                    'https://www.geetest.com/demo/gt/register-phrase').text
                response = response.replace("&&&START&&&", "")
                resp = json.loads(response)
                old_challenge = resp['challenge']
                gt = resp['gt']
                printt(self.threadID, "Get initial info success. (gt: {},challenge:{})".format(gt, old_challenge))
                while True:
                    try:
                        resultList, old_challenge = sendRequest(gt, old_challenge)
                        processResult(self.threadID, resultList)
                    except Exception as e:
                        printt(self.threadID, "Error: {}".format(e.args))
                        SleepThread(3).start()
            except Exception as e:
                printt(self.threadID, "Error(GetFirstChallenge): {}".format(e.args))


class SleepThread(threading.Thread):
    def __init__(self, sleepSec):
        threading.Thread.__init__(self)
        self.sleepSec = sleepSec

    def run(self):
        threadLock.acquire()
        print("Thread SleepThread:\tSleep {}s".format(self.sleepSec))
        time.sleep(self.sleepSec)
        threadLock.release()


class CountThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Count Thread Started")
        while True:
            try:
                while True:
                    lastCount = crawled
                    time.sleep(5)
                    txt = "StartTime: {}    Count: {}    Speed: {}/min".format(starttime, crawled,
                                                                               (crawled - lastCount) * 12)
                    import ctypes
                    ctypes.windll.kernel32.SetConsoleTitleW(txt)
            except:
                lastCount = crawled
                time.sleep(60)
                txt = "TotalCount: {}, Speed: {}/min".format(crawled, (crawled - lastCount))
                printt("Count", txt)


countThread = CountThread()


class WriteThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        def checkSig():
            return requestTerm

        printt("writeThread", "Write Thread Started")
        while True:
            try:
                for t in range(5):
                    if requestTerm:
                        sys.exit(0)
                    else:
                        time.sleep(1)
                if len(resultList) != 0:
                    resultFile = open(savename, 'a')
                    while True:
                        try:
                            item = resultList.pop()
                            resultFile.write(item + "\n")
                        except:
                            break
                    resultFile.close()
                if requestTerm:
                    printt("writeThread", "Write Thread Finished")
                    break
            except Exception as e:
                printt("writeThread", "Warning! Write Thread Error!!!!!\nErrorInfo: {}".format(e.args))


writeThread = WriteThread()


def printt(threadId, content):
    threadLock.acquire()
    print("Thread {}:\t{}".format(threadId, content))
    threadLock.release()


def processResult(threadID, l):
    global crawled
    if len(l) == 0:
        printt(threadID, "Request fail, Total crawled:{}".format(crawled))
    else:
        for i in l:
            resultList.append(i)
            crawled += 1
        printt(threadID, "Crawled {} item(s), Total crawled:{}".format(len(l), crawled))


def zzexit(signum, frame):
    printt("Main", 'Term signal received.')
    requestTerm = True
    writeThread.join()
    printt("Main", "Write Thread Finished.")
    printt("Main", "Jobs finished.")
    printt("Main", "Start time: {}".format(starttime))
    endtime = datetime.datetime.now()
    printt("Main", "End time: {}".format(endtime))
    printt("Main", "Elapsed time: {}".format((endtime - starttime).seconds))
    printt("Main", "Success count: {}".format(crawled))
    threadLock.acquire()
    time.sleep(60)
    threadLock.release()
    sys.exit(0)


def mainInit():
    countThread.start()
    writeThread.start()
    for i in range(maxThread):
        thread = myThread(i)
        thread.start()
        threads.append(thread)
        time.sleep(0.2)
    printt("Main", "All thread started")
    signal.signal(signal.SIGTERM, zzexit)


if __name__ == '__main__':
    mainInit()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        zzexit(None, None)
