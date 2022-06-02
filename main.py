import logging 
import threading
import time
from pygame import mixer 
from titlescreen import title
    
def music():#play music 
    mixer.init()
    mixer.music.load("spice/BeepBox-Song.mp3")
    for i in range(0,100):
        mixer.music.play()

if __name__ == "__main__":#use logging to play music on a separate thread that the menu and game are running on to solve pygame music problem
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")# set up logging

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=title, args=())# create thread
    y = threading.Thread(target=music, args=())# create thread
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish") 