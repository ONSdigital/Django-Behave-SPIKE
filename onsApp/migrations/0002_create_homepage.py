from django.db import migrations, models


def create_homepage(apps, schema_editor):
    # Get the HomePage model
    HomePage = apps.get_model("onsApp", "HomePage")

    # Create a new homepage instance
    HomePage.objects.create(
        title="ONS Static Site Template",
        hero_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare nisl ac dolor dapibus, non mattis sapien egestas.",
        hero_button_text="Go to page 1",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("onsApp", "0001_initial"),  # Adjust this to your actual initial migration file
    ]

    operations = [
        migrations.RunPython(create_homepage),
    ]