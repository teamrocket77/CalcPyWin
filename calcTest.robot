*** Settings ***
Library           calc.py

Test Setup        Kill Calcs  
Test Teardown     Kill Calcs

*** Variables ***
${eight}=    8
*** Test Cases ***
Test 1
    [Documentation]     This Test is Purely running the calculator
    Log    "Something"
    ${Calc}=    Start Calc
    Push Num Button    ${Calc}    8
    Push Num Button    ${Calc}    0
    Push Num Button    ${Calc}    8
    Run Keyword And Expect Error    ValueError: Argument 'number' got value '+' *    Push Num Button    ${Calc}     +
    [Tags]
Test 2
    Log    "Something else" 