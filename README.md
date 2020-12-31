# terraform-ec2module-bdd-demo

:fr: Sommaire / :gb: Table of Contents
=================

<!--ts-->

- [:fr: Description du projet](#fr-description-du-projet)
  * [Lancement des tests (Python)](#lancement-des-tests-python)
  * [Lancement des tests (Java)](#lancement-des-tests-java)
  * [Description des tests](#description-des-tests)
  * [Commandes utiles](#commandes-utiles)
- [:gb: Project Description](#gb-project-description)
  * [Launching Tests (Python)](#launching-tests-python)
  * [Launching Tests (Java)](#launching-tests-java)
  * [Tests description](#tests-description)
  * [Useful commands](#useful-commands)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


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

## Lancement des tests (Python)

### Pré-requis

1. aws CLI et authentification
  + `aws configure`
2. (optionel) (Création et) activation d'un environnement virtuel Python
  + `python -m venv $envName`
  + `./$envName/bin/activate`
3. Installation des dépendances
  + `pip install -r requirements.txt`

### Lancement des tests

1. Se déplacer dans le répertoire de test 
  + `${project.basedir}/test/default/python`
2. Lancer les tests
  + `behave`

## Lancement des tests (Java)

### Pré-requis

1. aws CLI et authentification
  + `aws configure`

### Lancement des tests

1. Se déplacer dans le répertoire de test
  + `${project.basedir}/test/default/java`
2. Lancer les tests
  + `mvn clean test`

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

## Commandes utiles

Affichage du layout pour article de blog et documentation:

```shell
tree -L 3 -I "terraform-tdd|terraform-tdd-helloworld-poc.iml|*tfstate*" --dirsfirst
.
├── examples
│   └── default
│       ├── main.tf
│       └── variables.tf
├── test
│   └── default
│       ├── java
│       ├── python
│       └── create_ec2_intances_module.feature
├── main.tf
├── outputs.tf
├── README.md
└── variables.tf

```



# :gb: Project Description

The goal of this project is to try to apply a "TDD" approach to "infrastructure as code" (it turned out to be more "BDD", but whatever). \
As a starter, we will just try to create an EC2 instance in a testing AWS account. \
We will elaborate more sophisticated cases later.

Tests are written using `Cucumber` / `Gherkin`, and there is are steps implementations for :
- Python
- Java

Next, we will try `Terratest`. \
We will then further investigate if there is a `go` implementation for `Cucumber` and if it is possible to mix it with `Terratest` 
so that we have some sort of a "single source of truth" / "golden source" for test specifications, regardless of the language,
and that would prevent specification drift if there is 1 feature file for each language / framework, that would be very likely be
get out of sync.

## Launching tests (Python)

### Pre-requisites

1. aws CLI and authentification
+ `aws configure`
2. (optional) (Create and) activate a Python virtual environment
+ `python -m venv $envName`
+ `./$envName/bin/activate`
3. Install dependencies
+ `pip install -r requirements.txt`

### Launching tests

1. Go to test directory
+ `${project.basedir}/test/default/python`
2. Launch tests
+ `behave`

## Launching tests (Java)

### Pre-requisites

1. aws CLI and authentification
+ `aws configure`

### Launching tests

1. Go to test directory
+ `${project.basedir}/test/default/java`
2. Launch tests
+ `mvn clean test`

## Tests description

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

## Useful Commands

Pretty-printing of the project layout, for blog article and documentation:

```shell
tree -L 3 -I "terraform-tdd|terraform-tdd-helloworld-poc.iml|*tfstate*" --dirsfirst
.
├── examples
│   └── default
│       ├── main.tf
│       └── variables.tf
├── test
│   └── default
│       ├── java
│       ├── python
│       └── create_ec2_intances_module.feature
├── main.tf
├── outputs.tf
├── README.md
└── variables.tf

```