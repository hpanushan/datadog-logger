import logging
import sys
import time
def main():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    counter = 0
    while True:
        counter += 1
        logging.info(f"test {counter}")
        time.sleep(1)

if __name__ == "__main__":
    main()
