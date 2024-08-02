
'''

1) What is LCEL in the context of LangChain Chains?
A. An older Python library for building Large Language Models
B. A declarative way to compose chains together using LangChain Expression Language
C. A programming language used to write documentation for LangChain
D. A legacy method for creating chains in LangChain
Answer: B. A declarative way to compose chains together using LangChain Expression Language
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

2) How are prompt templates typically designed for language models?
A. As complex algorithms that require manual compilation
B. To be used without any modification or customization
C. To work only with numerical data instead of textual content
D. As predefined recipes that guide the generation of language model prompts
Answer: D. As predefined recipes that guide the generation of language model prompts
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

3) What is the function of "Prompts" in the chatbot system?
A. They store the chatbot's linguistic knowledge.
B. They are used to initiate and guide the chatbot's responses.
C. They handle the chatbot's memory and recall abilities.
D. They are responsible for the underlying mechanics of the chatbot.
Answer: B. They are used to initiate and guide the chatbot's responses.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

4) How are chains traditionally created in LangChain?
A. Exclusively through third-party software integrations
B. Using Python classes, such as LLM Chain and others
C. Declaratively, with no coding required
D. By using machine learning algorithms
Answer: B. Using Python classes, such as LLM Chain and others
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

5) What is the purpose of memory in the LangChain framework?
A. To store various types of data and provide algorithms for summarizing past interactions
B. To retrieve user input and provide real-time output only
C. To act as a static database for storing permanent records
D. To perform complex calculations unrelated to user interaction
Answer: A. To store various types of data and provide algorithms for summarizing past interactions
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

6) Which is a characteristic of T-Few fine-tuning for Large Language Models (LLMs)?
A. It updates all the weights of the model uniformly.
B. It selectively updates only a fraction of the model's weights.
C. It increases the training time as compared to Vanilla fine-tuning.
D. It does not update any weights but restructures the model architecture.
Answer: B. It selectively updates only a fraction of the model's weights.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

7) What is the purpose of Retrieval Augmented Generation (RAG) in text generation?
A. To generate text using extra information obtained from an external data source
B. To generate text based only on the model's internal knowledge without external data
C. To store text in an external database without using it for generation
D. To retrieve text from an external source and present it without any modifications
Answer: A. To generate text using extra information obtained from an external data source
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

8) Which statement is true about Fine-tuning and Parameter-Efficient Fine-Tuning (PEFT)?
A. Both Fine-tuning and PEFT require the model to be trained from scratch on new data, making them equally data and computationally intensive.
B. Fine-tuning requires training the entire model on new data, often leading to substantial computational costs, whereas PEFT involves updating only a small subset of parameters, minimizing computational requirements and data needs.
C. Fine-tuning and PEFT do not involve model modification; they differ only in the type of data used for training, with Fine-tuning requiring labeled data and PEFT using unlabeled data.
D. PEFT requires replacing the entire model architecture with a new one designed specifically for the new task, making it significantly more data-intensive than Fine-tuning.
Answer: B. Fine-tuning requires training the entire model on new data, often leading to substantial computational costs, whereas PEFT involves updating only a small subset of parameters, minimizing computational requirements and data needs.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

9) What does the RAG Sequence model do in the context of generating a response?
A. It retrieves a single relevant document for the entire input query and generates a response based on that alone.
B. It modifies the input query before retrieving relevant documents to ensure a diverse response.
C. For each input query, it retrieves a set of relevant documents and considers them together to generate a cohesive response.
D. It retrieves relevant documents only for the initial part of the query and ignores the rest.
Answer: C. For each input query, it retrieves a set of relevant documents and considers them together to generate a cohesive response.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

10) Given the following code block: history = StreamlitChatMessageHistory(key="chat_messages") memory = ConversationBufferMemory(chat_memory=history) Which statement is NOT true about StreamlitChatMessageHistory?
A. A given StreamlitChatMessageHistory will not be shared across user sessions.
B. StreamlitChatMessageHistory can be used in any type of LLM application.
C. A given StreamlitChatMessageHistory will NOT be persisted.
D. StreamlitChatMessageHistory will store messages in Streamlit session state at the specified key.
Answer: B. StreamlitChatMessageHistory can be used in any type of LLM application.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

11) In the simplified workflow for managing and querying vector data, what is the role of indexing?
A. To map vectors to a data structure for faster searching, enabling efficient retrieval
B. To convert vectors into a nonindexed format for easier retrieval
C. To categorize vectors based on their originating data type (text, images, audio)
D. To compress vector data for minimized storage usage
Answer: A. To map vectors to a data structure for faster searching, enabling efficient retrieval
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

12) Accuracy in vector databases contributes to the effectiveness of Large Language Models (LLMs) by preserving a specific type of relationship. What is the nature of these relationships, and why are they crucial for language models?
A. Semantic relationships; crucial for understanding context and generating precise language
B. Hierarchical relationships; important for structuring database queries
C. Linear relationships; they simplify the modeling process
D. Temporal relationships; necessary for predicting future linguistic trends
Answer: A. Semantic relationships; crucial for understanding context and generating precise language
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

13) In which scenario is soft prompting appropriate compared to other training styles?
A. When there is a significant amount of labeled, task-specific data available
B. When the model needs to be adapted to perform well in a domain on which it was not originally trained
C. When there is a need to add learnable parameters to a Large Language Model (LLM) without task-specific training
D. When the model requires continued pretraining on unlabeled data
Answer: B. When the model needs to be adapted to perform well in a domain on which it was not originally trained
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

14) What is the purpose of Retrievers in LangChain?
A. To combine multiple components into a single pipeline
B. To train Large Language Models
C. To retrieve relevant information from knowledge bases
D. To break down complex tasks into smaller steps
Answer: C. To retrieve relevant information from knowledge bases
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

15) Why is it challenging to apply diffusion models to text generation?
A. Because text generation does not require complex models
B. Because text is not categorical
C. Because diffusion models can only produce images
D. Because text representation is categorical unlike images
Answer: D. Because text representation is categorical unlike images
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

16) What is LangChain?
A. A Java library for text summarization
B. A Ruby library for text generation
C. A JavaScript library for natural language processing
D. A Python library for building applications with Large Language Models
Answer: D. A Python library for building applications with Large Language Models
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

17) Which statement is true about string prompt templates and their capability regarding variables?
A. They can only support a single variable at a time.
B. They are unable to use any variables.
C. They require a minimum of two variables to function properly.
D. They support any number of variables, including the possibility of having none.
Answer: D. They support any number of variables, including the possibility of having none.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

18) What do prompt templates use for templating in language model applications?
A. Python's list comprehension syntax
B. Python's class and object structures
C. Python's lambda functions
D. Python's str.format syntax
Answer: D. Python's str.format syntax
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

19) What does the Loss metric indicate about a model's predictions?
A. Loss measures the total number of predictions made by a model.
B. Loss is a measure that indicates how wrong the model's predictions are.
C. Loss describes the accuracy of the right predictions rather than the incorrect ones.
D. Loss indicates how good a prediction is, and it should increase as the model improves.
Answer: B. Loss is a measure that indicates how wrong the model's predictions are.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

20) When does a chain typically interact with memory in a run within the LangChain framework?
A. Continuously throughout the entire chain execution process
B. Before user input and after chain execution
C. After user input but before chain execution, and again after core logic but before output
D. Only after the output has been generated
Answer: C. After user input but before chain execution, and again after core logic but before output
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

21) What does accuracy measure in the context of fine-tuning results for a generative model?
A. The depth of the neural network layers used in the model
B. How many predictions the model made correctly out of all the possible predictions
C. The computational efficiency of the model during training
D. The total number of parameters updated during fine-tuning
Answer: B. How many predictions the model made correctly out of all the possible predictions
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

22) How can the concept of "Groundedness" differ from "Answer Relevance" in the context of Retrieval Augmented Generation (RAG)?
A. Groundedness measures relevance to the user query, whereas Answer Relevance evaluates data integrity.
B. Groundedness focuses on data integrity, whereas Answer Relevance emphasizes lexical diversity.
C. Groundedness refers to contextual alignment, whereas Answer Relevance deals with syntactic accuracy.
D. Groundedness pertains to factual correctness, whereas Answer Relevance concerns query relevance.
Answer: D. Groundedness pertains to factual correctness, whereas Answer Relevance concerns query relevance.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

23) What does a cosine distance of 0 indicate about the relationship between two embeddings?
A. They are similar in direction
B. They are completely dissimilar
C. They are unrelated
D. They have the same magnitude
Answer: A. They are similar in direction.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

24) How are documents usually evaluated in the simplest form of keyword-based search?
A. By the complexity of language used in the documents
B. Based on the presence and frequency of the user-provided keywords
C. Based on the number of images and videos contained in the documents
D. According to the length of the documents
Answer: B. Based on the presence and frequency of the user-provided keywords.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

25) When is fine-tuning an appropriate method for customizing a Large Language Model (LLM)?
A. When the LLM requires access to the latest data for generating outputs
B. When you want to optimize the model without any instructions
C. When the LLM does not perform well on a task and the data for prompt engineering is too large
D. When the LLM already understands the topics necessary for text generation
Answer: C. When the LLM does not perform well on a task and the data for prompt engineering is too large.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

26) In the context of generating text with a Large Language Model (LLM), what does the process of greedy decoding entail?
A. Picking a word based on its position in a sentence structure
B. Using a weighted random selection based on a modulated distribution
C. Selecting a random word from the entire vocabulary at each step
D. Choosing the word with the highest probability at each step of decoding
Answer: D. Choosing the word with the highest probability at each step of decoding.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

27) How does the temperature setting in a decoding algorithm influence the probability distribution over the vocabulary?
A. Decreasing the temperature broadens the distribution, making less likely words more probable.
B. Temperature has no effect on probability distribution; it only changes the speed of decoding.
C. Increasing the temperature flattens the distribution, allowing for more varied word choices.
D. Increasing the temperature removes the impact of the most likely word.
Answer: C. Increasing the temperature flattens the distribution, allowing for more varied word choices.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

28) Which LangChain component is responsible for generating the linguistic output in a chatbot system?
A. Document Loaders
B. LangChain Application
C. LLMs
D. Vector Stores
Answer: C. LLMs (Large Language Models).
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

29) How does the structure of vector databases differ from traditional relational databases?
A. It uses simple row-based data storage.
B. It is not optimized for high-dimensional spaces.
C. A vector database stores data in a linear or tabular format.
D. It is based on distances and similarities in a vector space.
Answer: D. It is based on distances and similarities in a vector space.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

30) How does a presence penalty function in language model generation?
A. It penalizes all tokens equally, regardless of how often they have appeared.
B. It penalizes only tokens that have never appeared in the text before.
C. It penalizes a token each time it appears after the first occurrence.
D. It applies a penalty only if the token has appeared more than twice.
Answer: C. It penalizes a token each time it appears after the first occurrence.
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


'''

