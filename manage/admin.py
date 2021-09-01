from django.contrib import admin
from .models.premium_subscription import PremiumSubscriptions
from .models.shows_domain import ShowDomains
from .models.show import Show
from .models.episode import Episode
# Register your models here.
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(ShowDomains)
admin.site.register(PremiumSubscriptions)
