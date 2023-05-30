# Template pour les challenges OCI

Template pour les challenges d'OCI avec extensions VSCode et infrastructure de
testing installée.

## Code source

Le challenge doit être codé dans le dossier ``src/``. Le point d'entrée est
``main.py``

## Tests automatiques

Les tests automatiques se trouvent dans le dossier ``tests/``. En principe, vous
ne devez pas modifier les fichiers présents dans ce dossier. En revanche, vous
pouvez compléter avec vos propres tests en créant un nouveau fichier
``test_*.py`` dans le dossiers ``tests/``.