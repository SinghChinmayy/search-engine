from pipeline.loaders.loaders import TxtLoader
from pipeline.processor.normalizer import TextNormalization
from pipeline.processor.tokenizer import TextTokenize
class pipeline:
    def __init__(self, path):
        self.path = path

    def tokens(self):
        # loading text
        input_text = TxtLoader(self.path)

        # normalization
        obj = TextNormalization(input_text.load())

        normalized = obj.normalize()

        # tokenization
        tokens_obj = TextTokenize(normalized)
        tokens = tokens_obj.tokenize()
        return tokens
