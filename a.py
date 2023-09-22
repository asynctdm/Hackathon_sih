
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


from langchain.llms.huggingface_pipeline import HuggingFacePipeline
import faulthandler
faulthandler.enable()
def model(model_id: str, task: str, model_kwargs: dict, pipeline_kwargs: dict):
    embedding_func = HuggingFacePipeline.from_model_id(
    model_id='mrm8488/t5-base-finetuned-summarize-news',
    task='summarization',
    model_kwargs=model_kwargs,
    pipeline_kwargs=pipeline_kwargs,
    )
    return embedding_func


model_name = 'mrm8488/t5-base-finetuned-summarize-news',
model_kwargs = {'temperature': 0.75, 'top_k': 10, 'top_p': 0.5, 'max_length': 150, 'min_length': 10,'num_beams': 2, 'num_return_sequences': 2, 'repetition_penalty': 2.5, 'length_penalty': 1.0}
pipeline_kwargs = {'repetition_penalty': 2.5, 'length_penalty': 1.0}
# cache_folder='.\\hugging_face_model\\'
# cache_folder = '.\\model\\'

model = model(model_name,'summarization', model_kwargs, pipeline_kwargs)
prompt = 'Prime Minister Justin Trudeau’s allegation of Indian involvement in Khalistani leader Hardeep Singh Nijjar’s killing heightened the tensions and triggered a diplomatic row, and tit-for-tat expulsions of senior diplomats this week. No formal announcement of the suspension of visa services was made even as BLS International, which runs the visa application centres in Canada, posted a message on its Canadian website in this regard. “Important notice from the Indian Mission: Due to operational reasons, with effect from 21st September 2023 [Thursday], Indian visa services have been suspended till further notice.” An Indian official confirmed the suspension but refused to comment further. “The language is clear and it says what it is intended to say.” This is the first time India has suspended visas since the Covid-19 pandemic. The Indian high commission’s website could not be accessed late on Wednesday for confirmation as it appeared to be down. The suspension followed India’s advisory on Wednesday asking its citizens in Canada to exercise utmost caution due to growing anti-India activities and “politically-condoned hate crimes”. Indian students have particularly been advised to exercise extreme caution and remain vigilant.'
edited_prompt = f'ummarise this news article\n{prompt}'
response = model._call(prompt=edited_prompt)


print("Response = ", response)