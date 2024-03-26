import sys
import qrcode
from dotenv import load_dotenv
import logging
from pathlib import Path
import os
import argparse
import validators
from datetime import datetime

# Load environmental secrets
load_dotenv()

# Unique Configuration Variables
MYTHICAL_QR_DIRECTORY = 'ancient_codes'
MYSTICAL_FILL_COLOR = 'indigo'
ENIGMATIC_BACK_COLOR = 'aquamarine'

def setup_logging_adventure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def create_quest_directory(quest: Path):
    try:
        quest.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to manifest {quest} in the mystical realm: {e}")
        sys.exit(1)

def is_magical_url(url):
    if validators.url(url):
        return True
    else:
        logging.error(f"The essence of the provided URL lacks magical resonance: {url}")
        return False

def summon_qr_code(data, path, fill_color=MYSTICAL_FILL_COLOR, back_color=ENIGMATIC_BACK_COLOR):
    if not is_magical_url(data):
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)

        with path.open('wb') as qr_file:
            qr_image.save(qr_file)
        logging.info(f"A portal to the unknown has been forged at {path}")

    except Exception as e:
        logging.error(f"An unexpected rift occurred during the summoning of the QR code: {e}")

def embark_on_quest():
    parser = argparse.ArgumentParser(description='Embark on a mystical quest to create a QR code.')
    parser.add_argument('--url', help='The magical URL to encode in the QR code', default='https://github.com/Akarsh0809/Homework-7.git')
    args = parser.parse_args()

    setup_logging_adventure()

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    qr_filename = f"QR_Arcane_{timestamp}.png"

    qr_quest = Path.cwd() / os.getenv('QR_CODE_DIR', MYTHICAL_QR_DIRECTORY)
    create_quest_directory(qr_quest)

    qr_path = qr_quest / qr_filename

    summon_qr_code(args.url, qr_path)

if __name__ == "__main__":
    embark_on_quest()
