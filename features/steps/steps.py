"""
Feature: Vending Machine accepts Quarters, Dimes, and Nickles. It does not accept pennies

  Scenario: Vending Machine accepts quarters
    Given I have a "Quarter"
    When I insert a "Quarter" into the vending machine
    Then the vending machine accepts the "Quarter"

  Scenario: Vending Machine accepts Dimes
    Given I have a "Dime"
    When I insert a "Dime" into the vending machine
    Then the vending machine accepts the "Dime"

  Scenario: Vending Machine accepts Nickels
    Given I have a "Nickel"
    When I insert a "Nickel" into the vending machine
    Then the vending machine accepts the "Nickel"

  Scenario: Vending Machine does not accept Pennies
    Given I have a "Penny"
    When I insert a "Penny" into the vending machine
    Then the vending machine does not accepts the coin

Feature: Payment Feature
  Acceptance criteria for the vending machine

  Scenario: Customer orders an item
    Given I am a vendor
    When I go to order an item
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".25" dollar
    When I insert ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I am a vendor
    And order an item for ".50" dollar
    When I insert ".25"
    Then the displays says "Insert Coins"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".25"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"

  Scenario: Customer pays for item
    Given I purchase an item for ".50"
    And I have inserted ".30"
    And display says "Insert Coins"
    When I insert another ".25"
    Then the displays says "Thank you"
    And ".05" cents is returned

Feature: Product Feature
  Acceptance criteria for selecting various products from the vending machine

  Scenario: Customer orders Chips
    Given I order "Chips" for ".50"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Cola
    Given I order "Cola" for "1.00"
    When I select the respective button
    And I have inserted "4" "Quarter"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer orders Candy
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    And I have inserted "1" "Dime"
    And I have inserted "1" "Nickle"
    Then the product is dispensed
    And the machine displays "Thank you"

  Scenario: Customer does not have enough coins to complete transaction
    Given I order "Candy" for ".65"
    When I select the respective button
    And I have inserted "2" "Quarter"
    Then the machine displays "Insert Coins"
"""
from behave import given, when, then
from src.model.dime import Dime
from src.model.nickel import Nickel
from src.model.penny import Penny
from src.model.quarter import Quarter



@given(u'I have a "Quarter"')
def step_impl(context):
    context.quarter = Quarter()


@when(u'I insert a "Quarter" into the vending machine')
def step_impl(context):
    context.vending_machine.insert_coins(context.quarter)


@then(u'the vending machine accepts the "Quarter"')
def step_impl(context):
    assert context.vending_machine.accepted_coins == [context.quarter]


@given(u'I have a "Dime"')
def step_impl(context):
    context.dime = Dime()


@when(u'I insert a "Dime" into the vending machine')
def step_impl(context):
    context.vending_machine.insert_coins(context.dime)


@then(u'the vending machine accepts the "Dime"')
def step_impl(context):
    assert context.vending_machine.accepted_coins == [context.dime]


@given(u'I have a "Nickel"')
def step_impl(context):
    context.nickel = Nickel()


@when(u'I insert a "Nickel" into the vending machine')
def step_impl(context):
    context.vending_machine.insert_coins(context.nickel)


@then(u'the vending machine accepts the "Nickel"')
def step_impl(context):
    assert context.vending_machine.accepted_coins == [context.nickel]


@given(u'I have a "Penny"')
def step_impl(context):
    context.penny = Penny()


@when(u'I insert a "Penny" into the vending machine')
def step_impl(context):
    context.vending_machine.insert_coins(context.penny)


@then(u'the vending machine does not accepts the coin')
def step_impl(context):
    assert context.vending_machine.accepted_coins == []


@given(u'I am a vendor')
def step_impl(context):
    pass


@when(u'I go to order an item')
def step_impl(context):
    pass


@then(u'the displays says "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == "Insert Coins"


@given(u'order an item for ".25" dollar')
def step_impl(context):
    pass


@when(u'I insert ".25"')
def step_impl(context):
    context.vending_machine.insert_coins(Quarter())


@then(u'the displays says "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == "Thank you"


@given(u'order an item for ".50" dollar')
def step_impl(context):
    pass


@given(u'I purchase an item for ".50"')
def step_impl(context):
    pass


@given(u'I have inserted ".25"')
def step_impl(context):
    context.vending_machine.insert_coins(Quarter())


@given(u'display says "Insert Coins"')
def step_impl(context):
    pass


@when(u'I insert another ".25"')
def step_impl(context):
    context.vending_machine.insert_coins(Quarter())


@given(u'I have inserted ".30"')
def step_impl(context):
    context.vending_machine.insert_coins(Quarter())
    context.vending_machine.insert_coins(Quarter())
    context.vending_machine.insert_coins(Dime())


@then(u'".05" cents is returned')
def step_impl(context):
    assert context.vending_machine.returned_coins == [Nickel()]


@given(u'I order "Chips" for ".50"')
def step_impl(context):
    pass


@when(u'I select the respective button')
def step_impl(context):
    pass


@when(u'I have inserted "2" "Quarter"')
def step_impl(context):
    context.vending_machine.insert_coins(Quarter())
    context.vending_machine.insert_coins(Quarter())


@then(u'the product is dispensed')
def step_impl(context):
    pass


@then(u'the machine displays "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == "Thank you"


@given(u'I order "Cola" for "1.00"')
def step_impl(context):
    pass


@when(u'I have inserted "4" "Quarter"')
def step_impl(context):
    pass


@given(u'I order "Candy" for ".65"')
def step_impl(context):
    pass


@when(u'I have inserted "1" "Dime"')
def step_impl(context):
    pass


@when(u'I have inserted "1" "Nickle"')
def step_impl(context):
    pass


@then(u'the machine displays "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == "Insert Coins"