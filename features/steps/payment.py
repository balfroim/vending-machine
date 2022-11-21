"""
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
"""
from behave import given, when, then
from src.vending_machine import VendingMachine

@given('I am a vendor')
def step_impl(context):
    context.vending_machine = VendingMachine()

@when('I go to order an item')
def step_impl(context):
    context.vending_machine.order_item()

@then('the displays says "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == "Insert Coins"

@when('I insert "{coin}"')
def step_impl(context, coin):
    context.vending_machine.insert_coin(coin)

@then('the displays says "Thank you"')
def step_impl(context):
    assert context.vending_machine.display == "Thank you"

@when('I purchase an item for "{price}"')
def step_impl(context, price):
    context.vending_machine.order_item(price)

@then('"{change}" cents is returned')
def step_impl(context, change):
    assert context.vending_machine.change == float(change)

@given('I insert another "{coin}"')
def step_impl(context, coin):
    context.vending_machine.insert_coin(coin)

@given(u'order an item for ".25" dollar')
def step_impl(context):
    context.vending_machine.order_item(".25")


@given(u'order an item for ".50" dollar')
def step_impl(context):
    context.vending_machine.order_item(".50")


@given(u'I purchase an item for ".50"')
def step_impl(context):
    context.vending_machine.order_item(".50")


@given(u'I have inserted ".25"')
def step_impl(context):
    context.vending_machine.insert_coin(".25")


@given(u'display says "Insert Coins"')
def step_impl(context):
    assert context.vending_machine.display == "Insert Coins"


@when(u'I insert another ".25"')
def step_impl(context):
    context.vending_machine.insert_coin(".25")


@given(u'I have inserted ".30"')
def step_impl(context):
    context.vending_machine.insert_coin(".30")