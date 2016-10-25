# Test technique Django badges pour modèles 3D

Cette application Django permet à un internaute de créer un compte puis de simuler l'upload de modèles 3D (page models/new). 

Des badges lui sont automatiquement attribués lors de certains évènements.

Fonctionnalités implémentées :
  - authentification avec informations supplémentaires (lien OnetoOne entre les modèles User et RegisteredUser)
  - création de nouveaux objets correspondant aux modèles 3D (vue générique CreateView)
  - badges attribués via des signaux pour découplage le plus effectif possible
  - tests unitaires vérifiant l'attribution des badges
  - API (django-rest-framework) pour obtenir la liste des utilisateurs, des modèles, des badges.

  
Les templates HTML sont plus que basiques, ils se contentent d'afficher les messages passés à l'utilisateur et les champs de formulaires à remplir.
