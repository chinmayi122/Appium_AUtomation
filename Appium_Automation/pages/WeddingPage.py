from base.BasePage import BasePage


class WeddingPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        print(driver.page_source)


    #Locator Values in Wedding Page

    _createWedding="//android.widget.Button[@content-desc='Create New Wedding']"  #xapth
    _yourRole="(//android.view.View[@content-desc='Create a new Wedding']/following-sibling::android.view.View)[1]"
    _selectYourRole="//android.widget.RadioButton[@content-desc='Event Manager']"
    _doneButton="//android.widget.Button[@content-desc='Done']"
    _weddingDate="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]"
    _selectWeddingDate="new UiSelector().className('android.view.View').instance(39)"
    _okButton="//android.widget.Button[@content-desc='OK']"
    _bridesName="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
    _enterBridesName="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]"
    _groomsName="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[4]"
    _createWeddingButton="//android.widget.Button[@content-desc='Create Wedding']"
    _createdWedding="((//android.view.View)[7]/..//android.widget.ImageView)[last()]"


    def createWedding(self):
        self.ClickElement(self._createWedding,"xpath")

    def yourRole(self):
        self.ClickElement(self._yourRole,"xpath")

    def selectYourRole(self):
        self.ClickElement(self._selectYourRole,"xpath")

    def doneBUtton(self):
        self.ClickElement(self._doneButton,"xpath")

    def WeddingDate(self):
        self.ClickElement(self._weddingDate, "xpath")

    def selectWeddingDate(self):
        self.ClickElement(self._selectWeddingDate, "index")


    def okBUtton(self):
            self.ClickElement(self._okButton, "xpath")

    def bridesNameClick(self):
            self.ClickElement(self._bridesName,"xpath")

    def bridesName(self):
            self.SendKeys("999999997",self._enterBridesName,"xpath")

    def groomsName(self):
            self.SendKeys("Nishanth",self._groomsName,"xpath")

    def createWeddingButton(self):
            self.ClickElement(self._createWeddingButton, "xpath")

    def weddingCreated(self):
            self.ClickElement(self._createdWedding, "xpath")