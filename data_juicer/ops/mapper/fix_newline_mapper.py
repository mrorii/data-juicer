import re

from ..base_op import OPERATORS, Mapper

OP_NAME = 'fix_newline_mapper'

DOUBLE_ESCAPED_NEWLINE_REGEX = re.compile(r'\\n')

@OPERATORS.register_module(OP_NAME)
class FixNewlineMapper(Mapper):
    """Mapper to fix incorrect newlines in text samples."""

    def __init__(self, *args, **kwargs):
        """
        Initialization method.

        :param args: extra args
        :param kwargs: extra args
        """
        super().__init__(*args, **kwargs)

    def process(self, sample):
        sample[self.text_key] = DOUBLE_ESCAPED_NEWLINE_REGEX.sub(
            '\n', sample[self.text_key]
        )
        return sample
