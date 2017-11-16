from compare import expect
@given(u'I have ${Valor1} in my account')
def step_impl(context,Valor1):
    context.Valor1=int(Valor1)

@when(u'I choose to withdraw the fixed amount of ${Valor2}')
def step_impl(context, Valor2):
    context.withdraw=int(Valor2)

@then(u'I should receive ${Valor3} cash')
def step_impl(context, Valor3):
    print("This is your $", Valor3)


@then(u'the balance of my account should be ${Valor4}')
def step_impl(context, Valor4):
    remaining=context.Valor1-context.withdraw
    expect(remaining).to_equal(int(Valor4))

