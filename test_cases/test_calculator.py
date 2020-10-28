from packages.client import Calculator

calc = Calculator(base_url="http://165.22.81.75:8090/test/calculate")


def test_sum_1():

    request = calc.create_request(num1=2, num2=3, action="+")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": 5\n}\n'

def test_sum_2():

    request = calc.create_request(num1=-5, num2=-5, action="+")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": -10\n}\n'

def test_sub_1():

    request = calc.create_request(num1=5, num2=3, action="-")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": 2\n}\n'

def test_sub_2():

    request = calc.create_request(num1=5, num2=9, action="-")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": -4\n}\n'

def test_mult_1():

    request = calc.create_request(num1=4, num2=4, action="*")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": 16\n}\n'

def test_mult_2():

    request = calc.create_request(num1=-2, num2=4, action="*")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": -8\n}\n'

def test_div_1():

    request = calc.create_request(num1=8, num2=2, action="/")
    response = calc.send_request(request)

    assert response.text == '{\n  "result": 4\n}\n'

def test_div_2():

    request = calc.create_request(num1=8, num2=0, action="/")
    response = calc.send_request(request)

    assert response.text == 'Cannot divide by zero'
