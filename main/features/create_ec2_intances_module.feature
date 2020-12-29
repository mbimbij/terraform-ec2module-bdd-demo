Feature: ec2 creation module

  Background: a "clean" account
    Given the region "eu-west-3"
    And an account with only the default VPC
    And no EC2 instance

  Scenario: create an EC2 instance
    When i create the following EC2 instance in the default VPC
      | model | t2.micro |
      | count | 1        |
    Then there is exactly 1 instance with the following attributes
      | model | t2.micro |