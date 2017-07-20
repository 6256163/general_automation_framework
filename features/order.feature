@tags @tag
Feature: Order
    User can new order and audit order to make it switch to correct type and state.

    Background: Launch browser
        Given browser should be launched
            |browser|
            |chrome |
        And login page is opened
        When input user login info and submit
             |key|value|
             |username|2|
             |password|123456|
             |verifycode|imqa|
        Then show the index page


    Scenario: new order
        Given navigate to order_list page

