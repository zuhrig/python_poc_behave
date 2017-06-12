Feature: Vial entry Smoke Test Suite -> happy path flow
  Background: Login To CLIA
    Given I am logged to clia

  Scenario Outline: Vial Barcode inputs
     Given we are on protocol 5330
     When we search by an existing <id>
     Then we should see that <id> info displayed

     Examples: id_types
        | id              |
        | vial_barcode_id |
        | qr_decoded_id   |

  Scenario Outline: Vial form inputs
     Given we search by an existing vial_barcode_id
     Then we should see that <form_id> displayed as <type>
     And we should be able to set <fill_data> in <form_id>
     And we should be able to submit it

     Examples: form_test_data
        | form_id        | type        | fill_data       |
        | supervisor     | select_list | Juan Bustamante |
        | arrival_date   | date_picker | 21-Jun-2017     |

  Scenario: Check consistency
      Given we have submitted a vial
      When I search in on the DB
      Then we should have the same data in the DB
