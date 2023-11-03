# Generated by Django 4.2.7 on 2023-11-03 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("module_1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="child",
            name="Child_Parent_Code",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="module_1.parent",
                verbose_name="Идентификатор родителя",
            ),
        ),
        migrations.AlterField(
            model_name="parent",
            name="Parent_Code",
            field=models.IntegerField(verbose_name="Код родителя"),
        ),
    ]