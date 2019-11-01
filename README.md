# Rasa Training Data
Crowd-sourced training data for the development and testing of Rasa NLU models. 

### About this repository 

This repository is open for contributions and we very much appreciate your support in expanding the collection of training data available to the community!

Each folder is a category of training data. Within each category there is an `NLU.md` file containing the training data sectioned by intent type and a `README.md` file, listing the intent types contained in `NLU.md`.

### Categories 

* [Banking](https://github.com/RasaHQ/rasa-training-data/tree/master/banking)
* [Generic](https://github.com/RasaHQ/rasa-training-data/tree/master/greetings)
* [Mood](https://github.com/RasaHQ/rasa-training-data/tree/master/mood)
* [Weather](https://github.com/RasaHQ/rasa-training-data/tree/master/weather)

---  

### How to contribute

To contribute via pull request, follow these steps:

1. Create an issue describing the training data you would like to contribute 

2. Decide if you would like to contribute to an existing category or create a new one. 
   * Each category contains an `NLU.md` file with multiple intents, if the category you would like to create only contains one intent, consider if it can be contributed as part of another category. 

3. Format your training data using markdown in the `NLU.md` file, 
   * Title each section of intents with the type of intent e.g. `intent:mood_happy` or `intent:mood_unhappy`

4. Update the `README.md` file including a list of the type of intents contained in your folder. 

5. Create a pull request describing your changes 

Your pull request will be reviewed by a maintainer, who will get back to you about any necessary changes or questions. You will also be asked to sign a Contributor License Agreement.

---  

### About Rasa

<img align="right" height="244" src="https://i.imgur.com/YR7ziAx.png">

- **What does Rasa do? 🤔**
  [Check out our Website](https://rasa.com/)

- **I'm new to Rasa 😄**
  [Get Started with Rasa](https://rasa.com/docs/getting-started/)

- **I'd like to read the detailed docs 🤓**
  [Read The Docs](https://rasa.com/docs/)

- **I'm ready to install Rasa 🚀**
  [Installation](https://rasa.com/docs/rasa/user-guide/installation/)

- **I want to learn how to use Rasa 🚀**
  [Tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)

- **I have a question ❓**
  [Rasa Community Forum](https://forum.rasa.com/)

- **I would like to contribute 🤗**
  [How to Contribute](#how-to-contribute)
