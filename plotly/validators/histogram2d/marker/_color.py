import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='color', parent_name='histogram2d.marker', **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )