from collections import OrderedDict
from dataclasses import dataclass, field
from operator import itemgetter
from time import time
from typing import Text, MutableMapping, Any, Callable


@dataclass
class Measurer:
    title: Text
    measurements: MutableMapping[Text, float] = field(default_factory=dict)

    def time_it(self, meta: Text, function: Callable[[...], Any], *args, **kwargs) -> Any:
        start = time()

        result = function(*args, **kwargs)

        end = time()

        delta = end - start

        self.measurements[meta] = delta

        return result

    def visualize(self) -> None:
        items = self.measurements.items()

        sorted_items = sorted(items, key=itemgetter(1))

        places = OrderedDict(sorted_items)

        print("Tests:", self.title)

        for index, (meta, measure) in enumerate(places.items(), 1):
            print(f" {meta} ({index} place)")
            print(f"  Takes {measure} seconds")
