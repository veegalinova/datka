from typing import Callable, TypeVar, Sequence

from IPython.display import display, clear_output, Image
import ipywidgets as widgets


ItemT = TypeVar("ItemT")


class DatasetWidget:
    def __init__(self, items: Sequence[ItemT], display_fn: Callable[[ItemT], None]):
        self.images = items
        self.display_fn = display_fn

        self.output = widgets.Output()
        self.forward_button = widgets.Button(icon="arrow-right")
        self.backward_button = widgets.Button(icon="arrow-left")
        self.buttons_box = widgets.HBox(
            children=(self.backward_button, self.forward_button)
        )
        self.widget = widgets.VBox(children=(self.buttons_box, self.output))

        self.current_image_index = -1
        self.total_images = len(self.images)
        self.show_widget()

    def next_image_handler(self, obj):
        self.current_image_index += 1
        if self.current_image_index >= self.total_images:
            self.current_image_index = 0

        with self.output:
            clear_output(wait=True)
            self.display_fn(self.images[self.current_image_index])

    def previous_image_handler(self, obj):
        self.current_image_index -= 1

        if self.current_image_index < 0:
            self.current_image_index = 0

        with self.output:
            clear_output(wait=True)
            self.display_fn(self.images[self.current_image_index])

    def show_widget(self):
        display(self.widget)
        self.forward_button.on_click(self.next_image_handler)
        self.backward_button.on_click(self.previous_image_handler)
        self.next_image_handler(None)
