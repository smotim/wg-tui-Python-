import npyscreen

class FormOne(npyscreen.Form):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is form one")

class FormTwo(npyscreen.Form):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is form two")

class FormThree(npyscreen.Form):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is form three")

class FormFour(npyscreen.Form):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is form four")

class FormFive(npyscreen.Form):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is form five")

class MenuForm(npyscreen.FormWithMenus):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name="This is the menu form")
        menu = self.add_menu(name="Menu", shortcut="^M")
        menu.addItem(text="Form One", onSelect=self.switch_to_form_one)
        menu.addItem(text="Form Two", onSelect=self.switch_to_form_two)
        menu.addItem(text="Form Three", onSelect=self.switch_to_form_three)
        menu.addItem(text="Form Four", onSelect=self.switch_to_form_four)
        menu.addItem(text="Form Five", onSelect=self.switch_to_form_five)
        menu.addItem(text="Exit", onSelect=self.exit_app)

    def switch_to_form_one(self):
        self.parentApp.switchForm("ONE")

    def switch_to_form_two(self):
        self.parentApp.switchForm("TWO")

    def switch_to_form_three(self):
        self.parentApp.switchForm("THREE")

    def switch_to_form_four(self):
        self.parentApp.switchForm("FOUR")

    def switch_to_form_five(self):
        self.parentApp.switchForm("FIVE")

    def exit_app(self):
        self.parentApp.setNextForm(None)
        self.editing = False

class MenuApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MenuForm, name="Menu")
        self.addForm("ONE", FormOne, name="Form One")
        self.addForm("TWO", FormTwo, name="Form Two")
        self.addForm("THREE", FormThree, name="Form Three")
        self.addForm("FOUR", FormFour, name="Form Four")
        self.addForm("FIVE", FormFive, name="Form Five")

if __name__ == "__main__":
    app = MenuApp()
    app.run()
