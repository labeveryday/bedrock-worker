from pydantic import BaseModel, PositiveInt, PositiveFloat


class LLMParams(BaseModel):
    prompt: str
    temperature: PositiveFloat = 1.0
    modelId: str
    maxTokenCount: PositiveInt = 4096
    stopSequences: list[str] = []
    topP: PositiveFloat = None
    topK: PositiveInt = None
