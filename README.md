# ProsocialDialog

Welcome! 👋🏻\
This is the official repository of the ProsocialDialog dataset, Canary, and Prost from our EMNLP 2022 paper: \
**[ProsocialDialog: A Prosocial Backbone for Conversational Agents.](https://hyunw.kim/papers/prosocial-dialog.pdf)**

![dialogue illustration](images/dialogue.png)

Please cite our work if you found the resources in this repository useful:

```bib
@inproceedings{kim2022prosocialdialog,
    title={ProsocialDialog: A Prosocial Backbone for Conversational Agents},
    author={Hyunwoo Kim and Youngjae Yu and Liwei Jiang and Ximing Lu and Daniel Khashabi and Gunhee Kim and Yejin Choi and Maarten Sap},
    booktitle={EMNLP},
    year=2022
}
```

## Dataset

We provide two different formats of our dataset:

* HuggingFace: dataframe format
* Direct download: list of dialogues

The only difference is the format; the contents are the same.

### HuggingFace 🤗

You can load our dataset from the [HuggingFace hub](https://huggingface.co/datasets/allenai/prosocial-dialog) as the following:

```python
from datasets import load_dataset

dataset = load_dataset("allenai/prosocial-dialog", split='train')
prosocial_df = dataset.to_pandas()
```

💡 Note, the dataset format of the HuggingFace hub version and the direct download version is different. For the HuggingFace version, please take a look at the [dataset preview](https://huggingface.co/datasets/allenai/prosocial-dialog).

### Direct download

You can also download our dataset directly by clicking this [link](https://drive.google.com/u/1/uc?id=1d-987AjyfVdFnohBqQ3yaHt-b5mVezHa&export=download&confirm=t).

#### Dataset format when downloaded directly using the link above

Each split (train/valid/test) contains a list of dialogues. \
A dialogue has the following structure:

```
[
    {
        "text": ... # utterance 1
        "labels": [
            ... # utterance 2
        ],
        "rots": [
            ...
        ],
        "safety_label": ...,
        "safety_annotations": [
            ...
        ],
        "safety_annotation_reasons": [
            ...
        ],
        "source": ...,
        "etc": ...,
        "episode_done": false
    },
    ...,
    {
        "text": "I don't care what people think about me. I just want to make someone else's life miserable. Maybe I should instead threaten him with this.", # utterance 5
        "labels": [
            "You need to stop this. He might be having medical difficulties with this issue, so please try to help him out instead. It's important to look out for others when they're having trouble." # utterance 6
        ],
        "rots": [
            "It's wrong to threaten someone.",
            "You should look out for others."
        ],
        "safety_label": "__needs_intervention__",
        "safety_annotations": [
            "needs caution",
            "needs intervention",
            "needs intervention"
        ],
        "safety_annotation_reasons": [
            "They don't care how their actions would hurt the other person.",
            "Did not listen to the advice and plans to threaten the classmate.",
            "Now the speaker is thinking of threatening his classmate."
        ],
        "source": "socialchemistry",
        "etc": "reddit/amitheasshole/b26onw",
        "episode_done": true
    }
]
```

Please see below for a description of each attribute in the dataset:

attribute | type | description
--- | ---  | ---
`text` | str | the potentially unsafe utterance
`labels` | list of str | the guiding utterance grounded on rules-of-thumb (`rots`)
`rots` | list of str\|null | the relevant rules-of-thumb for `text` *not* labeled as \_\_casual\_\_
`safety_label` | str | the final verdict of the context according to `safety_annotations`: {\_\_casual\_\_, \_\_possibly\_needs\_caution\_\_, \_\_probably\_needs\_caution\_\_, \_\_needs\_caution\_\_, \_\_needs\_intervention\_\_}
`safety_annotations` | list of str | raw annotations from three workers: {casual, needs caution, needs intervention}
`safety_annotation_reasons` | list of str | the reasons behind the safety annotations in free-form text from each worker
`source` | str | the source of the seed text that was used to craft the first utterance of the dialogue: {socialchemistry, sbic, ethics_amt, ethics_reddit}
`etc` | str\|null | other information
`episode_done` | bool | an indicator of whether it is the end of the dialogue

## Canary 🐥

You can now directly download our Canary [here](https://storage.googleapis.com/ai2-mosaic-public/projects/prosocial-dialog/models/canary.tar.gz)!<br>
The model will also be automatically downloaded when you create Canary by calling the `Canary()` class.<br>
Have a look at the [demo notebook](https://github.com/skywalker023/prosocial-dialog/blob/main/demo/canary_demo.ipynb) to see how you can load Canary and use it!

### Environment setup

Our code is built on the [ParlAI](https://parl.ai/) framework. We recommend you create a conda environment as follows

```bash
conda env create -f environment.yml
```

and activate it with

```bash
conda activate prosocial-dialog
```

## Have any questions?

Please contact [Hyunwoo Kim](https://hyunw.kim) at hyunw.kim at vl.snu.ac.kr

## License

This repository is MIT licensed. See the [LICENSE](https://github.com/skywalker023/prosocial-dialog/blob/main/LICENSE) file for details.
