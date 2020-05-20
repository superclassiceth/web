# Generated by Django 2.2.4 on 2020-05-19 14:17

from django.db import migrations, models

def populateFunderAddress(apps, schema_editor):
    BountyFulfillment = apps.get_model('dashboard', 'BountyFulfillment')

    for fulfillment in BountyFulfillment.objects.all():
        fulfillment.funder_address = fulfillment.bounty.bounty_owner_address

        fulfillment.funder_profile = fulfillment.bounty.bounty_owner_profile

        if fulfillment.bounty.web3_type == 'qr':
            fulfillment.payout_type = 'qr'
            fulfillment.tenant = fulfillment.token_name
        else:
            fulfillment.payout_type = 'bounties_network'
            fulfillment.tenant = 'ETH'
            if not fulfillment.token_name:
                fulfillment.token_name = fulfillment.bounty.token_name


        print(fulfillment)

        fulfillment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0109_auto_20200519_1417'),
    ]

    operations = [
        migrations.RunPython(populateFunderAddress)
    ]
