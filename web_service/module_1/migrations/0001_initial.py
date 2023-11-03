# Generated by Django 4.2.7 on 2023-11-03 06:56

from django.db import migrations, models
import django.db.models.deletion
import module_1.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Administrator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Administrator_Tabel",
                    models.IntegerField(verbose_name="Табельный номер администратора"),
                ),
                (
                    "Administrator_FIO",
                    models.TextField(verbose_name="ФИО администратора"),
                ),
                (
                    "Administrator_Phonenumber",
                    models.TextField(verbose_name="Номер телефона администратора"),
                ),
                (
                    "Administrator_Passport",
                    models.TextField(verbose_name="Данные паспорта администратора"),
                ),
                (
                    "Administrator_email",
                    models.TextField(verbose_name="Электронная почта администратора"),
                ),
                (
                    "Administrator_Polis",
                    models.PositiveBigIntegerField(
                        verbose_name="Полис обязательного медицинского страхования администратора"
                    ),
                ),
            ],
            options={
                "verbose_name": "Администратор",
                "verbose_name_plural": "Администраторы",
                "db_table": "Administrators",
            },
        ),
        migrations.CreateModel(
            name="Parent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Parent_Code",
                    models.IntegerField(verbose_name="Идентификатор родителя"),
                ),
                ("Parent_FIO", models.TextField(verbose_name="ФИО Родителя")),
                (
                    "Parent_Date",
                    models.DateField(verbose_name="Дата рождения родителя"),
                ),
                (
                    "Parent_Home_Propiska",
                    models.TextField(verbose_name="Адрес прописки родителя"),
                ),
                (
                    "Parent_Home",
                    models.TextField(verbose_name="Место жительства родителя"),
                ),
                ("Parent_SNILS", models.IntegerField(verbose_name="СНИЛС родителя")),
                (
                    "Parent_Phonenumeber",
                    models.TextField(verbose_name="Номер телефона родителя"),
                ),
                (
                    "Parent_Passport",
                    models.TextField(verbose_name="Данные паспорта родителя"),
                ),
            ],
            options={
                "verbose_name": "Родитель",
                "verbose_name_plural": "Родители",
                "db_table": "parents",
            },
        ),
        migrations.CreateModel(
            name="Zav_UVR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Zav_UVR_Tabel",
                    models.IntegerField(
                        verbose_name="Табельный номер заведующего учебно-воспитательной работы"
                    ),
                ),
                (
                    "Zav_UVR_FIO",
                    models.TextField(
                        verbose_name="ФИО заведующего учебно-воспитательной работы"
                    ),
                ),
                (
                    "Zav_UVR_Phonenumber",
                    models.TextField(
                        verbose_name="Номер телефона заведующего учебно-воспитательной работы"
                    ),
                ),
                (
                    "Zav_UVR_Passport",
                    models.TextField(
                        verbose_name="Данные паспорта заведующего учебно-воспитательной работы"
                    ),
                ),
                (
                    "Zav_UVR_email",
                    models.TextField(
                        verbose_name="Электронная почта заведующего учебно-воспитательной работы"
                    ),
                ),
                (
                    "Zav_UVR_Polis",
                    models.PositiveBigIntegerField(
                        verbose_name="Полис обязательного медицинского страхования заведующего учебно-воспитательной работы"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заведующий учебно-воспитательной работы",
                "verbose_name_plural": "Заведующие учебно-воспитательной работы",
                "db_table": "Zav_UVR",
            },
        ),
        migrations.CreateModel(
            name="Statement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Statement_Code", models.IntegerField(verbose_name="Код заявления")),
                (
                    "Statement_Course",
                    models.TextField(verbose_name="Выбранный обучающий курс"),
                ),
                (
                    "Statement_Group",
                    models.TextField(verbose_name="Выбранная учебная группа"),
                ),
                (
                    "Statement_Administrator_Tabel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.administrator",
                        verbose_name="Администратор, готовящий заявление",
                    ),
                ),
                (
                    "Statement_Parent_Code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.parent",
                        verbose_name="Родитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявление",
                "verbose_name_plural": "Заявления",
                "db_table": "Statements",
            },
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Child_Code", models.IntegerField(verbose_name="Код обучающегося")),
                ("Child_FIO", models.TextField(verbose_name="ФИО ребёнка")),
                ("Child_Date", models.DateField(verbose_name="Дата рождения ребёнка")),
                (
                    "Child_Home_Propiska",
                    models.TextField(verbose_name="Адрес прописки ребёнка"),
                ),
                (
                    "Child_Home",
                    models.TextField(verbose_name="Место жительства ребёнка"),
                ),
                (
                    "Child_Gender",
                    models.TextField(
                        validators=[module_1.models.gender_check],
                        verbose_name="Пол ребёнка",
                    ),
                ),
                (
                    "Child_Parent_Code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.parent",
                        verbose_name="Код родителя",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ребёнок",
                "verbose_name_plural": "Дети",
                "db_table": "children",
            },
        ),
        migrations.CreateModel(
            name="Agreement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Agreement_Code", models.IntegerField(verbose_name="Код договора")),
                (
                    "Agreement_Course",
                    models.TextField(verbose_name="Выбранный обучающий курс"),
                ),
                (
                    "Agreement_Group",
                    models.TextField(verbose_name="Выбранная учебная группа"),
                ),
                (
                    "Agreement_Requisites",
                    models.TextField(verbose_name="Реквизиты банка от компании"),
                ),
                (
                    "Agreement_Price",
                    models.IntegerField(verbose_name="Цена предоставления услуг"),
                ),
                (
                    "Agreement_Administrator_Tabel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.administrator",
                        verbose_name="Администратор, готовящий заявление, являющееся основанием заключения договора",
                    ),
                ),
                (
                    "Agreement_Parent_Code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.parent",
                        verbose_name="Родитель",
                    ),
                ),
                (
                    "Agreement_Statement_Code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.statement",
                        verbose_name="Заявление, являющееся основанием заключения договора",
                    ),
                ),
                (
                    "Agreement_Zav_UVR_Tabel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="module_1.zav_uvr",
                        verbose_name="Заведующий учебно-воспитательной работой, готовящий договор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Итоговый договор",
                "verbose_name_plural": "Итоговые договора",
                "db_table": "Agreements",
            },
        ),
    ]
