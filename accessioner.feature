Feature: Accessioner

  Scenario: Set select list and vial info
      Given we are on protocol 5330
      And I set a random supervisor
      And I set a testtube
      Then I should see the sample-tubeundefined table
