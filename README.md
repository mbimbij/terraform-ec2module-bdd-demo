# terraform-tdd-helloworld-poc

:fr: Sommaire / :gb: Table of Contents
=================

<!--ts-->

* [Documentation en français](#fr-description-du-projet)
* [English Documentation (coming soon)](#gb-project-description-coming-soon )

---

# :fr: Description du projet

Le but de ce projet est de chercher à appliquer une approche TDD à de "l'infra as code".

Pour Démarrer, on va juste chercher à créer en TDD une instance EC2 dans un compte AWS de test.

On élaborera des cas plus sophistiqués par la suite

## lancement des tests

### Pré-requis

1. (optionel) (Création et) activation d'un environnement virtuel Python
  - `python -m venv $envName`
  - `./$envName/bin/activate`
2. Installation des dépendances
  - `pip install -r requirements.txt`
3. Lancement des tests
  - `behave`

## tests

```gherkin
Background: a "clean" account
Given an account with a default VPC
And no EC2 instance
And the default region "eu-west-3"

When i create the following EC2 instance in the default VPC
|model|t2.micro|
|count|1       |
Then there is exactly 1 instance with the following attributes
|model|t2.micro|
```

# :gb: Project Description (Coming soon)