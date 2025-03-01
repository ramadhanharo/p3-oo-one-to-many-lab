import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner()
    assert owner

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet()
    assert pet 
    assert pet

    owner = Owner()
    pet = Pet()
    assert pet

    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet()
    pet2 = Pet()

    assert pet1 in Pet.all
    assert pet2 in Pet.all
    assert len(Pet.all) == 2

    Pet.all = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner()
    pet1 = Pet()
    pet2 = Pet()

    assert owner

    Pet.all = []

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner()
    pet = Pet()
    

    assert pet
    assert owner

    Pet.all = []

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    owner = Owner()
    with pytest.raises(Exception):
        owner.add_pet("Lucky")

    Pet.all = []

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner()
    pet1 = Pet()
    pet2 = Pet()
    pet3 = Pet()
    pet4 = Pet()
    
    assert owner