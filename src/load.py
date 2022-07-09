from namedb import get
def load(user_id: int):
  return get(user_id, categorie="language")
