import pathlib
from functools import reduce

import streamlit as st
import pandas as pd
from clumper import Clumper


st.markdown("# Intent Example Finder")

st.sidebar.markdown("Made with love over at [Rasa](https://rasa.com/).")
st.sidebar.image(
    "https://rasahq.github.io/rasa-nlu-examples/square-logo.svg", width=100
)

clump = (Clumper.read_yaml("*/nlu.yml")
         .unpack("nlu")
         .mutate(examples=lambda d: d['examples'].split("\n"))
         .explode(example="examples")
         .mutate(example=lambda d: d["example"].replace("- ", ""))
         .keep(lambda d: len(d["example"]) > 0))

intents = clump.select("intent").drop_duplicates().map(lambda d: d['intent']).collect()
intent_selection = st.sidebar.selectbox("What model do you want to use", intents)

data = clump.keep(lambda d: d['intent'] == intent_selection).collect()
examples = "\n".join([f"     - {d['example']}" for d in data])
print(data)

text = f"""
```yaml
nlu:
  - intent: {intent_selection}
  - examples: |
{examples}
```
"""

st.markdown(text)
