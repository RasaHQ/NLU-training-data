import streamlit as st
from string import Template
from clumper import Clumper


st.markdown("# Intent Example Finder")
st.markdown("Use the selector in the sidebar to construct NLU data as a starting point.")

st.sidebar.markdown("Made with love over at [Rasa](https://rasa.com/).")
st.sidebar.image(
    "https://rasahq.github.io/rasa-nlu-examples/square-logo.svg", width=100
)

clump = (Clumper.read_yaml("*/nlu.yml")
         .unpack("nlu"))

intents = clump.select("intent").drop_duplicates().map(lambda d: d['intent']).collect()
intent_selection = st.sidebar.multiselect("What intents would you like to see?", intents, default=("bot_challenge", ))
st.sidebar.markdown("The original data is on [GitHub](https://github.com/RasaHQ/NLU-training-data).")

data = (clump
        .keep(lambda d: d['intent'] in intent_selection)
        .mutate(examples = lambda d: d['examples'].replace("- ", "      - "))
        .collect())

template = Template("  - intent: $intent\n    examples : |\n$examples")
rendered = '\n'.join([template.substitute(d) for d in data])


text = f"""
```yaml
nlu:
{rendered}
```
"""

st.markdown(text)
