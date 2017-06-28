from products.models import Product, Cosmetics

p = Product(
	juid = '001',
	category = "Lipstick",
	name = "Dark Side",
	net_weight = 3,
	brand = "Mac"
)
p.save()

c = Cosmetics(
	product=p,
	product_type = "Lipstick"
)
c.save()
