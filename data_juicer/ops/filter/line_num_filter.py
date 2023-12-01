import sys

from jsonargparse.typing import PositiveInt

from data_juicer.utils.constant import Fields, InterVars, StatsKeys

from ..base_op import OPERATORS, Filter
from ..op_fusion import INTER_LINES


OP_NAME = 'line_num_filter'

@OPERATORS.register_module(OP_NAME)
@INTER_LINES.register_module(OP_NAME)
class LineNumFilter(Filter):
    """Filter to keep samples with line number within a specific
    range."""

    def __init__(self,
                 min_num: PositiveInt = 10,
                 max_num: PositiveInt = sys.maxsize,
                 *args,
                 **kwargs):
        """
        Initialization method.

        :param min_num: The min filter line number in this op, samples
            will be filtered if their line number is below this
            parameter.
        :param max_num: The max filter line number in this op, samples
            will be filtered if their line number exceeds this
            parameter.
        :param args: extra args
        :param kwargs: extra args
        """
        super().__init__(*args, **kwargs)
        self.min_num = min_num
        self.max_num = max_num

    def compute_stats(self, sample, context=False):
        # check if it's computed already
        if StatsKeys.num_line in sample[Fields.stats]:
            return sample

        context_key = f'{InterVars.lines}'
        if context and context_key in sample[Fields.context]:
            lines = sample[Fields.context][context_key]
        else:
            lines = sample[self.text_key].splitlines()
            if context:
                sample[Fields.context][context_key] = lines

        sample[Fields.stats][StatsKeys.num_line] = len(lines)
        return sample

    def process(self, sample):
        if self.min_num <= sample[Fields.stats][
                StatsKeys.num_line] <= self.max_num:
            return True
        else:
            return False
