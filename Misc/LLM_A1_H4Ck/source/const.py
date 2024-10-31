from os import environ

#! init openai apt
OPENAI_API = "https://api.openai.com/v1"
OPENAI_KEY = environ.get("OPENAI_KEY")

#! init challenges
CHALLENGE_TEST_FLAG = r"zjnuctf{test_flag}"
CHALLENGE_ONE_FLAG = environ.get("FLAG1", r"zjnuctf{Ez4I_Pr0mpT_1n73cti0n}")
CHALLENGE_TWO_FLAG = environ.get("FLAG2", r"zjnuctf{Ex3c_Pyth0n_C0d3_1s_V3r7_Ezzz!}")
CHALLENGE_THREE_FLAG = environ.get("FLAG3", r"zjnuctf{LLM_FUt10ns_C4ll1Ng_1s_G@0d!}")
CHALLENGE_TWO_RANDOM_VAR = r"THIS_IS_RANDOM_STRING"
CHALLENGE_TWO_BASE_CODE = f"""
import os, sys
sys.addaudithook((lambda x: lambda *_: print(_[-1][-2]) if "excepthook" in str(_) else x(1))(os._exit))
{CHALLENGE_TWO_RANDOM_VAR} = r'{CHALLENGE_TEST_FLAG}'
"""
