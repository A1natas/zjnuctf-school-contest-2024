from challenge1 import challenge_one
from challenge2 import CHALLENGE_TWO_BASE_CODE, challenge_two
from challenge3 import challenge_three


def main():
    prompt = r"""
 ________      _____     __  __      __  __      ____       ______    ____    
/\_____  \    /\___ \   /\ \/\ \    /\ \/\ \    /\  _`\    /\__  _\  /\  _`\  
\/____//'/'   \/__/\ \  \ \ `\\ \   \ \ \ \ \   \ \ \/\_\  \/_/\ \/  \ \ \L\_\
     //'/'       _\ \ \  \ \ , ` \   \ \ \ \ \   \ \ \/_/_    \ \ \   \ \  _\/
    //'/'___    /\ \_\ \  \ \ \`\ \   \ \ \_\ \   \ \ \L\ \    \ \ \   \ \ \/ 
    /\_______\  \ \____/   \ \_\ \_\   \ \_____\   \ \____/     \ \_\   \ \_\ 
    \/_______/   \/___/     \/_/\/_/    \/_____/    \/___/       \/_/    \/_/ 
"""
    prompt += "Welcome to 2024 ZJNUCTF 4th, here are three AI challenges...\n"
    prompt += "1. AI Interpreter\n"
    prompt += "2. Code Helper\n"
    prompt += "3. Function Selector\n"
    prompt += "Your choice:"

    user_input = input(prompt)
    match user_input:
        case "1":
            prompt = "This AI can fully understand what you are saying and translate it. Try to have a conversation with AI.  I secretly told you that I told the AI about the flag, try to get it...\n"
            prompt += "Your prompt: "
            print(challenge_one(input(prompt).strip()))
        case "2":
            prompt = "This AI can generate the corresponding Python 3 code according to your requirements, but if the AI thinks you want to generate malicious code, it will warn you of 'Your are a HACKER!'. If everything goes smoothly, the generated code will be executed after it is generated, but there is a special section of code that will be executed before the generated code, here it is:"
            prompt += f"\n{CHALLENGE_TWO_BASE_CODE}\n"
            prompt += "Now show your prompt and try to execute code to get flag: "
            print(challenge_two(input(prompt).strip()))
        case "3":
            prompt = "This AI is a file-read tool.It will select the corresponding function to read the file based on the filename you input, and try to read '/flag' by bypassing it!\n"
            prompt += (
                "Please input your prompt to tell AI which file you want to read:\n"
            )
            user_input = input(prompt).strip()
            base_url = input(
                "Before send your prompt, please choose OpenAI api base url(default is `https://api.openai.com/v1`):\n"
            ).strip()
            if base_url == "default":
                base_url = ""
            api_key = input(
                "Before send your prompt, please give me your own api key(default is woodwhale's gpt-3.5 base key):\n"
            ).strip()
            print(challenge_three(base_url, api_key, user_input))
        case _:
            print("WTF???")


if __name__ == "__main__":
    main()
