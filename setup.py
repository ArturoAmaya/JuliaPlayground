from julia import Main
import julia
import ipywidgets as widgets
w = widgets.IntSlider()
display(w)
julia.install()


def dry(self):
    print(w.value)


button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'  # (FontAwesome names without the `fa-` prefix)
)
button.on_click(dry)
display(button)
