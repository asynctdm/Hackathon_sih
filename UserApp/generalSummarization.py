# Using llama.cpp in python
import faulthandler
faulthandler.enable()
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.schema import HumanMessage,SystemMessage,AIMessage 


template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# prompt = PromptTemplate(template=template, input_variables=["question"])
# # Callbacks support token-wise streaming
callback_manager = CallbackManager([StdOutCallbackHandler()])
# Make sure the model path is correct for your system!

def llm_init(file_path :str):
    '''
    file_path str : The file path for the model
    '''

    llm = LlamaCpp(
        model_path=f'{file_path}',
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        callback_manager=callback_manager, 
        verbose=True, # Verbose is required to pass to the callback manager
    )
    return llm
# llm.generate(
#     [
#         SystemMessage(content="You are an unhelpful AI bot that makes a joke at whatever the user says"),
#         HumanMessage(content="I would like to go to New York, how should I do this?")
#     ]
# )

# llm("You are not rakesh ")
# prompt = """
# Question: When was the iphone first released?
# """
# response  = llm(prompt)
# print('Response = ', response)

# Fro testing
if __name__ == '__main__':
    llm = llm_init('/Users/cardinal/testing/vicuna-13b-v1.5-16k.Q3_K_M.gguf')
    machineChat = llm('How can I learn ML')
    # for ch in machineChat:
    #     print("Character = ", ch)
    print("Machine chat :", machineChat)