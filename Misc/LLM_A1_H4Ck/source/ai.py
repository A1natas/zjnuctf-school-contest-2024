from const import OPENAI_API, OPENAI_KEY
from openai import OpenAI
from openai._types import NOT_GIVEN


class A1natasAI:
    def __init__(self, base_url: str = None, api_key: str = None) -> None:
        self.retry_count = 0
        if not base_url:
            base_url = OPENAI_API
        if not api_key:
            if base_url == OPENAI_API:
                self.api_keys = OPENAI_KEY.split("|")
                self.api_key_index = 0
                api_key = self.api_keys[self.api_key_index]
            else:
                api_key = "Here is woodwhale from A1natas!"

        self.base_url = base_url
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def refresh_api_key(self):
        if self.base_url != OPENAI_API:
            return False

        if self.api_key_index >= len(self.api_keys) - 1:
            self.retry_count += 1
            if self.retry_count > 3:
                return False
            self.api_key_index = 0
        else:
            self.api_key_index += 1

        api_key = self.api_keys[self.api_key_index]
        self.client = OpenAI(api_key=api_key, base_url=self.base_url)
        
        return True if self.client else False

    def create(
        self,
        model: str = None,
        stream: bool = False,
        temperature: float = None,
        messages: list = None,
        function_call: str = None,
        functions: list = None,
    ):
        err, completion = None, None
        if model:
            try:
                completion = self.client.chat.completions.create(
                    model=model,
                    stream=stream or NOT_GIVEN,
                    temperature=temperature or NOT_GIVEN,
                    messages=messages or NOT_GIVEN,
                    functions=functions or NOT_GIVEN,
                    function_call=function_call or NOT_GIVEN,
                )
            except Exception as e:
                err = f"{e}\n"

            return completion, err

        for model in [
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-16k-0613",
        ]:
            try:
                completion = self.client.chat.completions.create(
                    model=model,
                    stream=stream or NOT_GIVEN,
                    temperature=temperature or NOT_GIVEN,
                    messages=messages or NOT_GIVEN,
                    functions=functions or NOT_GIVEN,
                    function_call=function_call or NOT_GIVEN,
                )
                if completion:
                    return completion, err
            except Exception as e:
                if err is None:
                    err = ""
                err += f"{e}\n"

        if not completion:
            if self.refresh_api_key():
                return self.create(
                    model,
                    stream,
                    temperature,
                    messages,
                    function_call,
                    functions,
                )

        return completion, err
