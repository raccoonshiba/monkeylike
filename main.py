import logging 
import threading
import time
from pygame import mixer 
from titlescreen import title
    
def music():
    mixer.init()
    mixer.music.load("spice/BeepBox-Song.mp3")
    mixer.music.play()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=title, args=())
    y = threading.Thread(target=music, args=())
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")