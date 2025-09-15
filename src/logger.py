import logging
from datetime import datetime
from pathlib import Path

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = Path.cwd() / "logs"
logs_dir.mkdir(parents=True, exist_ok=True) # create logs/ directory
LOG_FILE_PATH = logs_dir / LOG_FILE # file inside logs/

logging.basicConfig(
    filename=str(LOG_FILE_PATH),
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    print(f"Log written to - {LOG_FILE_PATH}")