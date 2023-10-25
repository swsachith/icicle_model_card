from icicle_model_card.icicle_model_card import *
import json
import unittest

from jsonschema import validate
import os.path

SCHEMA_JSON = os.path.join(os.path.dirname(__file__), '../icicle_model_card/schema', 'schema.json')


class PersonTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.aimodel = AIModel(
            name="DenseNet",
            version="v0.1",
            description="DenseNet CNN model",
            owner="PyTorch",
            location="pytorch.org",
            license="testLicence",
            framework="tensorflow",
            model_type="cnn",
            test_accuracy=0.89
        )
        self.bias_analysis = BiasAnalysis(0.1, 0.2, 20, 10, 10, 20, 0.1, 0.2, 0.2, 0.1)
        self.xai_analysis = ExplainabilityAnalysis("XAI Test 2", [Metric("xai1", 0.5), Metric("xai2", 0.8)])

        self.mc = ModelCard(
            name="icicle-camera-traps",
            version="0.1",
            short_description="Camera Traps CNN inference model card",
            full_description="Camera Traps CNN full descr inference model card",
            keywords="cnn, pytorch, icicle",
            author="Joe",
            input_data="cifar10",
            output_data="None",
            ai_model=self.aimodel,
            bias_analysis=self.bias_analysis,
            xai_analysis=self.xai_analysis
        )
        self.mc_save_location = "./test_mc.json"

    def test_json_serialization(self):
        """
        This tests the serialization of the Model Card object.
        :return:
        """
        # Convert the dataclass object to JSON string using the custom encoder
        mc_json = json.dumps(self.mc, cls=ModelCardJSONEncoder, indent=2)

        # Parse the JSON string back to a dictionary
        parsed_mc = json.loads(mc_json)

        self.assertEqual(parsed_mc['name'], "icicle-camera-traps")
        self.assertEqual(parsed_mc['ai_model']['name'], "DenseNet")
        self.assertEqual(parsed_mc['bias_analysis']['demographic_parity_difference'], 0.1)

    def test_schema_compatibility(self):
        """
        This tests whether the python classes are inline with the provided model card schema.
        :return:
        """
        # Convert the dataclass object to JSON string using the custom encoder
        mc_json = json.dumps(self.mc, cls=ModelCardJSONEncoder, indent=4)

        with open('../icicle_model_card/schema/schema.json', 'r') as schema_file:
            schema = json.load(schema_file)

        try:
            validate(json.loads(mc_json), schema)
        except:
            self.fail("Validation Error!")

    def test_validate(self):
        """
        This tests the validate function.
        :return:
        """
        is_valid = validate_mc(model_card=self.mc)
        self.assertTrue(is_valid)

    def test_framework_enum(self):
        """
        This tests the validate function.
        :return:
        """
        mc = ModelCard(
            name="tset-mc",
            version="test-version",
            short_description="short desc",
            full_description="full_desc",
            keywords="test keyword",
            author="test author"
        )
        aimodel = AIModel(
            name="DenseNet",
            version="v0.1",
            description="DenseNet CNN model",
            owner="PyTorch",
            location="pytorch.org",
            license="testLicence",
            framework="keras",
            model_type="dnn",
            test_accuracy=0.89
        )
        bias_analysis = BiasAnalysis(0.1, 0.2, 20, 10, 10, 20, 0.1, 0.2, 0.2, 0.1)
        xai_analysis = ExplainabilityAnalysis("XAI Test 2", [Metric("xai1", 0.5), Metric("xai2", 0.8)])

        mc.ai_model = aimodel
        mc.bias_analysis = bias_analysis

        is_valid = validate_mc(model_card=mc)
        self.assertFalse(is_valid)

    def test_json_conversion(self):
        """
        This tests data insertion via converting it to json, converting back to python.
        :return:
        """

        # Convert the dataclass object to JSON string using the custom encoder
        mc_json = json.dumps(self.mc, cls=ModelCardJSONEncoder, indent=4)

        # convert the json string back to python model
        mc_converted = json.loads(mc_json)

        self.assertEqual(mc_converted['input_data'], "cifar10")

    def test_json_save(self):
        """
        This tests if the MC save as json works
        :return:
        """
        save_mc(self.mc, self.mc_save_location)

        # file existing verification
        self.assertTrue(os.path.exists(self.mc_save_location), "File not found")

        # Verify the content in the file is same as the saved data
        with open(self.mc_save_location, 'r') as json_file:
            saved_data = json.load(json_file)

        mc_json = json.dumps(self.mc, cls=ModelCardJSONEncoder, indent=4)

        self.assertEqual(saved_data, mc_json, "Saved JSON data doesn't match the original Model Card")

    def tearDown(self):
        # Removing the saved file for the model card
        if os.path.exists(self.mc_save_location):
            os.remove(self.mc_save_location)


if __name__ == '__main__':
    unittest.main()