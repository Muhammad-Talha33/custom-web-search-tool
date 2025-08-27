from agents import Runner, set_tracing_disabled, SQLiteSession
from my_agent.simple_agent import assistant

set_tracing_disabled(True)

def main():
    session = SQLiteSession("mysession123", "conversations.db")
    while True:
     prompt = input("Enter your query: ")
     if prompt == "":
        break
     res = Runner.run_sync(starting_agent=assistant, input=prompt, session=session)
     print(res.final_output, "\n")


if __name__ == "__main__":
    main()
