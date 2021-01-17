# Datka

------------
Misc tools for image data visualization and analysis.
##Installation

--------

```bash
pip install https://github.com/veegalinova/datka
```
## Example

----------
### Jupyter Widgets
#### Visualizing CIFAR-10

```python
import torchvision
import matplotlib.pyplot as plt

# Define your dataset
dataset = torchvision.datasets.CIFAR10(
    root="./data", train=False, download=True
)
classes = (
    'plane', 'car', 'bird', 'cat',
    'deer', 'dog', 'frog', 'horse', 'ship', 'truck'
)


# Define your visualization function
def visualize_my_dataset(data):
    image, label = data
    label = classes[label]
    plt.suptitle(label, fontsize=22)
    plt.imshow(image)
    plt.show()


# Visualize
from datka.jupyter.widgets import DatasetWidget

DatasetWidget(items=dataset, display_fn=visualize_my_dataset)
```
![Alt Text](docs/dataset_widget.gif)
