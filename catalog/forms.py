from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product
from .mixins import FormControlMixin
from PIL import Image

SPAM_WORDS = ["казино", "биржа", "обман", "криптовалюта", "дешево", "полиция", "крипта", "бесплатно", "радар"]

class ProductForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "image"]
        exclude = ["created_at", "updated_at"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"placeholder": "Введите название"})
        self.fields["price"].widget.attrs.update({"placeholder": "Введите цену"})
        self.fields["description"].widget.attrs.update({"placeholder": "Введите описание"})


    def clean_name(self):
        cleaned_name = self.cleaned_data["name"]  # Оригинал
        check_name = cleaned_name.lower()
        for word in SPAM_WORDS:
            if word in check_name:
                raise ValidationError(f"Слово \"{word}\" является запрещенным словом в названии")
        return cleaned_name


    def clean_description(self):
        cleaned_description = self.cleaned_data["description"]
        check_description = cleaned_description.lower()
        for word in SPAM_WORDS:
            if word in check_description:
                raise ValidationError(f"Слово \"{word}\" является запрещенным словом в описании")
        return cleaned_description


    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


    def clean_image(self):
        image = self.cleaned_data.get("image")
        max_size_mb = 5
        if image.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f"Файл слишком большой (не более {max_size_mb} МБ)")

        valid_formats = ["JPEG", "PNG"]
        try:
            img = Image.open(image)
            if img.format not in valid_formats:
                raise ValidationError(f"Неподдерживаемый формат. Разрешены: {', '.join(valid_formats)}")
        except Exception:
            raise ValidationError("Невозможно прочитать изображение")

        return image