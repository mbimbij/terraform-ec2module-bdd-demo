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