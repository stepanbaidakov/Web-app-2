from .models import Product

class CategoryService:

    @staticmethod
    def products_in_category(category_id):
        return Product.objects.filter(category_id=category_id)