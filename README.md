# ICICLE Model Card

### How to run

1. In your colab notebook run the following command to install the Model Card
```shell
!pip install 'git+https://github.com/swsachith/icicle_model_card.git'
```

2. Import the Model Card
```python
from icicle_model_card.icicle_model_card import ModelCard
```

3. Initialize the Model Card
```python
mc = ModelCard(
            name="test-mc",
            version="test-version",
            short_description="short desc",
            full_description="full_desc",
            keywords="test keyword",
            author="test author"
        )
```

4. Add details to the Model Card
```python
mc.input_data = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
```

5. Get the JSON version of the Model Card
```python
print(mc)
```