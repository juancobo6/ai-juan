To introduce the topic of agents, let’s start by clarifying what we mean by an **agent**. 

The term is still new, loosely defined, and very much in vogue, so the exact wording shifts from one author to the next. Rather than chase a single “official” answer, I’ll share the working definition we’ll use in this series—one tailored to agents built on large language models (LLMs).


**In our context, an agent is a system that accomplishes tasks by combining three capabilities:**

**Decision-making** – choosing what to do next.

**Tool use** – invoking external resources such as APIs, code interpreters, or databases.

**Memory** – retaining information from prior steps or interactions.


That definition can feel abstract, so let’s try comparing an agent with a plain language model.


Most of us have tried GPT. It’s easy to think of ChatGPT as “just a model,” but it is better understood as an **agent** built on top of GPT-4 (or 3.5, or whichever engine is under the hood). A raw model only transforms input into output; an agent layers decision logic, tool calls, and memory on top of that model.

Let's see a concrete example, imagine we ask ChatGPT:

Write a Python script that prints the first ten prime numbers, run it, and show me the result._


To satisfy that request, ChatGPT must:

First, draft the Python code and decide that it need to be executed - **decision-making**.

Then, execute the code through an embedded tool - **tool calling**.

After getting the result from the tool, it Inspect the output to verify success and decide whether further action is needed - again, **decision-making**

And finally, respond with both the script and the result.

All the while, it **stores** the interaction in memory; if we later ask, “What was the last thing I asked you?” it can answer.


Remove the agent layer, and a standalone model would fail on every count: it couldn’t execute code, assess results, remember previous turns, or decide on next steps—because none of those abilities live inside the model itself.