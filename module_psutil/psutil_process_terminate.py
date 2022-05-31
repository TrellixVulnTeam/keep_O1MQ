import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    pid = int(sys.argv[1])

    p = psutil.Process(pid=pid)
    logging.info("Terminate process pid = %s", p.pid)

    p.terminate()
    logging.info("Done")
