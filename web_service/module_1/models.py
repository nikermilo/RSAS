from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


def gender_check(Child_Gender):
    if Child_Gender not in ["Мужской", "Женский"]:
        raise ValidationError(
            gettext_lazy('%(Child_Gender)s is wrong gender'),
            params={'Child_Gender': Child_Gender},
        )

class Parent(models.Model):
    """"Родители"""

    class Meta:
        db_table = "parents"
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    Parent_Code = models.IntegerField(verbose_name="Код родителя")
    Parent_FIO = models.TextField(verbose_name="ФИО Родителя")
    Parent_Date = models.DateField(verbose_name="Дата рождения родителя")
    Parent_Home_Propiska = models.TextField(verbose_name="Адрес прописки родителя")
    Parent_Home = models.TextField(verbose_name="Место жительства родителя")
    Parent_SNILS = models.IntegerField(verbose_name="СНИЛС родителя")
    Parent_Phonenumeber = models.TextField(verbose_name="Номер телефона родителя")
    Parent_Passport = models.TextField(verbose_name="Данные паспорта родителя")

    def __str__(self):
        return f"{self.Parent_FIO} {self.Parent_Date} {self.Parent_Home_Propiska} {self.Parent_Home} {self.Parent_SNILS}
        {self.Parent_Phonenumeber} {self.Parent_Passport} {self.Parent_Code}"

class Child(models.Model):
    """"Дети"""

    class Meta:
        db_table = "children"
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"

    Child_Code = models.IntegerField(verbose_name="Код обучающегося")
    Child_FIO = models.TextField(verbose_name="ФИО ребёнка")
    Child_Date = models.DateField(verbose_name="Дата рождения ребёнка")
    Child_Home_Propiska = models.TextField(verbose_name="Адрес прописки ребёнка")
    Child_Home = models.TextField(verbose_name="Место жительства ребёнка")
    Child_Gender = models.TextField(verbose_name="Пол ребёнка", validators=[gender_check])
    Child_Parent_Code = models.ForeignKey(Parent, on_delete=models.RESTRICT, verbose_name="Код родителя")

    def __str__(self):
        return f"{self.Child_Code} {self.Child_Date} {self.Child_FIO} {self.Child_Gender} {self.Child_Home} {self.Child_Home_Propiska} {self.Child_Parent_Code}"

class Administrator(models.Model):
    """"Администраторы"""

    class Meta:
        db_table = "Administrators"
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"

    Administrator_Tabel = models.IntegerField(verbose_name="Табельный номер администратора")
    Administrator_FIO = models.TextField(verbose_name="ФИО администратора")
    Administrator_Phonenumber = models.TextField(verbose_name="Номер телефона администратора")
    Administrator_Passport = models.TextField(verbose_name="Данные паспорта администратора")
    Administrator_email = models.TextField(verbose_name="Электронная почта администратора")
    Administrator_Polis = models.PositiveBigIntegerField(verbose_name="Полис обязательного медицинского страхования администратора")


    def __str__(self):
        return f"{self.Administrator_FIO} {self.Administrator_Phonenumber} {self.Administrator_Passport} {self.Administrator_email}
        {self.Administrator_Polis} {self.Administrator_Tabel}"

class Zav_UVR(models.Model):
    """"Заведующий учебно-воспитательной работы"""

    class Meta:
        db_table = "Zav_UVR"
        verbose_name = "Заведующий учебно-воспитательной работы"
        verbose_name_plural = "Заведующие учебно-воспитательной работы"

    Zav_UVR_Tabel = models.IntegerField(verbose_name="Табельный номер заведующего учебно-воспитательной работы")
    Zav_UVR_FIO = models.TextField(verbose_name="ФИО заведующего учебно-воспитательной работы")
    Zav_UVR_Phonenumber = models.TextField(verbose_name="Номер телефона заведующего учебно-воспитательной работы")
    Zav_UVR_Passport = models.TextField(verbose_name="Данные паспорта заведующего учебно-воспитательной работы")
    Zav_UVR_email = models.TextField(verbose_name="Электронная почта заведующего учебно-воспитательной работы")
    Zav_UVR_Polis = models.PositiveBigIntegerField(verbose_name="Полис обязательного медицинского страхования заведующего учебно-воспитательной работы")


    def __str__(self):
        return f"{self.Zav_UVR_FIO} {self.Zav_UVR_Phonenumber} {self.Zav_UVR_Passport} {self.Zav_UVR_email} {self.Zav_UVR_Polis} {self.Zav_UVR_Tabel}"
    
class Statement(models.Model):
    """Заявление"""

    class Meta:
        db_table = "Statements"
        verbose_name = "Заявление"
        verbose_name_plural = "Заявления"

    Statement_Code = models.IntegerField(verbose_name="Код заявления")
    Statement_Parent_Code = models.ForeignKey(Parent, on_delete=models.RESTRICT, verbose_name="Родитель")
    Statement_Administrator_Tabel = models.ForeignKey(Administrator, on_delete=models.RESTRICT, verbose_name="Администратор, готовящий заявление")
    Statement_Course = models.TextField(verbose_name="Выбранный обучающий курс")
    Statement_Group = models.TextField(verbose_name="Выбранная учебная группа")

    def __str__(self):
        return f"{self.Statement_Code} {self.Statement_Parent_Code} {self.Statement_Administrator_Tabel} {self.Statement_Course} {self.Statement_Group}"

class Agreement(models.Model):
    """Итоговый договор"""

    class Meta:
        db_table = "Agreements"
        verbose_name = "Итоговый договор"
        verbose_name_plural = "Итоговые договора"

    Agreement_Code = models.IntegerField(verbose_name="Код договора")
    Agreement_Parent_Code = models.ForeignKey(Parent, on_delete=models.RESTRICT, verbose_name="Родитель")
    Agreement_Zav_UVR_Tabel = models.ForeignKey(Zav_UVR, on_delete=models.RESTRICT, verbose_name="Заведующий учебно-воспитательной работой, готовящий договор")
    Agreement_Statement_Code = models.ForeignKey(Statement, on_delete=models.RESTRICT, verbose_name="Заявление, являющееся основанием заключения договора")
    Agreement_Administrator_Tabel = models.ForeignKey(Administrator, on_delete=models.RESTRICT,
                                                      verbose_name="Администратор, готовящий заявление, являющееся основанием заключения договора")
    Agreement_Course = models.TextField(verbose_name="Выбранный обучающий курс")
    Agreement_Group = models.TextField(verbose_name="Выбранная учебная группа")
    Agreement_Requisites = models.TextField(verbose_name="Реквизиты банка от компании")
    Agreement_Price = models.IntegerField(verbose_name="Цена предоставления услуг")

    def __str__(self):
        return f"{self.Agreement_Code} {self.Agreement_Parent_Code} {self.Agreement_Zav_UVR_Tabel} {self.Agreement_Statement_Code} {self.Agreement_Administrator_Tabel}
        {self.Agreement_Course} {self.Agreement_Group} {self.Agreement_Requisites} {self.Agreement_Price}"
    