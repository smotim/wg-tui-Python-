import npyscreen


class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department',
                                     values=['Указать путь до конфига', 'Установить соединение', 'Проверить соединение'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')


class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myEmployeeForm, name='Wg-tui')
        # A real application might define more forms here.......


if __name__ == '__main__':
    TestApp = MyApplication().run()
