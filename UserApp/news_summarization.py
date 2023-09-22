# The news summarization

from langchain.llms.huggingface_pipeline import HuggingFacePipeline
import faulthandler

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))


faulthandler.enable()
def model(model_id: str, task: str, model_kwargs: dict, pipeline_kwargs: dict):
    embedding_func = HuggingFacePipeline.from_model_id(
    model_id='mrm8488/t5-base-finetuned-summarize-news',
    task='summarization',
    model_kwargs=model_kwargs,
    pipeline_kwargs=pipeline_kwargs,
    )
    return embedding_func

# The main function which controls the model
def summarizer(userChat :str, ):
    model_name = 'mrm8488/t5-base-finetuned-summarize-news',
    model_kwargs = {'temperature': 0.75, 'top_k': 10, 'top_p': 0.5, 'max_length': 500, 'min_length': 10,'num_beams': 2, 'num_return_sequences': 2, 'repetition_penalty': 2.5, 'length_penalty': 1.0}
    pipeline_kwargs = {'repetition_penalty': 2.5, 'length_penalty': 1.0}

    model = model(model_name,'summarization', model_kwargs, pipeline_kwargs)
    edited_prompt = f'Summarise this news article\n{userChat}'
    response = model._call(prompt=edited_prompt)
    return response