from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

#With Chains
chain=template|model|parser
result=chain.invoke({'topic':'black hole'})
print(result)

#Without chains
prompt=template.invoke({'topic':'time dilation'})
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)