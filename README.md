# terraform-tdd-helloworld-poc

:fr: Sommaire / :gb: Table of Contents
=================

<!--ts-->

* [Documentation en français](#fr-description-du-projet)
* [English Documentation (coming soon)](#gb-project-description-coming-soon )

---

# :fr: Description du projet

Le but de ce projet est de chercher à appliquer une approche TDD à de "l'infra as code". \
Pour Démarrer, on va juste chercher à créer en TDD une instance EC2 dans un compte AWS de test. \
On élaborera des cas plus sophistiqués par la suite.

Les tests sont décrits avec `Cucumber` / `Gherkin`, et il y a une implémentation des steps:
- en Python
- en Java

Par la suite, nous essaierons d'implémenter des tests via `Terratest`. \
On investiguera s'il y a une implémentation `go` de `Cucumber` et s'il est possible de le mixer avec `Terratest`
pour avoir une "single source of truth" / "golden source" quant à la spécification des tests, et ce même cross-langage !

## lancement des tests (Python)

### Pré-requis

1. aws CLI et authentification
  - `aws configure`
2. (optionel) (Création et) activation d'un environnement virtuel Python
  - `python -m venv $envName`
  - `./$envName/bin/activate`
3. Installation des dépendances
  - `pip install -r requirements.txt`
4. Lancement des tests
  - `behave`

## lancement des tests (Java)

1. Se déplacer dans le répertoire de test 
  -`${project.basedir}/main/test-java`
2. Lancer les tests
  -`mvn clean test`

## Description des tests

```gherkin
Feature: ec2 creation module

  Background: a "clean" region
    Given the region "eu-west-3"
    And an account with only the default VPC
    And no EC2 instance

  Scenario: create an EC2 instance
    When i create the following EC2 instance in the default VPC
      | instance_type | instance_count |
      | t2.micro      | 1              |
    Then there is exactly 1 instance with the following attributes
      | instance_type |
      | t2.micro      |
```

# :gb: Project Description (Coming soon)