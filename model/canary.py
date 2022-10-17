import os
import json
from pathlib import Path

from typing import List, Union

from parlai.core.message import Message
from parlai.core.agents import create_agent
import parlai.core.build_data as build_data

PROJECT_HOME = Path(__file__).parent.parent.resolve()
DATA_DIR = os.path.join(PROJECT_HOME, 'data')

CANARY_MODEL_FILE = [
    build_data.DownloadableFile(
        'https://storage.googleapis.com/ai2-mosaic-public/projects/prosocial-dialog/models/canary.tar.gz',
        'canary.tar.gz',
        '33d264e73c389726f193b448a878275b45a91954a95ef4be988a1fba75712d60',
        zipped=True, from_google=False,
    ),
]

def download(datapath, version='v1.0'):
    dpath = os.path.join(datapath, 'models', 'canary')

    if not build_data.built(dpath, version):
        print('[Downloading and building Canary: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        print("NOTE: Since Canary's size is 10GB, the download and extraction can take a long time.")
        for downloadable_file in CANARY_MODEL_FILE:
            downloadable_file.download_file(dpath)

        # Mark the data as built.
        build_data.mark_done(dpath, version)

    return dpath

class Canary(object):
    def __init__(self):
        canary_dir = download(DATA_DIR)
        canary_meta_data = os.path.join(canary_dir, 'model.opt')
        with open(canary_meta_data) as f:
            opt = json.load(f)

        opt['skip_generation'] = False
        opt['model_file'] = os.path.join(canary_dir, 'model')
        self.agent = create_agent(opt)

    def chirp(self, input: Union[str, List]):
        if isinstance(input, str):
            input = [input]

        return self.get_batch_output(input)
    
    def get_output(self, input: str):
        return self.agent.respond(Message(text=input))

    def get_batch_output(self, batch_input: List[str]):
        message_batch = []
        for input in batch_input:
            message_batch.append(Message(text=input))

        return self.agent.batch_respond(message_batch)
    
    def reset(self):
        self.agent.reset()