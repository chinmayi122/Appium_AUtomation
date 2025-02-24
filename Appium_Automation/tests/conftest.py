import pytest
import time
from base.DriverClass import Driver

@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print("Before CLass")
    driver1 = Driver()
    #driver= driver1.getremoteServer()
    driver=driver1.getremoteServer()

    if request.cls is not None:
        request.cls.driver=driver

    yield  driver
    time.sleep(3)
    driver.quit()
    print("After CLass")


@pytest.yield_fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")