from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses import dataclass
import json
from json import JSONEncoder
from jsonschema import validate
import os.path

SCHEMA_JSON = os.path.join(os.path.dirname(__file__), 'schema', 'schema.json')

@dataclass
class AIModel:
    name: str
    version: str
    description: str
    owner: str
    location: str
    licence: Optional[str] = None
    model_structure: Optional[str] = None


@dataclass
class Metric:
    key: str
    value: str


@dataclass
class BiasAnalysis:
    name: str
    metrics: List[Metric] = field(default_factory=list)


@dataclass
class ExplainabilityAnalysis:
    name: str
    metrics: List[Metric] = field(default_factory=list)


@dataclass
class ModelCard:
    name: str
    version: str
    short_description: str
    full_description: str
    keywords: str
    author: str
    input_data: Optional[str] = None
    output_data: Optional[str] = None
    ai_model: Optional[AIModel] = None
    bias_analysis: Optional[BiasAnalysis] = None
    xai_analysis: Optional[ExplainabilityAnalysis] = None

    def __str__(self):
        """
        Overriding the __str__ to pretty print the model card in Json format.
        :return:
        """
        return json.dumps(self.__dict__, cls=ModelCardJSONEncoder, indent=2)

    def validate(self):
        """
        Validates the current model against the Model Card schema
        :return:
        """
        # Convert the dataclass object to JSON string using the custom encoder
        mc_json = json.dumps(self, cls=ModelCardJSONEncoder, indent=4)

        with open(SCHEMA_JSON, 'r') as schema_file:
            schema = json.load(schema_file)

        validate(json.loads(mc_json), schema)


class ModelCardJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (ModelCard, Metric, AIModel, ExplainabilityAnalysis, BiasAnalysis)):
            return obj.__dict__
        return super().default(obj)