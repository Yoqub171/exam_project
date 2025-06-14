from django.dispatch import receiver
from .models import Product
from uuid import uuid4
from django.db.models.signals import pre_delete, pre_save, post_delete, post_save
import json

@receiver(post_save, sender=Product)
def send_message_after_save(sender, instance, created, **kwargs):
    if created:
        instance.code = str(uuid4())
        instance.save()
        print('****************************')
        print(f'{instance.name} is succesfully created')
        print('****************************')

    # if not created:  
    #     print('****************************************')
    #     print(f'{instance.name} is succesfully updated')
    #     print('****************************************')


@receiver(pre_delete, sender=Product)
def save_product_before_delete(sender, instance, **kwargs):
    data = {
        "id": instance.id,
        "name": instance.name,
        "description": instance.description,
        "price": str(instance.price),
        "discount": str(instance.discount),
        "category": str(instance.category),
        "long_description": instance.long_description,
        "code": instance.code,

    }
    with open(f"product_{instance.id}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"{instance.name} succesfully saved saved.")
