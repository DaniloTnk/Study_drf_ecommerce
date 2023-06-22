import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        test_category = category_factory(name="Testing category str")
        # Assert
        assert test_category.__str__() == "Testing category str"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        test_brand = brand_factory(name="Testing brand str")
        # Assert
        assert test_brand.__str__() == "Testing brand str"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        test_brand = product_factory(name="Testing product str")
        # Assert
        assert test_brand.__str__() == "Testing product str"
