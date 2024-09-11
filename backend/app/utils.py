from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from app.config import settings

def setup_chain():
    # Define the template for the prompt
    template = """
        You are a helpful mental health assistant. The following is a conversation between a user and you. Use the conversation history to provide accurate and helpful responses.
        Conversation history:
        {history}
        User: {question}
        Assistant:
    """

    # Initialize the prompt
    prompt = PromptTemplate(template=template, input_variables=["history", "question"])

    # Initialize OpenAI LLM
    llm = OpenAI(
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY
    )

    # Setup memory to maintain chat history
    memory = ConversationBufferMemory(memory_key="history", input_key="question")

    # Create the LLM chain
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )

    return chain

# # Example usage
# if __name__ == "__main__":
#     chain = setup_chain()
#     response1 = chain.run({"question": "What are the common signs of depression?"})
#     print(response1)

#     response2 = chain.run({"question": "Can you tell me more about treatment options?"})
#     print(response2)
