from django.db import models


class Future(models.Model):
    name = models.CharField(max_length=50)
    ask = models.FloatField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    change1h = models.FloatField(blank=True, null=True)
    change24h = models.FloatField(blank=True, null=True)
    change_bod = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
    expired = models.BooleanField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    expiry_description = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    imf_factor = models.FloatField(blank=True, null=True)
    index = models.FloatField(blank=True, null=True)
    last = models.FloatField(blank=True, null=True)
    lower_bound = models.FloatField(blank=True, null=True)
    margin_price = models.FloatField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    move_start = models.DateTimeField(blank=True, null=True)
    perpetual = models.BooleanField(blank=True, null=True)
    position_limit_weight = models.FloatField(blank=True, null=True)
    post_only = models.BooleanField(blank=True, null=True)
    price_increment = models.FloatField(blank=True, null=True)
    size_increment = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=50)
    underlying = models.CharField(max_length=50)
    underlying_description = models.TextField(blank=True, null=True)
    upper_bound = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_usd24h = models.FloatField(blank=True, null=True)
    next_funding_rate = models.FloatField(blank=True, null=True)
    next_funding_time = models.DateTimeField(blank=True, null=True)
    open_interest = models.FloatField(blank=True, null=True)
    predicted_expiration_price = models.FloatField(blank=True, null=True)
    strike_price = models.FloatField(blank=True, null=True)
    delta = models.FloatField(blank=True, null=True)
    gamma = models.FloatField(blank=True, null=True)
    implied_volatility = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pair(models.Model):
    pair_a = models.ForeignKey(Future, related_name='a_pairs', on_delete=models.CASCADE)
    pair_b = models.ForeignKey(Future, related_name='b_pairs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return f'{self.pair_a}/{self.pair_b}'

    def __str__(self):
        return f'{self.pair_a}/{self.pair_b}'


class Spread(models.Model):
    pair = models.ForeignKey(Pair, related_name='spreads', on_delete=models.CASCADE)
    buy_spread = models.FloatField()
    sell_spread = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pair)

    class Meta:
        ordering = ['created_at']
