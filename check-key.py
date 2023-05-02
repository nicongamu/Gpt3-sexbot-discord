import openai

def check_openai_key(api_key):
    openai.api_key = api_key

    try:
        models = openai.Model.list()
        print("API key is valid.")
        return True
    except openai.errors.AuthenticationError:
        print("API key is invalid.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

api_key = input("Enter your OpenAI API key: ")
check_openai_key(api_key)
