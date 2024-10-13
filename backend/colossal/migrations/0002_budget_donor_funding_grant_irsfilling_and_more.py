# Generated by Django 5.1.2 on 2024-10-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colossal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Budget",
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
                ("programName", models.CharField(max_length=100)),
                ("budgetedAmount", models.FloatField()),
                ("actualSpent", models.FloatField()),
                ("remainingBalance", models.FloatField()),
                ("notes", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Donor",
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
                ("donorName", models.CharField(max_length=100)),
                ("donationDate", models.DateField()),
                ("totalAmount", models.FloatField()),
                ("allocatedAmount", models.FloatField()),
                ("remainingBalance", models.FloatField()),
                ("receiptIssued", models.DateField()),
                ("followupDate", models.DateField()),
                ("formRequired", models.BooleanField()),
                ("acknowledgmentLetterSent", models.BooleanField()),
                ("notes", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Funding",
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
                ("source", models.CharField(max_length=100)),
                ("restricted", models.BooleanField()),
                ("totalAmount", models.FloatField()),
                ("allocatedAmount", models.FloatField()),
                ("remainingBalance", models.FloatField()),
                ("restrictions", models.CharField(default="", max_length=500)),
                ("notes", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Grant",
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
                ("name", models.CharField(max_length=100)),
                ("grantor", models.CharField(max_length=100)),
                ("grantAmount", models.FloatField()),
                ("allocated", models.FloatField()),
                ("remaining", models.FloatField()),
                ("restrictions", models.CharField(default="", max_length=100)),
                ("dueDate", models.DateField()),
                ("notes", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="IrsFilling",
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
                ("fillingType", models.CharField(max_length=100)),
                ("dueDate", models.DateField()),
                ("status", models.CharField(default="", max_length=100)),
                ("notes", models.CharField(default="", max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name="income_statement",
            new_name="IncomeStatement",
        ),
        migrations.DeleteModel(
            name="balance_sheet",
        ),
        migrations.DeleteModel(
            name="bugeting",
        ),
        migrations.DeleteModel(
            name="donor_management",
        ),
        migrations.DeleteModel(
            name="funding_accounting",
        ),
        migrations.DeleteModel(
            name="grant_tracking",
        ),
        migrations.DeleteModel(
            name="irs_fillings",
        ),
        migrations.RenameField(
            model_name="incomestatement",
            old_name="restricted_funds",
            new_name="restrictedFunds",
        ),
        migrations.RenameField(
            model_name="incomestatement",
            old_name="revenue_source",
            new_name="revenueSource",
        ),
        migrations.RenameField(
            model_name="incomestatement",
            old_name="unrestricted_funds",
            new_name="unrestrictedFunds",
        ),
    ]
