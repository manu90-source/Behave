from behave import given  ,when,then

# --- GIVEN STEPS ---

@given('The account balance is ${balance:d}')
def step_impl(context, balance):
    # 'context' is used to store data between steps
    context.account_balance = balance

@given('the card is valid')
def step_impl(context):
    context.card_is_valid = True

@given('the machine contains enough money')
def step_impl(context):
    context.atm_machine_balance = 1000  # Default machine logic

# --- WHEN STEPS ---

@when('the Account Holder requests ${amount:d}')
def step_impl(context, amount):
    context.requested_amount = amount
    # Logic: Deduct money if funds are sufficient
    if context.account_balance >= amount:
        context.dispensed_amount = amount
        context.account_balance -= amount
    else:
        context.dispensed_amount = 0

# --- THEN STEPS ---
#add comment changes 


@then('the ATM should dispense ${dispensed_amount:d}')
def step_impl(context, dispensed_amount):
    assert context.dispensed_amount == dispensed_amount, \
        f"Expected {dispensed_amount}, but got {context.dispensed_amount}"

@then('the account balance should be ${remaining_balance:d}')
def step_impl(context, remaining_balance):
    assert context.account_balance == remaining_balance, \
        f"Expected {remaining_balance}, but balance is {context.account_balance}"

@then('the card should be returned')
def step_impl(context):
    # In a real Selenium test, you'd check for a UI message here
    print("Card has been ejected.")